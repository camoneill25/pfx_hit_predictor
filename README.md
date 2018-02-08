# Baseball Hit Predictor/Analysis

Baseball is a game built on statistics, one of the most fundamental parts of baseball is hitting, it is also one of the most complex. Can we use Pitch F/x technology to help predict a hit?

## Getting Started

The project primarily involves Python 3 for web-scraping, model construction, and feature selection/analysis. PSQL (or any SQL DB) for data storage. Make sure you have them installed on your machine before running the first set of scripts, which will place data into a SQL DB. Recommend looking at brooksbaseball.net to understand data structure and source.

The entirety of this project was completed on macOS, I have not, nor doI have plans for a Windows machine test.

### Prerequisites
* Python 3.7 or later
* Working knowledge of baseball
* PSQL or any SQL DB
* NOTE:You should know what BB_per_9 and pitcher xfip means to understand all statistical features within data set.

### Installing

Python 3.7 or later must be installed.
  Installtion instructions here: https://www.python.org/downloads/

SQL DB on your local machine must be installed.
  Installation instructions here: http://postgresguide.com/setup/install.html

Anaconda or a package with numpy, pandas, and sklearn
  Installation guide here: https://conda.io/docs/user-guide/install/index.html
  
Download: cleaned_player_id.csv | batter_stats_table.csv | pitcher_stats_table.csv | schedule_table.csv
* On GitHub Repo 
'''
Make sure these are all csv UTF-8 in format
'''


## Running the tests

Run Scripts in this order:
* pfx_data_collections.py 
* pfx_webscrapper.py
* NOTE: The script will take rouhgly 24 to 48 hours running to collect all the data and will be placed in the SQL table outlined in the create table script


## Built With

* [sqlalchemy](https://www.sqlalchemy.org) - SQL Management
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - XML
* [psycopg2](http://initd.org/psycopg/) - Python SQL control

## Contributing

Special thanks to Alex Felker at Affirma Consulting for all the help!


## Versioning
Currently Version 1.0


## Authors

* **Cameron O'Neill** - *Initial work* - [camoneill25](https://github.com/camoneill25)


## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks for all the help Jack, Matt and Miles!
* MLB Advanced Media
* Brooks Baseball Network
