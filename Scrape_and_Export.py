import gspread
import os
"""
Warning: This script assumes you have set up the Google Drive and Google Sheets API.
It will not work if you do not have these set up, along with the OAuth2 credentials stored on your computer.

HOW TO USE THIS SCRIPT:
1. Enter the directory of the folder containing the data saved as text files under results_directory, ensuring all backslashes are changed to forward slashes.
e.g. C:/Users/david/Documents/1_(SSD)_Important_Things/Work/Project Liber
2. Enter the row number of the title line for the set of data under title_line
3. Enter the simulation numbers corresponding to the exported simulation data under sim_numbers.
e.g. sim_numbers = [15,16,17,18] 
Where cp0.txt, drag0.txt, lift0.txt all correspond to Sim 1.

4. Enter the EXACT title of the spreadsheet under s_sheet_title.
5. Enter the EXACT title of the worksheet under which the data will be entered under w_sheet_title.
6. Enter the number of results you wish to export under num_results
7. Save the edited script in the same directory where ALL the results are located
8. Go ahead and run the script
"""
results_directory = "C:/Users/david/Documents/1_(SSD)_Important_Things/Work/Project Liber"
title_line = 32
sim_numbers = [15,16,17,18]
num_results = 4

s_sheet_title = "Google API Test"
w_sheet_title = "DOE Summary Results"

gc = gspread.oauth()

spreadsheet = gc.open("{}".format(s_sheet_title))
w_sheet = spreadsheet.worksheet("{}".format(w_sheet_title))
print(os.getcwd())

for i in range(num_results):
    cop_file = open("{}/cp{}.txt".format(results_directory, i), 'r')
    drag_file = open("{}/drag{}.txt".format(results_directory, i), 'r')
    lift_file = open("{}/lift{}.txt".format(results_directory, i), 'r')

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

    cop_col = w_sheet.find("Center of Pressure (x=0 [m])", in_row = title_line).col
    drag_tot_col = w_sheet.find("A. Drag [N] (Total)", in_row = title_line).col
    drag_comp_col = w_sheet.find("B. Drag : Pressure +Viscous", in_row = title_line).col
    lift_tot_col = w_sheet.find("A. Lift [N] (Total)", in_row = title_line).col
    lift_comp_col = w_sheet.find("B. Lift [N] (Pressure + Viscous)", in_row = title_line).col

    sim_row_match = w_sheet.findall("{}".format(sim_numbers[i]), in_column=1)
    if len(sim_row_match) > 0:
        j = 0
        while sim_row_match[j].row < title_line:
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