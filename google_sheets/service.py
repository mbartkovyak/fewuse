import gspread

gc = gspread.service_account(filename='credentials.json')

def write_to_sheet(data):
    sh = gc.open("LendLoop")
    worksheet = sh.sheet1
    worksheet.append_row(data)