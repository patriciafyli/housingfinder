import pytest
from unittest.mock import Mock, patch, PropertyMock
import gspread
from config import GoogleSheetsConfig
from sheets import Spreadsheet


SPREADSHEET_NAME = "Housing (Automated)"
WORKSHEET_NAME = "Test"

class TestGoogleSheets:

    @pytest.fixture
    def sheets(self):
        sheets = Spreadsheet(SPREADSHEET_NAME)

        sheets = Spreadsheet(SPREADSHEET_NAME)
        type(sheets).spreadsheet = PropertyMock(return_value=Mock(spec=gspread.Spreadsheet))

        return sheets

    def test_read_column(self, sheets):
        """Validate that column values can be read
        """
        column = 1
        sheets.read_column(WORKSHEET_NAME, column)

        sheets.spreadsheet.worksheet().col_values.assert_called_once()

    def test_append_rows(self, sheets):
        """Validate that rows can be appended to a worksheet
        """
        values = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        value_input_option = "RAW"

        sheets.append_rows(WORKSHEET_NAME, values, value_input_option)

        sheets.spreadsheet.worksheet().append_rows.assert_called_once()

    def test_find_cell(self, sheets):
        """Validate that a cell's location can be returned
        """
        sheets.find_cell(WORKSHEET_NAME, "1")

        sheets.spreadsheet.worksheet().find.assert_called_once()

    def test_delete_rows(self, sheets):
        """Validate that a row can be deleted
        """
        sheets.delete_rows(WORKSHEET_NAME, 1)

        sheets.spreadsheet.worksheet().delete_rows.assert_called_once()
