# Written by BOT Yokel

import gspread
"""
WARNING: This script assumes you have set up the Google Drive and Google Sheets API.
It will not work if you do not have these set up, along with the OAuth2 credentials stored on your computer.

HOW TO USE THIS SCRIPT:
1. Enter the directory of the folder containing the data saved as text files under results_directory. Ensure that all backslashes are changed to forward slashes.
e.g. C:/Users/david/Documents/1_(SSD)_Important_Things/Work/Project Liber
2. Enter the row number of the title line for the set of data under title_line
3. Enter the simulation numbers or uniquely identifying names corresponding to the exported simulation data under sim_numbers.
e.g. sim_numbers = [1,2,3,4], or sim_numbers = ["nc0", "nc50", "nc90"]
Where cp0.txt, drag0.txt, lift0.txt, etc. all correspond to Sim 1; cp1.txt, drag1.txt, lift1.txt, etc. all correspond to Sim 2; etc.

4. Enter the EXACT title of the spreadsheet under s_sheet_title.
5. Enter the EXACT title of the worksheet under which the data will be entered under w_sheet_title.
6. Enter the number of results you wish to export under num_results
7. Save the edited script in the same directory where ALL the results are located
8. Go ahead and run the script
"""

results_directory = "INSERT_HERE"
title_line = 000
sim_numbers = [
1,2
]
num_results = 000

s_sheet_title = "INSERT_HERE"
w_sheet_title = "DOE Summary Results"

gc = gspread.oauth()

spreadsheet = gc.open("{}".format(s_sheet_title))
w_sheet = spreadsheet.worksheet("{}".format(w_sheet_title))

for i in range(num_results):
    cop_file = open("{}/cp{}.txt".format(results_directory, i), 'r')
    drag_file = open("{}/drag{}.txt".format(results_directory, i), 'r')
    lift_file = open("{}/lift{}.txt".format(results_directory, i), 'r')
    iter_file = open("{}/iter{}.txt".format(results_directory, i), 'r')
    f_left_file = open("{}/f_left{}.txt".format(results_directory, i), 'r')
    f_right_file = open("{}/f_right{}.txt".format(results_directory, i), 'r')
    pitch_file = open("{}/pitch_moment{}.txt".format(results_directory, i), 'r')
    roll_file = open("{}/roll_moment{}.txt".format(results_directory, i), 'r')
    yaw_file = open("{}/yaw_moment{}.txt".format(results_directory, i), 'r')

    cop_all_data = cop_file.readlines()
    drag_all_data = drag_file.readlines()
    lift_all_data = lift_file.readlines()
    iter_all_data = iter_file.readlines()
    f_left_all_data = f_left_file.readlines()
    f_right_all_data = f_right_file.readlines()
    pitch_all_data = pitch_file.readlines()
    roll_all_data = roll_file.readlines()
    yaw_all_data = yaw_file.readlines()

    # cop values are on line 5
    # drag values are on line 13
    # lift values are on line 13
    # iter values are on line 1
    # f_left values are on line 13
    # f_right values are on line 13
    # pitch moment values are on line 13
    # roll moment values are on line 13
    # yaw moment values are on line 13

    cop_line_data = cop_all_data[4].split()
    drag_line_data = drag_all_data[12].split()
    lift_line_data = lift_all_data[12].split()
    iter_line_data = iter_all_data[0].split()
    f_left_line_data = f_left_all_data[12].split()
    f_right_line_data = f_right_all_data[12].split()
    pitch_line_data = pitch_all_data[12].split()
    roll_line_data = roll_all_data[12].split()
    yaw_line_data = yaw_all_data[12].split()

    cop_values = str(cop_line_data[1]) + " " + str(cop_line_data[2])
    drag_comp_values = str(drag_line_data[1]) + " " + str(drag_line_data[2])
    drag_tot_value = str(drag_line_data[3])
    lift_comp_values = str(lift_line_data[1] + " " + lift_line_data[2])
    lift_tot_value = str(lift_line_data[3])
    iter_value = str(iter_line_data[0])
    f_left_value = str(f_left_line_data[3])
    f_right_value = str(f_right_line_data[3])
    pitch_value = str(pitch_line_data[3])
    roll_value = str(roll_line_data[3])
    yaw_value =str(yaw_line_data[3])

    cop_col = w_sheet.find("Center of Pressure (x=0 [m])", in_row = title_line).col
    drag_tot_col = w_sheet.find("A. Drag [N] (Total)", in_row = title_line).col
    drag_comp_col = w_sheet.find("B. Drag [N]: Pressure + Viscous", in_row = title_line).col
    lift_tot_col = w_sheet.find("A. Lift [N] (Total)", in_row = title_line).col
    lift_comp_col = w_sheet.find("B. Lift [N]: Pressure + Viscous", in_row = title_line).col
    f_left_col = w_sheet.find("Force Left [N] (Total)", in_row = title_line).col
    f_right_col = w_sheet.find("Force Right [N] (Total)", in_row = title_line).col
    pitch_col = w_sheet.find("Pitch Moment [N-m] (axis = [0,1,0])", in_row = title_line).col
    roll_col = w_sheet.find("Roll Moment [N-m] (axis = [1,0,0])", in_row = title_line).col
    yaw_col =w_sheet.find("Yaw Moment [N-m] (axis = [0,0,1])", in_row = title_line).col
    status_col = w_sheet.find("Status", in_row = title_line).col
    iter_col = w_sheet.find("Number of Iterations", in_row = title_line).col

    sim_row_match = w_sheet.findall("{}".format(sim_numbers[i]), in_column=1)
    if len(sim_row_match) > 0:
        j = 0
        while sim_row_match[j].row < title_line:
            j+=1
    else:
        print("Script failed. Could not find matching row for simulation data.")
        input("Press enter to continue...")
    
    sim_row = sim_row_match[j].row

    w_sheet.update_cell(sim_row, iter_col, iter_value)
    w_sheet.update_cell(sim_row, drag_tot_col, drag_tot_value)
    w_sheet.update_cell(sim_row, drag_comp_col, drag_comp_values)
    w_sheet.update_cell(sim_row, lift_tot_col, lift_tot_value)
    w_sheet.update_cell(sim_row, lift_comp_col, lift_comp_values)
    w_sheet.update_cell(sim_row, status_col, "*converged done")
    w_sheet.update_cell(sim_row, cop_col, cop_values)
    w_sheet.update_cell(sim_row, f_left_col, f_left_value)
    w_sheet.update_cell(sim_row, f_right_col, f_right_value)
    w_sheet.update_cell(sim_row, pitch_col, pitch_value)
    w_sheet.update_cell(sim_row, roll_col, roll_value)
    w_sheet.update_cell(sim_row, yaw_col, yaw_value)

    cop_file.close()
    drag_file.close()
    lift_file.close()
    iter_file.close()
    f_left_file.close()
    f_right_file.close()
    pitch_file.close()
    roll_file.close()
    yaw_file.close()