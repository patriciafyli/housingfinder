from sys import exit
from search import Craigslist
from sheets import Spreadsheet

SPREADSHEET_NAME = "Housing (Automated)"
WORKSHEET_NAME = "Housing-RAW"
sheet = Spreadsheet(SPREADSHEET_NAME)


def search_craigslist(site, area, filters, geotagged):
    craigslist = Craigslist()

    results = craigslist.search(site=site, area=area, filters=filters, geotagged=geotagged)
    # craigslist.print_results(results)

    return results

def get_current_results(spreadsheet_id, spreadsheet_range):
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
        
        if not result['id'] in prev_listing_ids: # remove duplicates
            row = list(result.values())
            sheet_data.append(row)

        latest_listing_ids.append(result['id'])

    delete_expired_listings(latest_listing_ids, prev_listing_ids)

    return sheet_data

def delete_expired_listings(latest_listing_ids, prev_listing_ids):
    """Deletes expired listings
    """
    for id in prev_listing_ids:
        if id not in latest_listing_ids:
            cell = sheet.find_cell(WORKSHEET_NAME, id)
            sheet.delete_row(WORKSHEET_NAME, cell.row)

def main():

    # Define Craigslist search parameters
    site='washingtondc'
    area='doc'
    filters={
        'min_bedrooms': 2,
        'max_bedrooms': 2,
        'min_bathrooms': 2,
        'max_bathrooms': 2,
        'max_price': 2800,
        'laundry': 'w/d in unit',
        'parking': ['carport', 'attached garage', 'detached garage', 'off-street parking', 'street parking']
        }
    geotagged = False # TODO: enhancement: make the geotagging work with Sheets

    # Define target spreadsheet metadata
    spreadsheet_id = "1UfCp7ZucZ5RKJOVRBDQu7S-upFLIQGNXyxUsdavkFiQ" # Housing (Automated)
    spreadsheet_range = "Housing-RAW"
    value_input_option = "RAW"

    # Generate results
    results = search_craigslist(site, area, filters, geotagged)
    prev_listing_ids = get_current_results(spreadsheet_id, spreadsheet_range)

    sheet_data = generate_sheet_data(results, prev_listing_ids)

    # Append new results to spreadsheet
    response = sheet.append_rows(WORKSHEET_NAME, sheet_data, value_input_option)
    print(response)


if __name__ == '__main__':
    exit(main())