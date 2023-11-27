import json
import datetime
import time

def date():
    #!Store the current date and time
    current_datetime = datetime.datetime.now()
    date = current_datetime.strftime("%Y-%m-%d")
    time_str = current_datetime.strftime("%H:%M:%S")

    with open("bot.json", "r") as json_file:
        data = json.load(json_file)
    if data:
        current_date = ("Today date is " + date)
        data[0]["bot_response"] = current_date
        current_time = ("Today time is " + time_str)
        data[1]["bot_response"] = current_time
        current_dateAndtime = ("Today date and time is " + date + " " + time_str)
        data[2]["bot_response"] = current_dateAndtime
    with open("bot.json", "w") as json_file:
        json.dump(data, json_file, indent=2)