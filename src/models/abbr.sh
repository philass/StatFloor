#!/bin/bash


awk '{if($NF=="Present"){print $2}}' < all_teams.txt > teams.txt
