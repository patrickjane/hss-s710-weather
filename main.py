#!/usr/bin/env python
# -----------------------------------------------------------------------------
# HSS skill implementation
# Copyright (c) 2020 - Patrick Fial
# -----------------------------------------------------------------------------
# main.py
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

import skill
import asyncio

# ------------------------------------------------------------------------------
# main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    skill = skill.Skill()

    if not skill.develop:
        skill.run()
    else:
        loop = asyncio.get_event_loop()

        if skill.default_language.startswith("de"):
            pass
            # print("--------------------- s710:getForecast -------------------------")
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "jetzt"}, {"time": "now"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "heute"}, {"time": "today"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "heute früh"}, {"time": "todayMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "heute vormittag"}, {"time": "todayForenoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "gegen mittag"}, {"time": "todayNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "am nachmittag"}, {"time": "todayAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "am abend"}, {"time": "todayEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "in der nacht"}, {"time": "todayNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "morgen"}, {"time": "tomorrow"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "morgen früh"}, {"time": "tomorrowMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "morgen am vormittag"}, {"time": "tomorrowForenoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "morgen gegen mittag"}, {"time": "tomorrowNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "morgen am nachmittag"}, {"time": "tomorrowAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "morgen am abend"}, {"time": "tomorrowEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "morgen in der nacht"}, {"time": "tomorrowNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "übermorgen"}, {"time": "dayAfter"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "übermorgen früh"}, {"time": "dayAfterMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "übermorgen am vormittag"}, {"time": "dayAfterForenoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "übermorgen am mittag"}, {"time": "dayAfterNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "übermorgen nachmittag"}, {"time": "dayAfterAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "übermorgen gegen abend"}, {"time": "dayAfterEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "übermorgen in der nacht"}, {"time": "dayAfterNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "diese woche"}, {"time": "thisWeek"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "ende der woche"}, {"time": "weekend"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "nächste woche"}, {"time": "nextWeek"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "montag"}, {"time": "monday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "dienstag"}, {"time": "tuesday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "mittwoch"}, {"time": "wednesday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "donnerstag"}, {"time": "thursday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "freitag"}, {"time": "friday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "samstag"}, {"time": "saturday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "sonntag"}, {"time": "sunday"}));

            # print("--------------------- s710:getTemperature -------------------------")
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "jetzt"}, {"time": "now"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "heute"}, {"time": "today"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "heute früh"}, {"time": "todayMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "heute vormittag"}, {"time": "todayForenoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "gegen mittag"}, {"time": "todayNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "am nachmittag"}, {"time": "todayAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "am abend"}, {"time": "todayEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "in der nacht"}, {"time": "todayNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "morgen"}, {"time": "tomorrow"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "morgen früh"}, {"time": "tomorrowMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "morgen am vormittag"}, {"time": "tomorrowForenoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "morgen gegen mittag"}, {"time": "tomorrowNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "morgen am nachmittag"}, {"time": "tomorrowAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "morgen am abend"}, {"time": "tomorrowEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "morgen in der nacht"}, {"time": "tomorrowNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "übermorgen"}, {"time": "dayAfter"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "übermorgen früh"}, {"time": "dayAfterMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "übermorgen am vormittag"}, {"time": "dayAfterForenoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "übermorgen am mittag"}, {"time": "dayAfterNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "übermorgen nachmittag"}, {"time": "dayAfterAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "übermorgen gegen abend"}, {"time": "dayAfterEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "übermorgen in der nacht"}, {"time": "dayAfterNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "diese woche"}, {"time": "thisWeek"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "ende der woche"}, {"time": "weekend"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "nächste woche"}, {"time": "nextWeek"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "montag"}, {"time": "monday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "dienstag"}, {"time": "tuesday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "mittwoch"}, {"time": "wednesday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "donnerstag"}, {"time": "thursday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "freitag"}, {"time": "friday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "samstag"}, {"time": "saturday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "sonntag"}, {"time": "sunday"}));

            # print("--------------------- s710:hasSun -------------------------")
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "jetzt"}, {"time": "now"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "heute"}, {"time": "today"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "heute früh"}, {"time": "todayMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "heute vormittag"}, {"time": "todayForenoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "gegen mittag"}, {"time": "todayNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "am nachmittag"}, {"time": "todayAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "am abend"}, {"time": "todayEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "in der nacht"}, {"time": "todayNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "morgen"}, {"time": "tomorrow"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "morgen früh"}, {"time": "tomorrowMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "morgen am vormittag"}, {"time": "tomorrowForenoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "morgen gegen mittag"}, {"time": "tomorrowNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "morgen am nachmittag"}, {"time": "tomorrowAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "morgen am abend"}, {"time": "tomorrowEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "morgen in der nacht"}, {"time": "tomorrowNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "übermorgen"}, {"time": "dayAfter"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "übermorgen früh"}, {"time": "dayAfterMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "übermorgen am vormittag"}, {"time": "dayAfterForenoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "übermorgen am mittag"}, {"time": "dayAfterNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "übermorgen nachmittag"}, {"time": "dayAfterAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "übermorgen gegen abend"}, {"time": "dayAfterEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "übermorgen in der nacht"}, {"time": "dayAfterNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "diese woche"}, {"time": "thisWeek"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "ende der woche"}, {"time": "weekend"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "nächste woche"}, {"time": "nextWeek"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "montag"}, {"time": "monday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "dienstag"}, {"time": "tuesday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "mittwoch"}, {"time": "wednesday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "donnerstag"}, {"time": "thursday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "freitag"}, {"time": "friday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "samstag"}, {"time": "saturday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "sonntag"}, {"time": "sunday"}));

            # print("--------------------- s710:hasRain -------------------------")
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "jetzt"}, {"time": "now"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "heute"}, {"time": "today"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "heute früh"}, {"time": "todayMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "heute vormittag"}, {"time": "todayForenoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "gegen mittag"}, {"time": "todayNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "am nachmittag"}, {"time": "todayAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "am abend"}, {"time": "todayEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "in der nacht"}, {"time": "todayNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "morgen"}, {"time": "tomorrow"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "morgen früh"}, {"time": "tomorrowMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "morgen am vormittag"}, {"time": "tomorrowForenoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "morgen gegen mittag"}, {"time": "tomorrowNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "morgen am nachmittag"}, {"time": "tomorrowAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "morgen am abend"}, {"time": "tomorrowEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "morgen in der nacht"}, {"time": "tomorrowNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "übermorgen"}, {"time": "dayAfter"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "übermorgen früh"}, {"time": "dayAfterMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "übermorgen am vormittag"}, {"time": "dayAfterForenoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "übermorgen am mittag"}, {"time": "dayAfterNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "übermorgen nachmittag"}, {"time": "dayAfterAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "übermorgen gegen abend"}, {"time": "dayAfterEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "übermorgen in der nacht"}, {"time": "dayAfterNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "diese woche"}, {"time": "thisWeek"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "ende der woche"}, {"time": "weekend"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "nächste woche"}, {"time": "nextWeek"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "montag"}, {"time": "monday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "dienstag"}, {"time": "tuesday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "mittwoch"}, {"time": "wednesday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "donnerstag"}, {"time": "thursday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "freitag"}, {"time": "friday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "samstag"}, {"time": "saturday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "sonntag"}, {"time": "sunday"}));

        elif skill.default_language.startswith("en"):
            pass
            # print("--------------------- s710:getForecast -------------------------")
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "right now"}, {"time": "now"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "today"}, {"time": "today"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "ealier today"}, {"time": "todayMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "around noon"}, {"time": "todayNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "towards afternoon"}, {"time": "todayAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "this evening"}, {"time": "todayEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "at night"}, {"time": "todayNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "tomorrow"}, {"time": "tomorrow"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "tomorrow morning"}, {"time": "tomorrowMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "tomorrow around noon"}, {"time": "tomorrowNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "tomorrow afternoon"}, {"time": "tomorrowAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "tomorrow at evening"}, {"time": "tomorrowEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "tomorrow night"}, {"time": "tomorrowNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "day after tomorrow"}, {"time": "dayAfter"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "day after tomorrow morning"}, {"time": "dayAfterMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "day after tomorrow around noon"}, {"time": "dayAfterNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "day after tomorrow at afternoon"}, {"time": "dayAfterAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "day after tomorrow evening"}, {"time": "dayAfterEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "day after tomorrow night"}, {"time": "dayAfterNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "this week"}, {"time": "thisWeek"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "towards the end of the week"}, {"time": "weekend"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "in the next week"}, {"time": "nextWeek"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "monday"}, {"time": "monday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "tuesday"}, {"time": "tuesday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "wednesday"}, {"time": "wednesday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "thursday"}, {"time": "thursday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "friday"}, {"time": "friday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "saturday"}, {"time": "saturday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getForecast", {"time": "sunday"}, {"time": "sunday"}));

            # print("--------------------- s710:getTemperature -------------------------")
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "right now"}, {"time": "now"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "today"}, {"time": "today"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "ealier today"}, {"time": "todayMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "around noon"}, {"time": "todayNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "towards afternoon"}, {"time": "todayAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "this evening"}, {"time": "todayEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "at night"}, {"time": "todayNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "tomorrow"}, {"time": "tomorrow"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "tomorrow morning"}, {"time": "tomorrowMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "tomorrow around noon"}, {"time": "tomorrowNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "tomorrow afternoon"}, {"time": "tomorrowAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "tomorrow at evening"}, {"time": "tomorrowEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "tomorrow night"}, {"time": "tomorrowNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "day after tomorrow"}, {"time": "dayAfter"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "day after tomorrow morning"}, {"time": "dayAfterMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "day after tomorrow around noon"}, {"time": "dayAfterNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "day after tomorrow at afternoon"}, {"time": "dayAfterAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "day after tomorrow evening"}, {"time": "dayAfterEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "day after tomorrow night"}, {"time": "dayAfterNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "this week"}, {"time": "thisWeek"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "towards the end of the week"}, {"time": "weekend"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "in the next week"}, {"time": "nextWeek"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "monday"}, {"time": "monday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "tuesday"}, {"time": "tuesday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "wednesday"}, {"time": "wednesday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "thursday"}, {"time": "thursday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "friday"}, {"time": "friday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "saturday"}, {"time": "saturday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:getTemperature", {"time": "sunday"}, {"time": "sunday"}));

            # print("--------------------- s710:hasSun -------------------------")
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "right now"}, {"time": "now"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "today"}, {"time": "today"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "ealier today"}, {"time": "todayMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "around noon"}, {"time": "todayNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "towards afternoon"}, {"time": "todayAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "this evening"}, {"time": "todayEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "at night"}, {"time": "todayNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "tomorrow"}, {"time": "tomorrow"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "tomorrow morning"}, {"time": "tomorrowMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "tomorrow around noon"}, {"time": "tomorrowNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "tomorrow afternoon"}, {"time": "tomorrowAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "tomorrow at evening"}, {"time": "tomorrowEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "tomorrow night"}, {"time": "tomorrowNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "day after tomorrow"}, {"time": "dayAfter"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "day after tomorrow morning"}, {"time": "dayAfterMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "day after tomorrow around noon"}, {"time": "dayAfterNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "day after tomorrow at afternoon"}, {"time": "dayAfterAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "day after tomorrow evening"}, {"time": "dayAfterEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "day after tomorrow night"}, {"time": "dayAfterNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "this week"}, {"time": "thisWeek"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "towards the end of the week"}, {"time": "weekend"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "in the next week"}, {"time": "nextWeek"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "monday"}, {"time": "monday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "tuesday"}, {"time": "tuesday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "wednesday"}, {"time": "wednesday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "thursday"}, {"time": "thursday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "friday"}, {"time": "friday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "saturday"}, {"time": "saturday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasSun", {"time": "sunday"}, {"time": "sunday"}));

            # print("--------------------- s710:hasRain -------------------------")
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "right now"}, {"time": "now"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "today"}, {"time": "today"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "ealier today"}, {"time": "todayMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "around noon"}, {"time": "todayNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "towards afternoon"}, {"time": "todayAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "this evening"}, {"time": "todayEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "at night"}, {"time": "todayNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "tomorrow"}, {"time": "tomorrow"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "tomorrow morning"}, {"time": "tomorrowMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "tomorrow around noon"}, {"time": "tomorrowNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "tomorrow afternoon"}, {"time": "tomorrowAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "tomorrow at evening"}, {"time": "tomorrowEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "tomorrow night"}, {"time": "tomorrowNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "day after tomorrow"}, {"time": "dayAfter"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "day after tomorrow morning"}, {"time": "dayAfterMorning"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "day after tomorrow around noon"}, {"time": "dayAfterNoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "day after tomorrow at afternoon"}, {"time": "dayAfterAfternoon"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "day after tomorrow evening"}, {"time": "dayAfterEvening"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "day after tomorrow night"}, {"time": "dayAfterNight"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "this week"}, {"time": "thisWeek"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "towards the end of the week"}, {"time": "weekend"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "in the next week"}, {"time": "nextWeek"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "monday"}, {"time": "monday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "tuesday"}, {"time": "tuesday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "wednesday"}, {"time": "wednesday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "thursday"}, {"time": "thursday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "friday"}, {"time": "friday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "saturday"}, {"time": "saturday"}));
            # loop.run_until_complete(skill.handle({"empty": True}, "4aac32e9-cbf2-4bfd-a0a3-ae565ab19043", "default", "s710:hasRain", {"time": "sunday"}, {"time": "sunday"}));