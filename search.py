from craigslist import CraigslistHousing

# CraigslistHousing.show_filters()


class Craigslist:

    def search(self, site, area, category=None, filters=None, sort_by=None, geotagged=None):
        """Performs a Craigslist search
        """
        housing = self._build(site, area, category, filters)
        results = housing.get_results(sort_by=sort_by, geotagged=geotagged)

        return results

    def _build(self, site, area, category=None, filters=None):
        """Builds the housing object
        """
        housing = CraigslistHousing(
            site=site,
            area=area,
            category=category,
            filters=filters
        )

        return housing

    def print_results(self, results):
        """Prints results from Craigslist search
        """
        for result in results:
            print(result)
