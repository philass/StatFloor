"""
Class for a player. Encapsulates Retrieving there data, from
baseball reference.


------------
Example Usage

------------
player1 = Batter("mike", "trout")
table = player1.get_logs(2018)
print(table)
------------
"""
from os import path
import os
from os import system
import pandas as pd
from pids import playerid_lookup


class Batter:
    """
    Class for representing a baseball batter -
    interfaces with baseball reference to get data
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.bref_id = playerid_lookup(last_name, first_name)

    def get_logs(self, year=2019):
        """
        Get game Logs from start date to end Date

        """
        data_path = "../../data/player_data/"
        directory = data_path + self.bref_id + "/" + str(year)
        filtered_logs = directory + "/filtered_logs.csv"
        raw_logs = directory + "/gameLogs.csv"
        if not path.exists(filtered_logs):
            url = self.get_url(year)
            raw_df = pd.read_html(url)[-1]
            data_frame = raw_df[raw_df.Pos.notnull()]
            if data_frame.empty:
                print("Could not get Data")
            else:
                print("Saving result to....")
                try:
                    os.mkdir(data_path + "/" + self.bref_id)
                except:  # pylint: disable=W0702
                    print("Player folder exists")
                try:
                    os.mkdir(data_path + "/" + self.bref_id + "/" + str(year))
                except:  # pylint: disable=W0702
                    print("Player year folder exsits")
                # replace file
                data_frame.to_csv(raw_logs, index=False)
                print(raw_logs)
                os.chdir("../scrapers/")
                command = ("./playerLogs.sh " + self.first_name + " " +
                           self.last_name + " " + str(year))  # Execute cleaning script
                system(command)
                system("ls")
                os.chdir("../player")
        return pd.read_csv(filtered_logs)

    def get_url(self, year=2019):
        """
        Generate URL (as a string) to be
        scraped for gamelogs for a given pid and year
        """
        return "https://www.baseball-reference.com/players/gl.fcgi?id=" \
            + self.bref_id + "&t=b&year=" + str(year)
