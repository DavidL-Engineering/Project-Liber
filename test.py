results_directory = "C:/Users/david/Documents/1_(SSD)_Important_Things/Work/Project Liber/Results"
files_directory = "C:/Users/david/Documents/1_(SSD)_Important_Things/Work/Project Liber/Data"

iter_file = open("{}/drag-rfile.out".format(files_directory), 'r')
iter_lines = iter_file.readlines()
iter_data = iter_lines[len(iter_lines)-1]

output = open("{}/iter{}.txt".format(results_directory, 0), 'w')
output.write(iter_data)
output.close()