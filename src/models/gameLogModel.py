#!/usr/bin/env python3
"""
Trains a prediction Model based on Players
previous 10 game logs as training data
"""
from datetime import date
import pandas as pd
path = "/Users/philiplassen/CS/StatFloor/data/player_data"
pid = "troutmi01"
year = "2017"
start_date = date(int(year), 3, 1)
import numpy as np

def get_table(pid, year):
  df = pd.read_csv(path + "/" + pid + "/" + year + "/gameLogs.csv")
  del df['DFS(DK)']
  del df['DFS(FD)']
  del df['Pos']
  del df['Inngs']
  del df['Rslt']
  change = (df.columns[5])
  df.rename({change  : "Away"}, axis = 'columns', inplace = True)
  return df

def date_to_int(date1):
  """
  Takes a date of a certain string format
  and returns the date from an absolute Date
  declared in the global start date
  """
  res = date1.split()
  month = month_to_int(res[0])
  day = int(res[1])
  result_date = date(int(year), month, day)
  return (result_date - start_date).days




def month_to_int(month):
  """
  Takes a a 3 letter str for month and prints the
  corresponding integer
  """
  month = month.lower()
  months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
  return months.index(month) + 1

def away_filter(val):
  """
  Converts h/a respresentation to integer
  """
  return 1 if val == '@' else 0
  

result = get_table(pid, year)
result["Date"] = result["Date"].apply(date_to_int)
result["Away"] = result["Away"].apply(away_filter)
print(result)
# (To Do) Clean DataFrame i.e Strings -> Numbers, NAN -> Numbers, Remove -> Columns

# (To Do) Chunk into Training and Test 10 i.e list of matrices of consecutive 10 Games

def chunk(table, frame_size = 10):
  np_data = table.to_numpy()
  depth = np_data.shape[0] - frame_size + 1 
  chunked = np.zeros((frame_size, np_data.shape[1], depth))
  for i in range(depth):
    chunked[:, :, i] = np_data[i:i + frame_size, :]
  return chunked

chunks = chunk(result)
print(chunks)
print(chunks.shape)


# (To Do) Train a model i.e Regression

# (To Do) Cross validation i.e Accuracy of the Model



