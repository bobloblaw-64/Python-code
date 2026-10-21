
#CITS1401 Project. Code by Finlay Thomson, Student ID: 23953297

def main(file_name, ra_name):
    
    #open file and convert to matrix with all values lowercase 
    with open(file_name, 'r') as infile:
        file_matrix = []
        for line in infile:
            row = line.strip().split(',')
            lower_row = []
            for value in row:
                lower_row.append(value.lower())
            file_matrix.append(lower_row)
            
    #splits matrix into key and matrix
    key = file_matrix[0]
    file_matrix = file_matrix[1:]
    
    #handle case insensitivity:
    ra_name = ra_name.lower()
    
    #returns x value for a given matrix, row and key variable
    def row_value(input_matrix, row, key_value):
        return input_matrix[row][key.index(key_value)]
    
    #takes list, column title and value critera and strip the list of values that dont match
    def strip_list(list_to_strip, column_title, value_wanted):
        output = []
        for i in range(len(list_to_strip)):
            if row_value(list_to_strip, i, column_title).lower() == value_wanted.lower():
                output.append(list_to_strip[i])
        return output
    
    #takes a matrix and column title, returns all the values in that column as floats 
    def column_float(x, column_title):
        output = []
        for i in range(len(x)):
            try:
                output.append(float(row_value(x, i, column_title)))
            except ValueError:
                output = []
                break
        return output
    
    #similar to above but returns as a string
    def column_string(x, column_title):
        output = []
        for i in range(len(x)):
            output.append(str(row_value(x, i, column_title)))
        return output
        
    
    #compute SD of list as needed for OP1:
    def SD_of_list(list_to_compute):
        n = len(list_to_compute) #n = population size
        
        if n < 2:#as we take the root of 1/n-1 later we need to handle div0 and neg root errors
            return 0
        
        else:#this just SD formula in python form
            mean = sum(list_to_compute) / n
            sigma = 0.0
            for value in list_to_compute:
                sigma += (value - mean) ** 2
                
            return round((sigma / (n - 1)) ** 0.5, 4)
    
    #strips rows not in relevent region
    stripped_list = strip_list(file_matrix, "ra_name", ra_name)
    
    #Code for OP1:
    
    #sets up the OP1 dictionary keys as well as the first element of the value list (number of relevent sites)
    OP1 = {}
    for row in stripped_list:
        year = row[key.index('traffic_year')]
        if year in OP1:
            OP1[year][0] += 1
        else:
            OP1[year] = [1]
            
    #for loop to do calculations with each year in dictionary
    for year in OP1:
        
        #get a list of just the mon_sun data from relevant year
        stripped_by_year = strip_list(stripped_list, 'traffic_year', year)
        traff_vol_float = column_float(stripped_by_year, 'mon_sun')
        
        #add mean for year to output
        cur_year_mean = sum(traff_vol_float) / len(traff_vol_float)
        OP1[year].append(round(cur_year_mean, 4))
        
        #add SD for each year to output
        OP1[year].append(SD_of_list(traff_vol_float))
        
        #create list of tuples of the 3 values we care about for the last part of this output
        siteno_lst = column_string(stripped_by_year, 'site_no')
        heavy_percent_lst = column_float(stripped_by_year, 'pct_heavy_mon_sun')
        global_id_lst = column_string(stripped_by_year, 'globalid') 
        site_heavy_gid = list(zip(siteno_lst, heavy_percent_lst, global_id_lst))
        
        #sort first by heavy percent decending, then GID ascending, then the first element is our final value
        ordered_lst = sorted(site_heavy_gid, key=lambda x: (-x[1], x[2]))
        OP1[year].append(ordered_lst[0][0])
    
    
    #OP1 complete. Code for OP2:
        
    
    
    
    #set up a nested dictionary of all the LGA's as outer keys and all the SIDs as inner keys
    for row in stripped_list:
        gov_area = row[key.index('lg_name')]
        site_id = row[key.index('site_no')]
        if gov_area not in OP2:
            OP2[gov_area] = {site_id: []}
        else:
            OP2[gov_area][site_id] = []

    #iterate through a list of all the outer keys we just created and delete the ones that have less than 3 sites.
    for key in list(OP2.keys()):
        if len(OP2[key]) < 3:
            del OP2[key]
      
    
    #for gov_area in OP2:
        #for site_num in OP2[gov_area]:
    return siteno_lut
            
        
                 
print(main('sampleData_project.csv', 'Metropolitan'))
        
        
    
    