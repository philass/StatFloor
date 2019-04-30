#!/usr/bin/env python3

"""
Library for Scraping Game Logs for MLB
players from baseball-reference
"""

import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

YEAR = "2017"
PLAYER = "mike trout"
if len(sys.argv) > 1:
  PLAYER = sys.argv[1]
if len(sys.argv) > 2: 
  YEAR = sys.argv[2]
print(PLAYER)
print(YEAR)
  
def getContent(array):
  """
  Formats the content of an Array based 
  on the result of the array 
  comprehension - [t.contents for t in tds]
  """
  result = []
  for a in array:
    if len(a) == 0:
      result += [None]
    elif type(a[0]) == str:
      result += a 
    else:
      result += [a[0].string]
  return result

# Column Names for the DataFrames and CSV

headers = ["Rk",	"Gcar",	"Gtm",	"Date",	"Tm",		"Opp",	"Rslt",	"Inngs",	
"PA",	"AB",	"R",	"H",	"2B",	"3B",	"HR",	"RBI",	"BB",	"IBB",	
"SO",	"HBP",	"SH",	"SF",	"ROE",	"GDP",	"SB",	"CS",	"BA",	"OBP",	
"SLG",	"OPS",	"BOP",	"aLI",	"WPA",	"RE24",	"DK",	"FD", "Pos"]

def generatePID(val):
  """
  Generate pid based on player
  IMPORTANT
  DOES NOT WORK FOR NON UNIQUE NAME
  """
  index = val.index(' ')
  return val[index + 1:index + 6] + val[0:2] + "01"
 
def getUrl(pid, year):
 """
 Generate URL (as a string) to be 
 scraped for gamelogs for a given pid and year
 """
 print(year)
 return "https://www.baseball-reference.com/players/gl.fcgi?id=" + pid + "&t=b&year=" + year


def getData(player_name, year = "2019", verbose = False):
  """Generates a CSV of the GameLogs of a given player
  for the specfified year. The CSV has 37 columns and
  the number of rows dpeend on the number of games that
  the player played in that year"""
  pid = generatePID(player_name)
  url = getUrl(pid, year)
  print(url)
  response = requests.get(url)
  if not response:
    print("Coud not find Webpage")
    return #Exit the program 
  soup = bs(response.content, 'html.parser')
  game_log_table = soup.findAll('table')[-1]
  game_log_rows = game_log_table.findAll('tr')
  data = []
  for tr in game_log_rows:
    tds = tr.findAll('td')
    results = [t.contents for t in tds] 
    res = getContent(results)
    if len(res) > 0:
      data += [res]
  df = pd.DataFrame(data, columns = headers)
  df.to_csv(pid + "-" + year + ".csv")


""" 
If Command Line Arguements were given run
Code snippit Below
"""

if len(sys.argv) > 1:
  getData(PLAYER, year = YEAR)

