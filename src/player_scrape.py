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
from bs4 import BeautifulSoup as bs

def log(message):
  if '-v' in sys.argv:
    print(message)

pid = sys.argv[1]
pid = "troutmi01"



response = requests.get("https://www.baseball-reference.com/players/gl.fcgi?id=" + pid + "&t=b&year=2018")


if not response:
  print("Found Web Page")
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

for tr in game_log_rows:
  count = count + 1
  tds = tr.findAll('td')
  results = [t.contents for t in tds] 
  res = getContent(results)
  print(res)
  print("")
      




