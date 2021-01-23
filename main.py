from sys import exit
from search import Craigslist


def main():
    craigslist = Craigslist()

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

    results = craigslist.search(site=site, area=area, filters=filters)
    craigslist.print_results(results)


if __name__ == '__main__':
    exit(main())