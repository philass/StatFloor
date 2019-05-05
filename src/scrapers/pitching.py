#!/usr/bin/env python3

"""
Library for Scraping Game Logs for MLB
players from baseball-reference
"""

import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

