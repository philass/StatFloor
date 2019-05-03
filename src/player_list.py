#!/usr/bin/env python3

"""
Generate a list of Active Player Names and the respective Player IDs
"""


import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def getAllLetterPlayers(l):
  url = "https://www.baseball-reference.com/players/" + l + "/"
  response = requests.get(url)
  if not response:
    print("Could not find webpage")
    return #Exit function
  soup = bs(response.content, 'html.parser')
  players = soup.findAll('strong')
  print(players)
  return [(p1.find('a').text, p1.find('a').attrs['href'][11:-6]) for p1 in players 
                                                          if p1.find('a') != None]
    

def getAllPlayers():
  alphabet = "bcdefghijklmnopqrstuvwxyz"
  players = []
  for letter in alphabet:
    print(letter)
    ps = getAllLetterPlayers(letter)
    print(ps)
    players += ps
  print(players)
  return players

getAllPlayers()
    
  


