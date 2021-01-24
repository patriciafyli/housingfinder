from sys import exit
from config import GoogleSheetsConfig
from search import Craigslist
from sheets import GoogleSheets

sheets_config = GoogleSheetsConfig()
sheets = GoogleSheets(sheets_config)


def search_craigslist(site, area, filters, geotagged):
    craigslist = Craigslist()

    results = craigslist.search(site=site, area=area, filters=filters, geotagged=geotagged)
    # craigslist.print_results(results)

    return results

def get_current_results(spreadsheet_id, spreadsheet_range):
    """Retrieves the IDs of the current listings in the spreadsheet
    """
    values = sheets.read(spreadsheet_id, spreadsheet_range)
    ids = []

    if not values:
        print('No data found.')
    else:
        for row in values:
            ids.append(row[0])

    return ids[1:]

def generate_sheet_data(search_results, current_listing_ids):
    """Converts results dictionary to Google Sheets-formatted data
    """
    columns = None
    sheet_data = []
    
    for result in search_results:
        if not columns and not current_listing_ids: # only add columns if it is the first time running
            columns = list(result.keys())
            sheet_data.append(columns)
        
        if not result['id'] in current_listing_ids: # filter out current listing IDs
            row = list(result.values())
            sheet_data.append(row)

    return sheet_data

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

    # Search for listings
    results = search_craigslist(site, area, filters, geotagged)

    # Get current listing IDs in spreadsheet
    current_listing_ids = get_current_results(spreadsheet_id, spreadsheet_range)

    # Append new results to spreadsheet
    sheet_data = generate_sheet_data(results, current_listing_ids)
    body = dict(
        majorDimension='ROWS',
        values=sheet_data
    )

    response = sheets.append(spreadsheet_id, value_input_option, spreadsheet_range, body)
    print(response)


if __name__ == '__main__':
    exit(main())