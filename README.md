This is a personal project created to aid with apartment hunting. This program searches the housing section of Craigslist and appends results to a Google Sheets spreadsheet.

A *spreadsheet* refers to a Google Sheets workbook/spreadsheet.
A *worksheet* refers to a sheet/worksheet within the spreadsheet.

# How to Run

First, set up a virtual environment and install from `requirements/requirements.txt` and/or `requirements/test.txt` (if you would like to run the unit tests).

This program requires OAuth credentials to access a Google Drive account. Instructions for enabling access can be found [here](https://developers.google.com/sheets/api/quickstart/python#step_1_turn_on_the).

`gspread` requires the OAuth credentials to be saved to `~/.config/gspread/credentials.json`.

Activate the virtual environment and run the program:

> python main.py

## Libraries Used

- [python-craigslist](https://github.com/juliomalegria/python-craigslist) - Search and retrieve results from Craigslist
- [gspread](https://gspread.readthedocs.io/en/latest/) - Upload new results to Google Sheets and delete expired results
- [google-api-python-client, google-auth-httplib2, google-auth-oauthlib](https://developers.google.com/sheets/api/quickstart/python) - Authenticate with Google API

# System

- Macbook Pro 15
- macOS Catalina 10.15.7
- 16 GB 2400 MHz DDR4
- 2.2 GHz 6-Core Intel Core i7

# Process

1. A Craigslist search is performed based on specified criteria/filters (geotags included)
2. Results are cleaned to ensure successful write to Google Sheets
3. Previous search results are obtained from the target worksheet (if any). Duplicates are filtered out from the latest search results
4. Results are further filtered to improve personal relevancy
5. Previous search results, if they do not also appear in the latest search results, are deleted from the worksheet (remove expired results)
6. Latest search results are written to the worksheet

# Testing

Unit tests are written for pytest. They are not independent and require the `credentials.json` file to be set up as specified above.

Tests can be run with the following command from the root folder:

> pytest -s

# Deployment

The program was scheduled to run as a [crontab job](https://gavinwiener.medium.com/how-to-schedule-a-python-script-cron-job-dea6cbf69f4e); scheduling details can be found under the `deployment` folder.

Found instructions for troubleshooting on Mac [here](https://blog.bejarano.io/fixing-cron-jobs-in-mojave/).
