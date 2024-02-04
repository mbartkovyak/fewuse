import gspread
import os

CREDENTIALS_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "credentials.json"
)

gc = gspread.service_account(filename=CREDENTIALS_PATH)

def write_to_sheet(data):
    sh = gc.open("LendLoop")
    worksheet = sh.sheet1
    for x in data:
        worksheet.append_row(x)

if __name__ == "__main__":
    data = write_to_sheet(['test','TS'])