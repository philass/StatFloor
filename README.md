# StatFloor


This project aims to make accurate predictions of player performances and use these predictions to select lineups on the popular fantasy sport sights lineups

  - Data Retrieval
  - Statistical Modelling
  - Betting Strategey

## Software 

This project is primarilty devoloped with Python 3, and uses a few popular Python libraries.

### Prerequisites

The project uses the libraries: requests, bs4, and pandas. They can be installed with pip

```
pip3 install pandas bs4 requests
```

### Installing

The project can be installed by simply cloning the repository
```
git clone https://github.com/philiplassen/StatFloor.git
```


### Running

We can run the data Webscrape with the following command as an example.
```
python3 src/player_scrape.py "mike trout" 2018
``` 
This stores Mike Trout's gamelogs from 2018 in a csv

