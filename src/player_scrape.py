#!/usr/bin/env python3

"""
Usage 

python3 player_scrape PID

Output 

PID.csv

"""

import sys
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def log(message):
  if '-v' in sys.argv:
    print(message)

pid = sys.argv[1]
pid = "troutmi01"



response = requests.get("https://www.baseball-reference.com/players/gl.fcgi?id=" + pid + "&t=b&year=2018")


if not response:
  print("Coud not find Webpage")
  sys.exit() # Exit the Program

# ------- Proccessing Web Page ---------
log("Web Page Found")
log(response.text)
soup = bs(response.content, 'html.parser')
game_log_table = soup.findAll('table')[-1]
game_log_rows = game_log_table.findAll('tr')
count = 0

"""
def getContent(contents):
  if contents == []:
    return None
  else if contents:
"""

def getContent(array):
  result = []
  for a in array:
    if len(a) == 0:
      result += [None]
    elif type(a[0]) == str:
      #print("yo this worked")
      result += a 
    else:
      #print(a[0])
      result += [a[0].string]
  return result

data = []
for tr in game_log_rows:
  tds = tr.findAll('td')
  results = [t.contents for t in tds] 
  res = getContent(results)
  
  if len(res) > 0:
    data += [res] 



headers = ["Rk",	"Gcar",	"Gtm",	"Date",	"Tm",		"Opp",	"Rslt",	"Inngs",	
"PA",	"AB",	"R",	"H",	"2B",	"3B",	"HR",	"RBI",	"BB",	"IBB",	
"SO",	"HBP",	"SH",	"SF",	"ROE",	"GDP",	"SB",	"CS",	"BA",	"OBP",	
"SLG",	"OPS",	"BOP",	"aLI",	"WPA",	"RE24",	"DK",	"FD", "Pos"]
df = pd.DataFrame(data, columns = headers)
print(df)
