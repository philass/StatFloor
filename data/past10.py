#!/usr/bin/env python3
"""
Library for getting previous 10 games for Batters
"""

import pandas as pd
import pybaseball as pyb


def get_names_stats(last_name, first_name):
  """
  Get Batting numbers for the last 10 games player with 
  given first_name and last_name. Returns a PD DataFrame
  """
  # (To Do) Player Lookup takes very long may want to do this differently
  # (To Do) Also need to handle case for players with the same name
  # (To Do) Handle Empty DataFrame i.e player doesn't exist 
  pids = pyb.playerid_lookup(last_name, first_name)
  pid = pids["key_mlbam"][0]
  hit_logs = pyb.statcast_batter("2019-01-01", "2019-12-12", pid)
 


