import gspread
from pprint import pprint

Title_Line = 32
sim_numbers = [15,16,17,18]

s_sheet_title = "Google API Test"
w_sheet_title = "DOE Summary Results"

gc = gspread.oauth()

spreadsheet = gc.open("{}".format(s_sheet_title))
w_sheet = spreadsheet.worksheet("{}".format(w_sheet_title))

sim_row = w_sheet.findall("15", in_column=1)
for i in sim_row:
    print("row = " + str(i.row))
    print("col = " + str(i.col))

