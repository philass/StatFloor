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
if [ "$1" == "" ]
then
  echo "Missing Player First Name"
  exit 1
elif [ "$2" == "" ]
then
  echo "Missing Player Last Name"
  exit 1
elif [ "$3" == "" ]
then
  YEAR="2019"
else
  YEAR="$3"
fi

#Execute Python Webscrape
FILE_LOCATION="$(python3 getLogs.py $1 $2 $YEAR | tail -n 1)"
echo "$FILE_LOCATION"
DIR=$(dirname "${FILE_LOCATION}")
NEW_FILE=$DIR/filtered_logs.csv
head -n 1 "$FILE_LOCATION" > "$NEW_FILE"
grep '^[0-9]' "$FILE_LOCATION" >> "$NEW_FILE"

