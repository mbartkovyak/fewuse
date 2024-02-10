"""Module for interacting with Google Sheets via gspread."""
import os
import gspread

CREDENTIALS_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "credentials.json"
)

gc = gspread.service_account(filename=CREDENTIALS_PATH)

def write_to_sheet(data):
    """
    Appends each list in `data` as a new row to the first worksheet of the "LendLoop" Google Sheet.

    Args:
        data (list of list): Data rows to append.
    """
    sh = gc.open("LendLoop")
    worksheet = sh.sheet1
    for x in data:
        worksheet.append_row(x)

if __name__ == "__main__":
    # Ensure data is a list of lists, even if there's only one row to append.
    data = [['test', 'TS']]
    write_to_sheet(data)
