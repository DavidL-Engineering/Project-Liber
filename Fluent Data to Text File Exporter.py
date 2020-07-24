# encoding: utf-8
# Release 19.1
SetScriptVersion(Version="19.1.103")

'''
Instructions:
1. Enter results directory under variable results_directory. Change all backslashes to forward slashes
e.g. results_directory = "C:/Users/tom/Documents/DV2 Nose Study/Group 3/Results"
2. Enter the workbench project's file directory under files_directory. Change all backslashes to forward slashes
e.g. files_directory = "C:/Users/tom/Documents/DV2 Nose Study/Group 3/DV2 Nose Study Group 3_files"
3. Enter the number of simulations you wish to retrieve results from under num_sims
'''

results_directory = "insert_here"
files_directory = "insert_here"
num_sims = 0

i = 0

#For first Fluent sim
if i==0:
    system1 = GetSystem(Name="FLU")
    solution1 = system1.GetContainer(ComponentName="Solution")
    solution1.Edit()
    setup1 = system1.GetContainer(ComponentName="Setup")
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Results|Reports|Forces"))(cx-gui-do cx-list-tree-right-click "NavigationPane*List_Tree1" )')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*PopupMenuTree-Forces*Edit...")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Force Reports*List2(Wall Zones)\" '( 0 1))(cx-gui-do cx-activate-item \"Force Reports*List2(Wall Zones)\")(cx-gui-do cx-set-list-selections \"Force Reports*List2(Wall Zones)\" '( 0))(cx-gui-do cx-activate-item \"Force Reports*List2(Wall Zones)\")")
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"Force Reports*PanelButtons*PushButton4(Write)\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"{}/drag{}.txt\") \"All Files (*)\")".format(results_directory, i))
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame1(Direction Vector)*RealEntry3(Z)\" '( 1))(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame1(Direction Vector)*RealEntry1(X)\" '( 0))")
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"Force Reports*PanelButtons*PushButton4(Write)\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"lift{}.txt\") \"All Files (*)\")".format(i))
    setup1.SendCommand(Command='(cx-gui-do cx-set-toggle-button2 "Force Reports*Table1*ToggleBox1(Options)*Center of Pressure" #t)(cx-gui-do cx-activate-item "Force Reports*Table1*ToggleBox1(Options)*Center of Pressure")')
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"Force Reports*PanelButtons*PushButton4(Write)\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"cp{}.txt\") \"All Files (*)\")".format(i))
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Force Reports*PanelButtons*PushButton2(Cancel)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*FileMenu*Close Fluent")')
    
    iter_file = open("{}/dp0/FLU/Fluent/drag-rfile.out".format(files_directory), 'r')
    iter_lines = iter_file.readlines()
    iter_data = iter_lines[len(iter_lines)-1]

    output = open("{}/iter{}.txt".format(results_directory, i), 'w')
    output.write(iter_data)
    output.close()
    
    i+=1

for i in range(1,num_sims):
    system1 = GetSystem(Name="FLU {}".format(i))
    solution1 = system1.GetContainer(ComponentName="Solution")
    solution1.Edit()
    setup1 = system1.GetContainer(ComponentName="Setup")
    setup1.SendCommand(Command='(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Results|Reports|Forces"))(cx-gui-do cx-list-tree-right-click "NavigationPane*List_Tree1" )')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*PopupMenuTree-Forces*Edit...")')
    setup1.SendCommand(Command="(cx-gui-do cx-set-list-selections \"Force Reports*List2(Wall Zones)\" '( 0 1))(cx-gui-do cx-activate-item \"Force Reports*List2(Wall Zones)\")(cx-gui-do cx-set-list-selections \"Force Reports*List2(Wall Zones)\" '( 0))(cx-gui-do cx-activate-item \"Force Reports*List2(Wall Zones)\")")
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"Force Reports*PanelButtons*PushButton4(Write)\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"{}/drag{}.txt\") \"All Files (*)\")".format(results_directory, i))
    setup1.SendCommand(Command="(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame1(Direction Vector)*RealEntry3(Z)\" '( 1))(cx-gui-do cx-set-real-entry-list \"Force Reports*Table1*Frame2*Frame1(Direction Vector)*RealEntry1(X)\" '( 0))")
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"Force Reports*PanelButtons*PushButton4(Write)\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"lift{}.txt\") \"All Files (*)\")".format(i))
    setup1.SendCommand(Command='(cx-gui-do cx-set-toggle-button2 "Force Reports*Table1*ToggleBox1(Options)*Center of Pressure" #t)(cx-gui-do cx-activate-item "Force Reports*Table1*ToggleBox1(Options)*Center of Pressure")')
    setup1.SendCommand(Command="(cx-gui-do cx-activate-item \"Force Reports*PanelButtons*PushButton4(Write)\")(cx-gui-do cx-set-file-dialog-entries \"Select File\" '( \"cp{}.txt\") \"All Files (*)\")".format(i))
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "Force Reports*PanelButtons*PushButton2(Cancel)")')
    setup1.SendCommand(Command='(cx-gui-do cx-activate-item "MenuBar*FileMenu*Close Fluent")')
    
    
    iter_file = open("{}/dp0/FLU-{}/Fluent/drag-rfile.out".format(files_directory, i), 'r')
    iter_lines = iter_file.readlines()
    iter_data = iter_lines[len(iter_lines)-1]

    output = open("{}/iter{}.txt".format(results_directory, i), 'w')
    output.write(iter_data)
    output.close()
