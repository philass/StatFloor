#!/bin/bash

# Take the relevant team abbreviations from file with historical
# team names. Credit Soren Lassen with the solution.

awk '{if($NF=="Present"){print $2}}' < all_teams.txt > teams.txt
