import requests
import re
import json

url = requests.get("http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?lang=en&region=gb&calendartype=blacklist&limit=100&dates=20171007&tz=Europe/London")
data = json.loads(url.content)

def games_played():
    for d in range(20171000, 20171032):

        url = requests.get("http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?lang=en&region=gb&calendartype=blacklist&limit=100&dates={}&tz=Europe/London".format(d))
        data = json.loads(url.content)
        for event in data["events"]:
            for comp in event["competitions"]:
                print("")
                print("At venue - " + comp["venue"]["fullName"] + ":")
                print("")
                for compet in comp["competitors"]:
                    if (compet["homeAway"] == "home"):
                        print(compet["team"]["displayName"])
                        print("VS")
                    elif(compet["homeAway"] == "away"):
                        print(compet["team"]["displayName"])
                        print("")
games_played()

# Below functions are not called

def show_teams():
    print("")
    print("Teams:")
    print("")
    for event in data["events"]:
        for comp in event["competitions"]:
            for compet in comp["competitors"]:
                print(compet["team"]["displayName"])
                print("")

def show_venues():
    print("")
    print("Arenas:")
    print("")
    for event in data["events"]:
        for arena in event["competitions"]:
            print(arena["venue"]["fullName"])

def home_teams():
    print("")
    print("Home teams:")
    print("")
    for event in data["events"]:
        for comp in event["competitions"]:
            for compet in comp["competitors"]:
                if (compet["homeAway"] == "home"):
                    print(compet["team"]["displayName"])

def away_teams():
    print("")
    print("Away teams:")
    print("")
    for event in data["events"]:
        for comp in event["competitions"]:
            for compet in comp["competitors"]:
                if (compet["homeAway"] == "away"):
                    print(compet["team"]["displayName"])




#>>> print(text.strip()[-200:-69])
