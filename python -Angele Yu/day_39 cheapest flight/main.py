import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("./creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("python test").sheet1  # Open the spreadhseet
# sheet = client.open_by_url(
#     'https://docs.google.com/spreadsheets/d/1C562zarWY2U5Q8IVcP9mm9ZsvOAJ5McuywrVx4U6SwY').sheet1

# Get a list of all records
# print(data)
row = sheet.row_values(1)  # Get a specific row
# print(row)
col = sheet.col_values(1)  # Get a specific column
# print(col)
# cell = sheet.cell(1, 2).value  # Get the value of a specific cell
# print(cell)

# insertRow = ["hello", "5", "red", "blue"]
# sheet.add_rows(insertRow,4)  # Insert the list as a row at index 4
# sheet.update_cell(7, 1, "NEW ONE ADDED")
# sheet.update_cell(7, 2, "NEW ONE ADDED")
# sheet.update_cell(7, 3, "NEW ONE ADDED")
data = sheet.get_all_records()
# print(data)
# sheet.update_cell(2, 2, "CHANGED")  # Update one cell

# numRows = sheet.row_count  # Get the number of rows in the sheet
# print(numRows)
