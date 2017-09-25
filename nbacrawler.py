import requests
import re
import json
import datetime
from pprint import pprint
import os.path
API_URL = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?lang=en&region=gb&calendartype=blacklist&limit=100&dates={}&tz=Europe/London"

def games_played():

    for d in range(20171000, 20171032):

        url = requests.get(API_URL.format(d))
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

class NbaCrawler:
    """
    Crawling Espn.com for upcoming NBA fixtures.
    """
    def __init__(self, url, season_start=20171018, season_end=20180411):
        """
        Url is a string for the api url with date
        as a formated argument.
        e.g. "http://apiurl...dates={}&tz=Europe/London"
        """
        self.url = url
        self.data = {}
        self.season_start = season_start
        self.season_end = season_end

    def get_data_today(self):
        """
        Gets data from the url and formats todays date in to the string
        in the following format: "20171001"
        Saves the data from the url into the data attribute.
        """

        response = requests.get(self.url.format(datetime.date.today().strftime("%Y%m%d")))
        self.data = respone.json()

    def get_data_full_season_API(self):
        """
        Get the data from the api for a full season into self.data
        hint: use dict with date to store more than one days data
        """

        for d in range(self.season_start, self.season_end):
            response = requests.get(self.url.format(d))
            data = json.loads(response.content)
            self.data[d] = data

    def write_data_to_file(self):
        """
        Writes the json string to a file.
        """
        with open('NBA_full_season.json', 'w') as outfile:
            json.dump(self.data, outfile)

    def get_data_full_season(self):
        """
        Checks if the data is already stored in an existing json file and
        if it does, reads it.
        Else runs get_data_full_season_API and write_data_to_file.
        """
        self.json_file = "NBA_full_season.json"
        if os.path.isfile(self.json_file) == True:
            file.read(self.json_file)
        else:
            self.get_data_full_season_API()
            self.write_data_to_file()




def main():
    # DO STUFF
    nba_crawl = NbaCrawler(API_URL)
    nba_crawl.get_data_full_season()



if __name__ == '__main__':
    main()
