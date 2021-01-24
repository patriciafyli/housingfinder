import pytest
from unittest.mock import Mock, patch
from config import GoogleSheetsConfig
from sheets import GoogleSheets


class TestGoogleSheets:

    @pytest.fixture
    def sheets(self):
        config = GoogleSheetsConfig()
        sheets = GoogleSheets(config)

        return sheets

    def test_read(self, sheets):
        """Validate that a sheet can be read
        """
        spreadsheet_id = "1UfCp7ZucZ5RKJOVRBDQu7S-upFLIQGNXyxUsdavkFiQ" # HousingTest
        spreadsheet_range = "Test"

        sheets.read(spreadsheet_id, spreadsheet_range)
        # TODO: use a mock client

    def test_write(self, sheets):
        """Validate that a sheet can be written to
        """
        spreadsheet_id = "1UfCp7ZucZ5RKJOVRBDQu7S-upFLIQGNXyxUsdavkFiQ" # HousingTest
        value_input_option = "RAW"
        spreadsheet_range = "Test"
        body = dict(
            majorDimension='ROWS',
            values=[[1, 2, 3], [1, 2, 3], [1, 2, 3]] # first list is columns
        )

        response = sheets.write(spreadsheet_id, value_input_option, spreadsheet_range, body)
        print(response)
        # TODO: use a mock client