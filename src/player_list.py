#!/usr/bin/env python3

"""
Generate a list of Active Player Names and the respective Player IDs
and store them in a CSV file
"""


import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def getAllLetterPlayers(l):
  """
  Get all Player names starting with l and corresponding
  Reference ID's from Baseball reference as an array
  """
  url = "https://www.baseball-reference.com/players/" + l + "/"
  response = requests.get(url)
  if not response:
    print("Could not find webpage")
    return #Exit function
  soup = bs(response.content, 'html.parser')
  players = soup.findAll('strong')
  return [(p1.find('a').text, p1.find('a').attrs['href'][11:-6]) for p1 in players 
                                                          if p1.find('a') != None]
    

def getAllPlayers():
  """
  Generate A CSV of all active players from Baseball Reference
  """
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  players = []
  for letter in alphabet:
    ps = getAllLetterPlayers(letter)
    players += ps
  df = pd.DataFrame(players, columns = ["Name", "PID"])
  df.to_csv("data/pids.csv")
  return players



getAllPlayers()
    
  


