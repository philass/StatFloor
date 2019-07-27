#!/usr/bin/env python3

"""
Library for Scraping Player hittings Splits
from baseball reference
"""

import urllib.request
import sys
import pandas as pd
import pybaseball as pyb
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep

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
  url = "https://www.baseball-reference.com/players/split.fcgi?id=" + pid + "&year=" + year
  print(url)
  return url 


def get_rendered_html(url):
  """
  Gets html rendered after
  5 seconds of loading using a webdriver
  and returns the raw html as as string
  """
  driver = webdriver.Firefox(executable_path="/Users/philiplassen/CS/drivers/geckodriver")
  driver.get(url)
  sleep(5)
  html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
  driver.quit()
  return html


def getSplits(last_name, first_name, year = "2019"):
  """
  Get GameSplits of player with given first name lastname
  for given year
  """
  pids = pyb.playerid_lookup(last_name, first_name)
  pid = pids["key_bbref"][0]
  url = getUrl(pid, year)
  raw_html = get_rendered_html(url)
  tables = pd.read_html(raw_html)
  print(tables)
  print(type(tables))
  print(len(tables))
  return tables

splits = getSplits("trout", "mike")

