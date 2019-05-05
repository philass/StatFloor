#!/usr/bin/env python3

"""
Library for Scraping Game Logs for MLB
players from baseball-reference
"""

import pandas as pd
import pybaseball as pyb




def getUrl(pid, year):
 """
 Generate URL (as a string) to be 
 scraped for gamelogs for a given pid and year
 """
 return "https://www.baseball-reference.com/players/gl.fcgi?id=" + pid + "&t=b&year=" + year

def getLogs(last_name, first_name, year = "2019"):
  """
  Get Gamelogs of player with first and last name from
  given year. If no year is given 2019 is assumed
  """
  # (To Do) Player Lookup takes very long may want to do this differently
  # (To Do) Also need to handle case for players with the same name
  # (To Do) Handle Empty DataFrame i.e player doesn't exist 
  pids = pyb.playerid_lookup(last_name, first_name)
  pid = pids["key_bbref"][0]
  url = getUrl(pid, year)
  return pd.read_html(url)[-1]

result = getLogs("trout", "mike") 
print(result)

