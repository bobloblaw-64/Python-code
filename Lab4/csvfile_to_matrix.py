
#takes csv file, returns a list of each of its rows as a list 
def csvfile_to_matrix(filename):
    input_file = open(filename, "r")
    file_matrix = []
    for line in input_file: #for loop takes each row of file, turns into a list and adds it to our matrix
        row = line[:-1]#this removes the \n
        file_matrix.append(row.split(","))#converts row from string to list and adds to our matrix
    input_file.close()
    return file_matrix
                      


