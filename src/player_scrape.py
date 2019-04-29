#!/usr/bin/env python3

"""
Usage 

python3 player_scrape PID

Output 

PID.csv

"""


import sys
import requests

pid = sys.argv[1]
pid = "troutmi01"
response = requests.get("https://www.baseball-reference.com/players/gl.fcgi?id=" + pid + "&t=b&year=2019")
print(response)
print(type(response))






