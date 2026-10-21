def main(file_name, ra_name):
    #file_name = "SampleData_lab4.csv" 
        
    #takes csv file, returns a list of each of its rows as a list 
    input_file = open(file_name, "r")
    file_matrix = []
    for line in input_file: #for loop takes each row of file, turns into a list and adds it to our matrix
        row = line[:-1]#this removes the \n
        file_matrix.append(row.split(","))#converts row from string to list and adds to our matrix
    input_file.close()
    
    #splits matrix into key and matrix
    key = file_matrix[0]
    file_matrix = file_matrix[1:]
    
    def row_value(input_matrix, row, key_value):#returns x value for a given matrix, row and key variable
        return input_matrix[row][key.index(key_value)]
    
    #strips rows not in relevent region
    stripped_list = []
    for i in range(len(file_matrix)):
        if row_value(file_matrix, i, "RA_NAME") == ra_name:
            stripped_list.append(file_matrix[i])
    #sort by global ID:        
    stripped_list = sorted(stripped_list, key=lambda x: x[-1])
    
    #reduces matrix to pairs of specific key values we care about            
    def two_value_matrix(big_matrix, key_value_0, key_value_1):
        output = []
        for i in range(len(big_matrix)):
            x = [row_value(big_matrix, i, key_value_0), row_value(big_matrix, i, key_value_1)] 
            output.append(x)
        return output
    
    def whole_row_float(x, row_title):
        output = []
        for i in range(len(x)):
            output.append(row_value(x, i, row_title))
    
    #code for OP1:
    
    relevant_years = []#this list is the values in our stripped list that are later than 2022/23
    for i in range(len(stripped_list)):
        year = row_value(stripped_list, i, "TRAFFIC_YEAR") 
        if year[-2:] >= "23":
            relevant_years.append(stripped_list[i])
            
    #2 wide matrix with site no and traffic volume as values:
    site_traffic_volume = two_value_matrix(relevant_years, "SITE_NO", "MON_SUN")
    max_value = 0
    min_value = 0
    max_site = 0
    min_site = 0
    #find max and min in list, already ordered by id so we can take the first occurance of an extrema
    for i in range(len(site_traffic_volume)):
        traffic_int = int(site_traffic_volume[i][1])
        if traffic_int > max_value:
            max_value = traffic_int
            max_site = site_traffic_volume[i][0]
        if traffic_int < min_value or i == 0:
            min_value = traffic_int
            min_site = site_traffic_volume[i][0]
    
    OP1 = [max_site, min_site]#output 1 finished
    
    #code for output 2:
    
    #compute SD of any list:
    def SD_of_list(list_to_compute):
        heavy_percent = []
        for i in range(len(list_to_compute)):#gives list of just the values we care about and makes them floats
            heavy_percent.append(float(row_value(list_to_compute, i, "PCT_HEAVY_MON_SUN")))
        n = len(heavy_percent) #n = population size
        heavy_mean = sum(heavy_percent) / n
        sigma = 0.0
        for i in range(n):
            sigma += (heavy_percent[i] - heavy_mean) ** 2.0
        return round((sigma / (n - 1)) ** 0.5, 4)
    
    OP2 = [SD_of_list(stripped_list), SD_of_list(file_matrix)]
    
    #code for output 3:
    def sum_of_diff_to_power(data, power):#correlation formula uses these sums 3 times
        mean = sum(data) / n
        result = 0
        for i in range(len(data)):
            result += (data[i] - mean) ** power
        return result
    
    sum_of_diff_to_power(
        
    
    
    
    
    
        
    
    
        
    
 
        
        
    
    
    
    
    
                   
main("SampleData_lab4.csv", "Metropolitan")

    
    

