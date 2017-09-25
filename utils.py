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
