class GoogleSheetsConfig:

    def __init__(self):
        self.CLIENT_SECRETS_FILE = "/Users/pli/Documents/projects/housingfinder/credentials.json"
        self.TOKEN_PICKLE = "token.pickle"

        # Allows read/write access to the user's sheets and their properties.
        self.SCOPES = ["https://www.googleapis.com/auth/spreadsheets"] # If modifying these scopes, delete the file token.pickle.   