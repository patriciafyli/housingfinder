from sys import exit
from config import GoogleSheetsConfig
from search import Craigslist
from sheets import GoogleSheets

sheets_config = GoogleSheetsConfig()


def search_craigslist(site, area, filters, geotagged):
    craigslist = Craigslist()

    results = craigslist.search(site=site, area=area, filters=filters, geotagged=geotagged)
    # craigslist.print_results(results)

    return results

def get_sheet_data(raw_data):
    columns = None
    sheet_data = []
    
    for result in raw_data:
        if not columns:
            columns = list(result.keys())
            sheet_data.append(columns)
        
        row = list(result.values())
        sheet_data.append(row)

    return sheet_data

def write_to_gsheet(sheets_config, spreadsheet_id, value_input_option, spreadsheet_range, body):
    sheets = GoogleSheets(sheets_config)
    response = sheets.write(spreadsheet_id, value_input_option, spreadsheet_range, body)

    return response

def main():
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

    raw_data = search_craigslist(site, area, filters, geotagged)
    sheet_data = get_sheet_data(raw_data)

    spreadsheet_id = "1UfCp7ZucZ5RKJOVRBDQu7S-upFLIQGNXyxUsdavkFiQ" # Housing (Automated)
    value_input_option = "RAW"
    spreadsheet_range = "Housing-RAW"
    body = dict(
        majorDimension='ROWS',
        values=sheet_data
    )

    response = write_to_gsheet(sheets_config, spreadsheet_id, value_input_option, spreadsheet_range, body)
    print(response)


if __name__ == '__main__':
    exit(main())