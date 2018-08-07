# google drive: testing/b foods
# https://goo.gl/forms/2409gkrTdbi82Ukx2

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

from config import SECRETS_FILE_PATH, GOOGLE_DRIVE_AUTH_SCOPE

def extract_google_sheets():
    # Authenticate using the signed key
    credentials = ServiceAccountCredentials.from_json_keyfile_name(SECRETS_FILE_PATH, GOOGLE_DRIVE_AUTH_SCOPE)  # http://gspread.readthedocs.io/en/latest/oauth2.html

    gc = gspread.authorize(credentials)

    for spreadsheet in gc.openall():  # iterates through every spreadsheet shared with the service account email
        worksheet = spreadsheet.sheet1

        df = pd.DataFrame(worksheet.get_all_records())
        print(df)
    