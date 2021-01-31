from sys import exit
import utils
from config import GoogleSheetsConfig
from search import Craigslist
from sheets import Spreadsheet

config = GoogleSheetsConfig()
sheet = Spreadsheet(config.SPREADSHEET_NAME)
WORKSHEET_NAME = config.WORKSHEET_NAME


def search_craigslist(site, area, filters, sort_by=None, geotagged=None):
    craigslist = Craigslist()

    results = craigslist.search(site=site, area=area, filters=filters, sort_by=sort_by, geotagged=geotagged)

    return results

def get_current_results():
    """Retrieves the IDs of the current listings in the spreadsheet
    """
    values = sheet.read_column(WORKSHEET_NAME, 1)
    
    return values[1:] # do not include 'id'

def generate_sheet_data(search_results, prev_listing_ids):
    """Converts results dictionary to Google Sheets-formatted data
    Adds new listings and removes expired listings
    """
    columns = None
    sheet_data = []
    latest_listing_ids = []
    
    for result in search_results:
        if not columns and not prev_listing_ids: # only add columns if it is the first time running
            columns = list(result.keys())
            sheet_data.append(columns)
   
        if is_in_dc(result['url']):
            if is_in_neighborhood(result['where']) != True:
                if not result['id'] in prev_listing_ids: # remove duplicates

                        # convert geotag tuple to string
                        geotag_string = utils.tuple_to_string(result['geotag'])
                        result['geotag'] = geotag_string

                        row = list(result.values())
                        sheet_data.append(row)

                latest_listing_ids.append(result['id'])

    delete_expired_listings(latest_listing_ids, prev_listing_ids)

    return sheet_data

def is_in_dc(url):
    """Returns True if the listing is in Washington, D.C.
    """
    if "https://washingtondc.craigslist.org/doc/apa/d/washington" in url:
        return True

def is_in_neighborhood(where_col):
    """Returns True if the listing is in certain neighborhoods
    """
    if where_col:
        unwanted_neighborhoods = ['Petworth', 'Trinidad', 'Navy Yard', 'Mount Rainier', 'Van Ness', 'Anacostia'] # TODO: enhancement: NLP processing to standardize n-grams

        for neighborhood in unwanted_neighborhoods:
            if neighborhood in where_col:
                return True

def delete_expired_listings(latest_listing_ids, prev_listing_ids):
    """Deletes expired listings
    """
    for id in prev_listing_ids:
        if id not in latest_listing_ids:
            cell = sheet.find_cell(WORKSHEET_NAME, id)
            sheet.delete_rows(WORKSHEET_NAME, cell.row)

def main():

    # Define Craigslist search parameters
    site='washingtondc'
    area='doc'
    filters={
        'min_bedrooms': 2,
        'max_bedrooms': 2,
        'min_bathrooms': 2,
        'max_bathrooms': 2,
        'min_ft2': 900,
        'max_price': 2800,
        'laundry': 'w/d in unit',
        'parking': ['carport', 'attached garage', 'detached garage', 'off-street parking', 'street parking']
        }
    sort_by = "newest" # "price_asc", "price_desc"
    geotagged = True

    # Perform search
    results = search_craigslist(site, area, filters, sort_by, geotagged)

    # Filter and prepare final result set
    prev_listing_ids = get_current_results()

    sheet_data = generate_sheet_data(results, prev_listing_ids)

    # Append new results to spreadsheet
    response = sheet.append_rows(WORKSHEET_NAME, sheet_data, "RAW")
    print(response)


if __name__ == '__main__':
    exit(main())