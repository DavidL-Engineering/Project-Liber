import gspread
"""
Warning: This script assumes you have set up the Google Drive and Google Sheets API.
It will not work if you do not have these set up, along with the OAuth2 credentials stored on your computer.

HOW TO USE THIS SCRIPT:
1. Enter the row number of the title line for the set of data under Title_Line
2. Enter the simulation numbers corresponding to the exported simulation data under sim_numbers.
e.g. cp0.txt, drag0.txt, lift0.txt all correspond to Sim 1.

3. Enter the EXACT title of the spreadsheet under s_sheet_title.
4. Enter the EXACT title of the worksheet under which the data will be entered under w_sheet_title.
5. Enter the number of results you wish to export under num_results
6. Save the edited script in the same directory where ALL the results are located
7. Go ahead and run the script
"""

Title_Line = 32
sim_numbers = [15,16,17,18]
num_results = 4

s_sheet_title = "Google API Test"
w_sheet_title = "DOE Summary Results"

gc = gspread.oauth()

spreadsheet = gc.open("{}".format(s_sheet_title))
w_sheet = spreadsheet.worksheet("{}".format(w_sheet_title))

for i in range(num_results):
    cop_file = open("cp{}.txt".format(i), 'r')
    drag_file = open("drag{}.txt".format(i), 'r')
    lift_file = open("lift{}.txt".format(i), 'r')

    cop_all_data = cop_file.readlines()
    drag_all_data = drag_file.readlines()
    lift_all_data = lift_file.readlines()

    # cop values are on line 4
    # drag values are on line 12
    # lift values are on line 12

    cop_line_data = cop_all_data[4].split()
    drag_line_data = drag_all_data[12].split()
    lift_line_data = lift_all_data[12].split()

    cop_values = str(cop_line_data[1]) + " " + str(cop_line_data[2])
    drag_comp_values = str(drag_line_data[1]) + " " + str(drag_line_data[2])
    drag_tot_value = str(drag_line_data[3])
    lift_comp_values = str(lift_line_data[1] + " " + lift_line_data[2])
    lift_tot_value = str(lift_line_data[3])

    cop_col = w_sheet.find("Center of Pressure (x=0 [m])", in_row = Title_Line).col
    drag_tot_col = w_sheet.find("A. Drag [N] (Total)", in_row = Title_Line).col
    drag_comp_col = w_sheet.find("B. Drag : Pressure +Viscous", in_row = Title_Line).col
    lift_tot_col = w_sheet.find("A. Lift [N] (Total)", in_row = Title_Line).col
    lift_comp_col = w_sheet.find("B. Lift [N] (Pressure + Viscous)", in_row = Title_Line).col

    sim_row_match = w_sheet.findall("{}".format(sim_numbers[i]), in_column=1)
    if len(sim_row_match) > 0:
        j = 0
        while sim_row_match[j].row < Title_Line:
            j+=1
    else:
        print("Script failed. Could not find matching row for simulation data.")
        input("Press enter to continue...")
    
    sim_row = sim_row_match[j].row

    w_sheet.update_cell(sim_row, cop_col, cop_values)
    w_sheet.update_cell(sim_row, drag_tot_col, drag_tot_value)
    w_sheet.update_cell(sim_row, drag_comp_col, drag_comp_values)
    w_sheet.update_cell(sim_row, lift_tot_col, lift_tot_value)
    w_sheet.update_cell(sim_row, lift_comp_col, lift_comp_values)

    cop_file.close
    drag_file.close
    lift_file.close