import pytest
from unittest import mock
from unittest.mock import patch, Mock
from craigslist import CraigslistHousing
from search import Craigslist


class TestCraigslist:

    @patch("search.Craigslist._build")
    def test_search(self, mock_build):
        """Test to validate that Craigslist can be searched
        """
        site = "site"
        area = "area"
        category = "category"
        filters = "filters"
        mock_housing = Mock(spec=CraigslistHousing)
        mock_build.return_value = mock_housing

        craigslist = Craigslist()
        craigslist.search(site, area, category, filters)

        mock_housing.get_results.assert_called_once()


    def test_search_default(self):
        """Test to validate that Craigslist can be searched with default category and filters
        """
        pass
