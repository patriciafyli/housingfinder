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
        spreadsheet_id = "1UfCp7ZucZ5RKJOVRBDQu7S-upFLIQGNXyxUsdavkFiQ" # Housing (Automated)
        spreadsheet_range = "Test"

        values = sheets.read(spreadsheet_id, spreadsheet_range)
        # TODO: use a mock client

    def test_append(self, sheets):
        """Validate that a sheet can be appended to
        """
        spreadsheet_id = "1UfCp7ZucZ5RKJOVRBDQu7S-upFLIQGNXyxUsdavkFiQ" # Housing (Automated)
        value_input_option = "RAW"
        spreadsheet_range = "Test"
        body = dict(
            majorDimension='ROWS',
            values=[[1, 2, 3], [1, 2, 3], [1, 2, 3]] # first list is columns
        )

        response = sheets.append(spreadsheet_id, value_input_option, spreadsheet_range, body)
        print(response)
        # TODO: use a mock client

    def test_update(self, sheets):
        """Validate that a sheet can be updated
        """
        spreadsheet_id = "1UfCp7ZucZ5RKJOVRBDQu7S-upFLIQGNXyxUsdavkFiQ" # Housing (Automated)
        value_input_option = "RAW"
        spreadsheet_range = "Test"
        body = dict(
            majorDimension='ROWS',
            values=[[1, 2, 3], [1, 2, 3], [1, 2, 3]] # first list is columns
        )

        response = sheets.update(spreadsheet_id, value_input_option, spreadsheet_range, body)
        print(response)
        # TODO: use a mock client