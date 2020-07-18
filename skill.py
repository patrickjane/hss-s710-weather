# -----------------------------------------------------------------------------
# rhasspy Weather + DarkSky
# -----------------------------------------------------------------------------
# Copyright 2020 Patrick Fial
# -----------------------------------------------------------------------------
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

import time
import ssl
import certifi
import requests
import json
import locale
import calendar

from datetime import datetime, timedelta

import geopy.geocoders
from geopy.geocoders import Nominatim
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx

from hss_skill import hss

SKILL_ID = "s710-weather"
FORECAST_URL = "https://api.darksky.net/forecast/"

# -----------------------------------------------------------------------------
# class Skill
# -----------------------------------------------------------------------------

class Skill(hss.BaseSkill):

    # --------------------------------------------------------------------------
    # ctor
    # --------------------------------------------------------------------------

    def __init__(self):
        super().__init__()

        self.api_key = None
        self.home_location = None
        self.geolocator = Nominatim(user_agent = SKILL_ID, scheme="http")
        self.unit = 'si'

        LT.set_lang(self.default_language)
        locale.setlocale(locale.LC_ALL, self.default_language)

        self.weekdays = list(calendar.day_name)
        self.day_range_symbols = ['Morning', 'Forenoon', 'Noon', 'Afternoon', 'Evening', 'Night']
        self.hour_ranges = { 'Morning': (6, 10), 'Forenoon': (9, 12), 'Noon': (11, 14), 'Afternoon': (14,17), 'Evening': (17,22), 'Night': (22, -1) }

        self.http_headers = { 'Accept-Encoding': 'deflate, gzip' }
        self.http_lang = self.default_language[:2]

        if 'api_key' in self.config['skill']:
            self.api_key = self.config['skill']['api_key']

        if 'homecity' in self.config['skill']:
            homecity = self.config['skill']['homecity']

        if 'unit' in self.config['skill']:
            self.unit = self.config['skill']['unit']

        if not self.api_key or not homecity:
            raise Exception("Invalid/incomplete configuration (missing api_key/homecity)")

        try:
            loc = self.geolocator.geocode(homecity)
            self.home_location = (loc.latitude, loc.longitude)
        except Exception as e:
            self.log.error("Error: Failed to determine homecity coordinates for '{}' ({})".format(homecity, e))
            raise Exception("Failed to determine homecity coordinates")

    # --------------------------------------------------------------------------
    # handle (overwrites BaseSkill.handle)
    # --------------------------------------------------------------------------

    async def handle(self, request, session_id, site_id, intent_name, slots, mapped_slots):
        city = slots["location"] if "location" in slots else None
        time = slots["time"] if "time" in slots else None
        timeid = mapped_slots["time"] if "time" in mapped_slots else None

        self.log.debug("Intent {} with city {} and time {}".format(intent_name, city if city else '-', time if time else '-'))

        try:
            response_message = self.query_weather(intent_name, city, time, timeid)
        except Exception as e:
            self.log.error("Failed to query weather ({})".format(e))

        if self.develop:
            print(response_message)

        if not response_message:
            response_message = LT.errWeather

        return self.answer(session_id, site_id, response_message)

    # -------------------------------------------------------------------------
    # query_weather

    def query_weather(self, intent_name, city, time, timeid):

        # get corresponding home assistant service-url + payload

        try:
            req_url = self.get_request_url(city, self.home_location)
        except Exception as e:
            self.log.error("Failed to execute location HTTP request ({})".format(e))
            return None

        if not req_url:
            self.log.error("Failed to determine forecast URL/parameters, cannot query weather")
            return None

        self.log.debug("Debug: Querying URL [{}]".format(req_url.replace(self.api_key, "API_KEY")))

        try:
            req = requests.get(req_url, headers = self.http_headers, params = { 'units': self.unit, 'lang': self.http_lang, 'exclude': 'flags,alerts,minutely', 'extend': 'hourly' })
        except Exception as e:
            self.log.error("Failed to execute weather HTTP request ({})".format(e))
            return None

        if req.status_code != 200:
            self.log.error("Failed to query dark sky forecast (HTTP {} / {})".format(req.status_code, req.content.decode('utf-8')[:80] if req.content else "-"))
            return None

        try:
            response_content = json.loads(req.content.decode('utf-8'))
        except Exception as e:
            self.log.error("Failed to parse response content from dark sky ({})".format(e))
            return None

        try:
            response_message = self.process_response(intent_name, response_content, time, timeid)
        except Exception as e:
            self.log.error("Failed to parse response content from dark sky ({})".format(e))
            return None

        return response_message

    # -------------------------------------------------------------------------
    # get_request_url

    def get_request_url(self, city = None, coordinates = None):
        location = coordinates

        if city is not None:
            try:
                loc = self.geolocator.geocode(city)
                location = (loc.latitude, loc.longitude)
            except Exception as e:
                self.log.error("Failed to query coordinates for city '{}' ({})".format(city, e))
                return None

        if not location:
            return None

        return FORECAST_URL + self.api_key + "/" + str(location[0]) + "," + str(location[1])

    # -------------------------------------------------------------------------
    # process_response

    def process_response(self, intent_name, response_content, time, timeid):
        scale, tme_from, tme_to, prefix = self.get_timerange(time, timeid)
        weather = self.select_weather(response_content, scale, tme_from, tme_to)

        if not weather or not weather[0] or (scale == 'daily' and not weather[1]):
            self.log.warning('Failed to get weather info for requested range ({} - {})'.format(tme_from, tme_to))
            return None

        self.log.debug("Check weather with scale {} and prefix {}".format(scale, prefix))

        if intent_name == 's710:getForecast':
            return self.process_forecast(intent_name, scale, weather, prefix)

        if intent_name == 's710:getTemperature':
            return self.process_temperature(intent_name, scale, weather, prefix)

        if intent_name == 's710:hasRain':
            return self.process_has(intent_name, 'rain', scale, weather, prefix)

        if intent_name == 's710:hasSun':
            return self.process_has(intent_name, 'sun', scale, weather, prefix)

        if intent_name == 's710:hasSnow':
            return self.process_has(intent_name, 'snow', scale, weather, prefix)

        self.log.error("Intent {}/parameters not recognized, ignoring".format(intent_name))
        return None

    # -------------------------------------------------------------------------
    # process_forecast

    def process_forecast(self, intent_name, scale, weather_hours_and_days, prefix):
        def get_summary(wx_object, remove_dot = False):
            sum = wx_object['summary']

            if not remove_dot and not sum.endswith('.'):
                sum = sum + '.'

            if remove_dot and sum.endswith('.'):
                sum = sum[:-1]

            return sum

        def get_wx_on(what, data):
            if len(data) == 1:
                return LT.fmtPhenom1.format(what, data[0])

            return LT.fmtPhenom2.format(what, ', '.join(data[:-1]), data[-1]) if data else ''

        # 'jetzt'

        if scale == 'currently':
            return LT.fmtCurrentWx.format(get_summary(weather_hours_and_days[0]), str(round(weather_hours_and_days[0]['temperature'])))

        elif scale == 'daily':
            days = weather_hours_and_days[1]
            temps_max = [w['temperatureMax'] for w in days]
            temps_min = [w['temperatureMin'] for w in days]

            # 'morgen', 'dienstag', 'heute'

            if len(days) == 1:
                return LT.fmt1DayWx.format(prefix, get_summary(days[0]), str(round(days[0]['temperatureMin'])), str(round(days[0]['temperatureMax'])))

            # wochenende

            if len(days) == 2:
                day1 = datetime.fromtimestamp(days[0]['time']).weekday()
                day2 = datetime.fromtimestamp(days[1]['time']).weekday()

                if days[0]['summary'] == days[1]['summary']:
                    return LT.fmtWeekend1Wx.format(self.weekdays[day1].capitalize(),
                            self.weekdays[day2].capitalize(), get_summary(days[0]),
                            str(round(min(temps_min))), str(round(max(temps_max))))

                return LT.fmtWeekend2Wx.format(self.weekdays[day1].capitalize(), get_summary(days[0]),
                        self.weekdays[day2].capitalize(), get_summary(days[1]),
                        str(round(min(temps_min))), str(round(max(temps_max))))

            # more than 2 multiple days ('diese Woche', 'nächste Woche')

            day1 = self.weekdays[datetime.fromtimestamp(days[0]['time']).weekday()].capitalize()

            rain_days = [self.weekdays[datetime.fromtimestamp(w['time']).weekday()].capitalize() for w in days if w['icon'] == 'rain' and w['time'] != days[0]['time']]
            snow_days = [self.weekdays[datetime.fromtimestamp(w['time']).weekday()].capitalize() for w in days if w['icon'] == 'snow' and w['time'] != days[0]['time']]
            thunder_days = [self.weekdays[datetime.fromtimestamp(w['time']).weekday()].capitalize() for w in days if w['icon'] == 'thunderstorm' and w['time'] != days[0]['time']]

            rain_on =  get_wx_on(LT._rain, rain_days)
            snow_on = get_wx_on(LT._snow, snow_days)
            thunder_on = get_wx_on(LT._thunder, thunder_days)

            return LT.fmt1DayWx.format(day1, get_summary(days[0]), str(round(min(temps_min))), str(round(max(temps_max)))) + rain_on + snow_on + thunder_on
        else:
            hours = weather_hours_and_days[0]
            temps = [w['temperature'] for w in hours]

            if hours[0]['summary'] == hours[-1]['summary']:
                return LT.fmt1DayWx.format(prefix, get_summary(hours[0]), str(round(min(temps))), str(round(max(temps))))

            return LT.fmtHoursWx.format(prefix, get_summary(hours[0], True), get_summary(hours[-1]), str(round(min(temps))), str(round(max(temps))))

        return None

    # -------------------------------------------------------------------------
    # process_temperature

    def process_temperature(self, intent_name, scale, weather_hours_and_days, prefix):
        weather = weather_hours_and_days[0]

        if scale == 'currently' and 'temperature' in weather:
            return LT.fmtCurrentTemp.format(str(round(weather['temperature'])))

        weather = weather_hours_and_days[0]

        if len(weather) == 1:
            return LT.fmtDayTemp1.format(prefix, str(round(weather[0]['temperature'])))

        temps = [w['temperature'] for w in weather]

        return LT.fmtDayTemp2.format(prefix, str(round(min(temps))), str(round(max(temps))))

    # -------------------------------------------------------------------------
    # process_has

    def process_has(self, intent_name, what, scale, weather_hours_and_days, prefix):
        weather = weather_hours_and_days[0]
        weather_days = weather_hours_and_days[1]

        if scale == 'currently':
            if what == 'sun':
                if 'icon' in weather and weather['icon'] == 'clear-day':
                    return LT.fmtSunny

                if 'icon' in weather and 'cloudy' in weather['icon']:
                    return LT.fmtCloudy1 if weather['icon'] is not 'cloudy' else LT.fmtCloudy2

                return LT.fmtNope
            else:
                if 'precipType' not in weather or weather['precipType'] is not what or 'precipProbability' not in weather or weather['precipProbability'] < 0.3:
                    return LT.fmtNotPhenom.format(LT._raining if what == 'rain' else LT._snowing)

                if weather['precipProbability'] < 0.75:
                    return LT.fmtMaybePhenom.format(LT._raining if what == 'rain' else LT._snowing)

                return LT.fmtYesPhenom.format(LT._raining if what == 'rain' else LT._snowing)
        else:
            if what == 'sun':
                hasSun = [w for w in weather if w['icon'] == 'clear-day']
                hasPartly = [w for w in weather if w['icon'] == 'partly-cloudy-day']

                if not hasSun and not hasPartly:
                    return LT.fmtNope

                w = hasSun[0] if hasSun else hasPartly[0]
                dt = datetime.fromtimestamp(w['time'])
                day = self.weekdays[dt.weekday()]
                when = dt.strftime(LT.fmtHourString)

                if scale == 'hourly':
                    return LT.fmtHourPhenom1.format(when, LT._sunny) if hasSun else LT.fmtHourPhenom2.format(when, LT._sunny)
                elif len(weather_days) == 1:
                    return LT.fmtDayPhenom1.format(prefix, when, LT._sunny) if hasSun else LT.fmtDayPhenom2.format(prefix, when, LT._sunny)

                prefix = LT._on + day.capitalize()
                return LT.fmtDayPhenom1.format(prefix, when, LT._sunny) if hasSun else LT.fmtDayPhenom2.format(prefix, when, LT._sunny)
            else:
                hasRain = [w for w in weather if w['icon'] == 'rain' or ('precipType' in w and w['precipType'] == what and 'precipProbability' in w and w['precipProbability'] > 0.3)]
                hasHail = [w for w in weather if w['icon'] == 'hail' or ('precipType' in w and w['precipType'] == what and 'precipProbability' in w and w['precipProbability'] > 0.3)]
                hasThunder = [w for w in weather if w['icon'] == 'thunderstorm' or ('precipType' in w and w['precipType'] == what and 'precipProbability' in w and w['precipProbability'] > 0.3)]

                if not hasRain and not hasHail and not hasThunder:
                    return LT.fmtNope

                w = hasRain[0] if hasRain else (hasHail[0] if hasHail else hasThunder[0])
                dt = datetime.fromtimestamp(w['time'])
                day = self.weekdays[dt.weekday()]
                when = dt.strftime(LT.fmtHourString)

                if w['precipProbability'] < 0.3:
                    return LT.fmtNope

                if scale == 'hourly':
                    return LT.fmtHourPhenom1.format(when, LT._raining if hasRain else (LT._hailing if hasHail else LT._thundering))
                elif len(weather_days) == 1:
                    return LT.fmtDayPhenom3.format(prefix, LT._raining if hasRain else (LT._hailing if hasHail else LT._thundering))

                if w['precipProbability'] < 0.75:
                    return LT.fmtDayPhenom4.format(LT._on + day.capitalize(), when, LT._raining if hasRain else (LT._hailing if hasHail else LT._thundering))

                return LT.fmtDayPhenom1.format(LT._on + day.capitalize(), when, LT._raining if hasRain else (LT._hailing if hasHail else LT._thundering))

                return 'Am ' + day.capitalize() + ' wird es' + prob + ' gegen ' + when + ' ' + ('regnen.' if hasRain else ('hageln.' if hasHail else 'Gewitter geben.'))

        return None

    # -------------------------------------------------------------------------
    # select_weather

    def select_weather(self, weather, scale, tme_from, tme_to):
        res = None

        try:
            if scale == 'currently':
                return (weather['currently'], None)

            hours = [hour for hour in weather['hourly']['data'] if hour['time'] >= tme_from and hour['time'] <= tme_to]
            days = [day for day in weather['daily']['data'] if day['time'] >= tme_from and day['time'] <= tme_to]

            return (hours, days)

        except Exception as e:
            self.log.error('Failed to parse response contents ({})'.format(e))
            return None

        return res

    # -------------------------------------------------------------------------
    # get_timerange

    def get_timerange(self, time_string, timeid):
        if not time_string:
            return ('currently', None, None, 'Jetzt')

        # single weekdays

        contained_weekdays = [day for day in self.weekdays if day.lower() in time_string.lower()]

        if contained_weekdays:
            return self.get_weekday(self.weekdays.index(contained_weekdays[0]), time_string)

        # week-ends (sat+sun)

        if timeid == "weekend":
            return self.get_weekend_range(time_string)

        # whole week

        if 'week' in timeid.lower():
            return self.get_week_range(time_string, timeid)

        # whole day for specific day

        if timeid == 'today':
            return self.get_day_range(time.time(), LT._today)

        if timeid == 'tomorrow':
            return self.get_day_range(time.time() + 1 * 24 * 60 * 60, LT._tomorrow)

        if timeid == 'dayAfter':
            return self.get_day_range(time.time() + 2 * 24 * 60 * 60, LT._dayAfter)

        contained_day_range_symbols = [sym for sym in self.day_range_symbols if sym in timeid]

        # hour range of specific day

        if contained_day_range_symbols:
            if 'dayAfter' in timeid:
                return self.get_subrange(time_string, time.time() + 2 * 24 * 60 * 60, timeid) #'Übermorgen')

            if 'tomorrow' in timeid:
                return self.get_subrange(time_string, time.time() + 1 * 24 * 60 * 60, timeid) #'Morgen')

            return self.get_subrange(time_string, time.time(), timeid) #'Heute')

        return ('currently', None, None, 'Jetzt')

    # -------------------------------------------------------------------------
    # timerange helpers

    def get_day_range(self, epoch, prefix):
        dt1 = datetime.fromtimestamp(epoch).replace(minute = 0, hour = 0, second = 0, microsecond= 0)
        dt2 = datetime.fromtimestamp(epoch).replace(minute = 59, hour = 23, second = 59, microsecond= 0)

        return ('daily', dt1.timestamp(), dt2.timestamp(), prefix)

    def get_subrange(self, time_string, epoch, timeid):
        hour_range = None

        for key,v in self.hour_ranges.items():
            if key in timeid:
                hour_range = v
                break

        return self.get_hour_range(epoch, hour_range[0], hour_range[1], time_string)

    def get_hour_range(self, epoch, hours_from, hours_to, prefix):
        dt1 = datetime.fromtimestamp(epoch).replace(minute = 0, hour = hours_from, second = 0, microsecond= 0)
        dt2 = dt1

        if hours_to == -1: # nasty, i know -> next day 3:00
            dt2 = datetime.fromtimestamp(epoch + 1 * 24 * 60 * 60).replace(minute = 0, hour = 3, second = 0, microsecond= 0)
        else:
            dt2 = datetime.fromtimestamp(epoch).replace(minute = 0, hour = hours_to, second = 0, microsecond= 0)

        return ('hourly', dt1.timestamp(), dt2.timestamp(), prefix)

    def get_weekend_range(self, time_string):
        dt = datetime.fromtimestamp(time.time()).replace(minute = 0, hour = 0, second = 0, microsecond = 0)
        offset = 5 - dt.weekday()

        dt1 = dt + timedelta(days = offset)
        dt2 = dt1 + timedelta(days = 1)
        dt2 = dt2 + timedelta(hours = 23, minutes = 59)

        return ('daily', dt1.timestamp(), dt2.timestamp(), LT._for + LT.capitalize(time_string))

    def get_week_range(self, time_string, timeid):
        dt = datetime.fromtimestamp(time.time()).replace(minute = 0, hour = 0, second = 0, microsecond = 0)

        monday = dt + timedelta(days = 0 - dt.weekday())
        sunday = monday + timedelta(days = 6)
        sunday = sunday + timedelta(hours = 23, minutes = 59)

        if 'next' in timeid:
            dt1 = monday + timedelta(days = 7)
            dt2 = sunday + timedelta(days = 7)

            return ('daily', dt1.timestamp(), dt2.timestamp(), LT.capitalize(time_string))

        return ('daily', monday.timestamp(), sunday.timestamp(), LT.capitalize(time_string))

    def get_weekday(self, day, day_string):
        dt1 = datetime.fromtimestamp(time.time()).replace(minute = 0, hour = 0, second = 0, microsecond = 0)
        offset = day - dt1.weekday()

        if offset <= 0:
            offset = offset + 7

        dt1 = dt1 + timedelta(days = offset)
        dt2 = dt1.replace(minute = 59, hour = 23, second = 59, microsecond = 0)

        return ('daily', dt1.timestamp(), dt2.timestamp(), LT._on + LT.capitalize(day_string))

# -----------------------------------------------------------------------------
# class LT
# -----------------------------------------------------------------------------

class LT:
    lang = None
    _on = None
    _for = None
    _snow = None
    _rain = None
    _thunder = None
    _raining = None
    _snowing = None
    _sunny = None
    _raining = None
    _hailing = None
    _thundering = None
    _today = None
    _tomorrow = None
    _dayAfter = None

    errWeather = None
    fmtHourString = None
    fmtCurrentWx = None
    fmt1DayWx = None
    fmtHoursWx = None
    fmtWeekend1Wx = None
    fmtWeekend2Wx = None
    fmtPhenom1 = None
    fmtPhenom2 = None
    fmtCurrentTemp = None
    fmtDayTemp1 = None
    fmtDayTemp2 = None
    fmtNope = None
    fmtSunny = None
    fmtCloudy1 = None
    fmtCloudy2 = None
    fmtNotPhenom = None
    fmtMaybePhenom = None
    fmtYesPhenom = None
    fmtHourPhenom1 = None
    fmtHourPhenom2 = None
    fmtDayPhenom1 = None
    fmtDayPhenom2 = None
    fmtDayPhenom3 = None
    fmtDayPhenom4 = None

    def set_lang(to):
        if LT.lang == to:
            return

        LT.lang = to

        if LT.lang.startswith("de"):
            LT.errWeather = "Wetter konnte nicht abgefragt werden"
            LT._on = "Am "
            LT._for = "Am "
            LT._snow = 'Schnee'
            LT._rain = 'Regen'
            LT._thunder = 'Gewitter'
            LT._raining = 'regnet'
            LT._snowing = 'schneit'
            LT._sunny = 'sonnig'
            LT._raining = 'regnen'
            LT._hailing = 'hageln'
            LT._thundering = 'Gewitter geben'
            LT._today = 'Heute'
            LT._tomorrow = 'Morgen'
            LT._dayAfter = 'Übermorgen'
            LT.fmtHourString = '%H:%M Uhr'
            LT.fmtPhenom1 = ' Vermutlich {} am {}.'
            LT.fmtPhenom2 = ' Vermutlich {} am {} und {}.'
            LT.fmtCurrentWx = 'Das Wetter ist aktuell {} Temperatur liegt bei {} Grad.'
            LT.fmt1DayWx = 'Wetter {}: {} Temperaturen zwischen {} und {} Grad.'
            LT.fmtWeekend1Wx = 'Wetter am {} und {}: {} Die Temperaturen liegen zwischen {} und {} Grad.'
            LT.fmtWeekend2Wx = 'Wetter am {}: {} {} {} Die Temperaturen liegen zwischen {} und {} Grad.'
            LT.fmtHoursWx = 'Wetter {}: {} bis {} Temperaturen zwischen {} und {} Grad.'
            LT.fmtCurrentTemp = 'Es sind gerade {} Grad.'
            LT.fmtDayTemp1 = '{} wird es etwa {} Grad warm.'
            LT.fmtDayTemp2 = '{} wird es zwischen {} und {} Grad warm.'
            LT.fmtNope = 'Nein, ich denke nicht.'
            LT.fmtSunny = 'Ja, es ist gerade sonnig.'
            LT.fmtCloudy1 = 'Nein, es ist gerade eher bewölkt.'
            LT.fmtCloudy2 = 'Nein, es ist gerade bewölkt.'
            LT.fmtNotPhenom = 'Ich denke nicht, dass es gerade {}.'
            LT.fmtMaybePhenom = 'Ja, es {} gerade vermutlich.'
            LT.fmtYesPhenom = 'Ja, es {} gerade.'
            LT.fmtHourPhenom1 = 'Gegen {} wird es {}.'
            LT.fmtHourPhenom2 = 'Gegen {} wird es ein bisschen {}.'
            LT.fmtDayPhenom1 = '{} wird es gegen {} {}.'
            LT.fmtDayPhenom2 = '{} wird es gegen {} ein bisschen {}.'
            LT.fmtDayPhenom3 = '{} wird es {}.'
            LT.fmtDayPhenom4 = '{} wird es vermutlich gegen {} {}.'

        elif LT.lang.startswith("en"):
            LT.errWeather = "Failed to query weather"
            LT._on = ""
            LT._for = ""
            LT._snow = 'snow'
            LT._rain = 'rain'
            LT._thunder = 'thunderstorms'
            LT._raining = 'raining'
            LT._snowing = 'snowing'
            LT._sunny = 'sunny'
            LT._raining = 'raining'
            LT._hailing = 'hailing'
            LT._thundering = 'thundering'
            LT._today = 'today'
            LT._tomorrow = 'tomorrow'
            LT._dayAfter = 'day after tomorrow'
            LT.fmtHourString = '%I:%M %p'
            LT.fmtPhenom1 = ' Likely {} on {}.'
            LT.fmtPhenom2 = ' Likely {} on {} and {}.'
            LT.fmtCurrentWx = 'Weather currently {} Temperature at {} degrees.'
            LT.fmt1DayWx = 'Weather {}: {} Temperature between {} and {} degrees.'
            LT.fmtWeekend1Wx = 'Weather on {} and {}: {} Temperature between {} and {} degrees.'
            LT.fmtWeekend2Wx = 'Weather on {}: {} {} {} Temperature between {} and {} degrees.'
            LT.fmtHoursWx = 'Weather {}: {} to {} Temperature between {} and {} degrees.'
            LT.fmtCurrentTemp = 'Currently it\'s {} degrees.'
            LT.fmtDayTemp1 = '{} will be about {} degrees.'
            LT.fmtDayTemp2 = '{} will be between {} and {} degrees.'
            LT.fmtNope = 'No, I don\'t think so.'
            LT.fmtSunny = 'Yes, it\'s currently sunny.'
            LT.fmtCloudy1 = 'No, it\'s rather cloudy currently.'
            LT.fmtCloudy2 = 'No, it\'s cloudy currently.'
            LT.fmtNotPhenom = 'I don\'t think its {} currently.'
            LT.fmtMaybePhenom = 'Yes, probably it\'s {} currenlty.'
            LT.fmtYesPhenom = 'Yes, it\'s {} currenlty.'
            LT.fmtHourPhenom1 = 'It will be {1} around {0}.'
            LT.fmtHourPhenom2 = 'It will be a bit {1} around {0}.'
            LT.fmtDayPhenom1 = '{0} it will be {2} around {1}.'
            LT.fmtDayPhenom2 = '{0} it will be a bit {2} around {1}.'
            LT.fmtDayPhenom3 = '{} it will be {}.'
            LT.fmtDayPhenom4 = '{0} it will probably be {2} {1}.'

    def capitalize(str):
        if LT.lang.startswith("de"):
            return str.capitalize()

        return str