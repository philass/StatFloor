# Code for getting Player IDs from Baseball Reference
# Lots of this code is taken from pybaseball at the url
# https://github.com/jldbc/pybaseball/blob/master/pybaseball/playerid_lookup.py
#
import pandas as pd
import io
import requests

file_location = "../../data/ids/pids.csv"

def get_lookup_table():
    print('Gathering player lookup table. This may take a moment.')
    url = "https://raw.githubusercontent.com/chadwickbureau/register/master/data/people.csv"
    #s=requests.get(url).content
    #print(type(s))
    #table = pd.read_csv(io.StringIO(s.decode('utf-8')), dtype={'key_sr_nfl': object, 'key_sr_nba': object, 'key_sr_nhl': object})
    table = pd.read_csv(file_location, dtype={'key_sr_nfl': object, 'key_sr_nba': object, 'key_sr_nhl': object})
    cols_to_keep = ['name_last','name_first','key_mlbam', 'key_retro', 'key_bbref', 'key_fangraphs', 'mlb_played_first','mlb_played_last']
    table = table[cols_to_keep]
    #make these lowercase to avoid capitalization mistakes when searching
    table['name_last'] = table['name_last'].str.lower()
    table['name_first'] = table['name_first'].str.lower()
    # Pandas cannot handle NaNs in integer columns. We need IDs to be ints for successful queries in statcast, etc.
    # Workaround: replace ID NaNs with -1, then convert columns to integers. User will have to understand that -1 is not a valid ID.
    table[['key_mlbam', 'key_fangraphs']] = table[['key_mlbam', 'key_fangraphs']].fillna(-1)
    table[['key_mlbam', 'key_fangraphs']] = table[['key_mlbam', 'key_fangraphs']].astype(int) # originally returned as floats which is wrong
    return table



def playerid_lookup(last, first=None):
    # force input strings to lowercase
    last = last.lower()
    if first:
        first = first.lower()
    table = get_lookup_table()
    if first is None:
        results = table.loc[table['name_last']==last]
    else:
        results = table.loc[(table['name_last']==last) & (table['name_first']==first)]
    results = results.reset_index().drop('index', 1)
    result = results.at[0, "key_bbref"]
    return result


