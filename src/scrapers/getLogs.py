#!/usr/bin/env python3

"""
Library for Scraping Game Logs for MLB
players from baseball-reference
"""
import sys
import pandas as pd
import pybaseball as pyb
import os


#YEAR = "2019" # default year if not provided by user
if len(sys.argv) > 1:
  FIRST_NAME = sys.argv[1]
if len(sys.argv) > 2: 
  LAST_NAME = sys.argv[2]
if len(sys.argv) > 3: 
  YEAR = sys.argv[3]

headers = ["Rk",	"Gcar",	"Gtm",	"Date",	"Tm",		"Opp",	"Rslt",	"Inngs",	
"PA",	"AB",	"R",	"H",	"2B",	"3B",	"HR",	"RBI",	"BB",	"IBB",	
"SO",	"HBP",	"SH",	"SF",	"ROE",	"GDP",	"SB",	"CS",	"BA",	"OBP",	
"SLG",	"OPS",	"BOP",	"aLI",	"WPA",	"RE24",	"DK",	"FD", "Pos"]


path="/Users/philiplassen/CS/StatFloor/data/player_data"

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
  raw_df =  pd.read_html(url)[-1]
  df = raw_df[raw_df.Pos.notnull()]
  if df.empty:
    print("Could not get Data")
  else:
    print("Saving result to....")
    try:
      os.mkdir(path + "/" + pid)
    except:
      print("Player folder exists")
    try:
      os.mkdir(path + "/" + pid + "/" + year)
    except:
      print("Player year folder exsits")
    #replace file 
    path_of_buf = path + "/" + pid + "/" + year +  "/gameLogs.csv"
    df.to_csv(path_of_buf, index = False)
    print(path_of_buf)
  return df


  
  

""" 
If Command Line Arguements were given run
Code snippit Below
"""

if len(sys.argv) > 3:
  res = (getLogs(LAST_NAME, FIRST_NAME, year = YEAR))



