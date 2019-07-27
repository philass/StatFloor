#!/bin/bash
#
# Takes a players Gamelogs from a given season and stores
# and stores the data in the data folder
#
#
#
# Usage
#________________________________________
#
# ./playerLogs.sh "first_name last_name" YEAR
# 
# Example
# 
# ./playerLogs.sh "mike trout" 2018
#
#________________________________________
echo $1
echo $2
if [ "$1" == "" ]
then
  echo "Missing Player Name"
  exit 1
elif [ "$2" == "" ]
then
  YEAR="2019"
else
  YEAR="$2"
fi

#Execute Python Webscrape
python3 getLogs.py $1 $YEAR



