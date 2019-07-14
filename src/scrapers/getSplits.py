#!/usr/bin/env python3

"""
Library for Scraping Player hittings Splits
from baseball reference
"""

import sys
import pandas as pd
import pybaseball as pyb

YEAR = "2019" # default year if not provided by user
if len(sys.argv) > 1:
  PLAYER = sys.argv[1]
if len(sys.argv) > 2: 
  YEAR = sys.argv[2]

path="/Users/philiplassen/CS/StatFloor/data/player_data"


def getUrl(pid, year):
  """
  Generate Url (as a string to be scraped)
  for gamesplits
  """
  return "https://www.baseball-reference.com/players/split.fcgi?id=" + pid + "&year=" + year


def getSplits(last_name, first_name, year = "2019"):
  """
  Get GameSplits of player with given first name lastname
  for given year
  """
  pids = pyb.playerid_lookup(last_name, first_name)
  pid = pids["key_bbref"][0]
  url = getUrl(pid, year)
  dfs  = pd.read_html(url)
  return dfs
  




