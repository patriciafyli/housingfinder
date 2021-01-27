import gspread


class Spreadsheet:

    def __init__(self, name):
        """Class that represents a Google Sheet
        """
        self.name = name

    @property
    def gc(self):
        gc = gspread.oauth()

        return gc

    @property
    def spreadsheet(self):
        spreadsheet = self.gc.open(self.name)

        return spreadsheet

    def read_column(self, worksheet_name, index):
        """Reads data from a column inside a worksheet
        """
        worksheet = self.spreadsheet.worksheet(worksheet_name)
        values = worksheet.col_values(index)

        return values

    def append_rows(self, worksheet_name, values, value_input_option):
        """Appends rows to a worksheet
        """
        worksheet = self.spreadsheet.worksheet(worksheet_name)
        response = worksheet.append_rows(values, value_input_option)

        return response

    def delete_rows(self, worksheet_name, index):
        """Deletes a row in a worksheet
        """
        worksheet = self.spreadsheet.worksheet(worksheet_name)
        response = worksheet.delete_rows(index)

        return response

    def find_cell(self, worksheet_name, search_term):
        """Locates a cell in a worksheet
        """
        worksheet = self.spreadsheet.worksheet(worksheet_name)
        cell = worksheet.find(search_term)

        return cell


# DEPRECATED
# import logging
# import os.path
# import pickle
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from config import GoogleSheetsConfig

# logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)


# class GoogleSheets:

#     def __init__(self, config):
#         self._creds = None
#         self._token_pickle_file = config.TOKEN_PICKLE
#         self._client_secrets_file = config.CLIENT_SECRETS_FILE
#         self._scopes = config.SCOPES

#     @property
#     def sheets(self):
#         self._authenticate()
#         sheets = self._get_google_sheets_api()
        
#         return sheets

#     def read(self, spreadsheet_id, spreadsheet_range):
#         """Reads data from an existing sheet
#         """
#         result = self.sheets.values().get(spreadsheetId=spreadsheet_id,
#                                     range=spreadsheet_range).execute()
#         print(dict(result))
#         values = result.get('values', [])

#         return values

#     def append(self, spreadsheet_id, value_input_option, spreadsheet_range, body):
#         """Append rows to an existing sheet
#         """
#         print(f"Appending to Google Sheet {spreadsheet_id}...")

#         try:
#             response = self.sheets.values().append(spreadsheetId=spreadsheet_id,
#                                                 valueInputOption=value_input_option,
#                                                 range=spreadsheet_range,
#                                                 body=body).execute()
#             print("Successfully appended to Google Sheet")
#             return response
#         except Exception as e:
#             print(e)

#     def update(self, spreadsheet_id, value_input_option, spreadsheet_range, body):
#         """Updates data in an existing sheet
#         """
#         print(f"Updating Google Sheet {spreadsheet_id}...")

#         try:
#             response = self.sheets.values().update(spreadsheetId=spreadsheet_id,
#                                                 valueInputOption=value_input_option,
#                                                 range=spreadsheet_range,
#                                                 body=body).execute()
#             print("Successfully updated Google Sheet")
#             return response
#         except Exception as e:
#             print(e)

#     def _get_google_sheets_api(self):
#         """Creates an object representing the Google Sheets API
#         """
#         service = build('sheets', 'v4', credentials=self._creds)
#         sheets = service.spreadsheets()

#         return sheets

#     def _authenticate(self):
#         # The file token.pickle stores the user's access and refresh tokens, and is
#         # created automatically when the authorization flow completes for the first
#         # time.
#         if os.path.exists(self._token_pickle_file):
#             with open(self._token_pickle_file, 'rb') as token:
#                 creds = pickle.load(token)
#         else:
#             creds = self._generate_token_pickle()

#         self._creds = creds

#     def _generate_token_pickle(self):
#         """Creates a token.pickle to access Google Sheets
#         """
#         # If there are no (valid) credentials available, let the user log in.
#         if not self._creds or not self._creds.valid:
#             if self._creds and self._creds.expired and self._creds.refresh_token:
#                 self._creds.refresh(Request())
#             else:
#                 flow = InstalledAppFlow.from_client_secrets_file(
#                     self._client_secrets_file, self._scopes)
#                 creds = flow.run_local_server(port=0)

#             # Save the credentials for the next run
#             with open(self._token_pickle_file, 'wb') as token:
#                 pickle.dump(creds, token)

#         return creds