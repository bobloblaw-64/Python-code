
#CITS1401 Project. Code by Finlay Thomson, Student ID: 23953297

def main(file_name, ra_name):
    
    #handle case insensitivity:
    ra_name = ra_name.lower()
    
    #open file and convert to matrix with all values lowercase
    try:
        with open(file_name, 'r') as infile:
            file_matrix = []
            for line in infile:
                row = line.strip().split(',')
                lower_row = []
                for value in row:
                    lower_row.append(value.lower())
                file_matrix.append(lower_row)
                
    #if file_name invalid return empty values            
    except:
        return {}, {}, []
        
    #splits matrix into key and matrix
    try:
        key = file_matrix[0]
        file_matrix = file_matrix[1:]
    except:
        return {}, {}, []
    
    #do we have all required headers in this file?
    
    req_headers = ['site_no','ra_name','traffic_year','mon_sun','mon_fri','sat_sun','pct_heavy_mon_sun','pct_heavy_mon_fri',
                   'pct_heavy_sat_sun','lg_no','lg_name','ra_no','globalid','objectid']
     
    for header in req_headers:
        if header not in key:
            return {}, {}, []
            
    
    #returns x value for a given matrix, row and key variable
    def row_value(input_matrix, row, key_value):
        return input_matrix[row][key.index(key_value)]
    
    #takes list, column title and value critera and strip the list of values that dont match
    def strip_list(list_to_strip, column_title, value_wanted):
        col = key.index(column_title)
        value_wanted = value_wanted.lower()
        output = []
        for row in list_to_strip:
            if row[col] == value_wanted:
                output.append(row)
        return output
            
    
    #strips rows not in relevent region
    stripped_list = strip_list(file_matrix, "ra_name", ra_name)
    
    
    #detect invalid rows
    invalid_rows = []
    num_cols = ['mon_sun', 'mon_fri', 'sat_sun', 'pct_heavy_mon_sun', 'pct_heavy_mon_fri', 'pct_heavy_sat_sun', 'lg_no', 'ra_no', 'objectid']
    num_index = []
    for title in num_cols:
        num_index.append(key.index(title))
                         
    for row_no, row in enumerate(stripped_list):
        #check row has a value for each header value
        if len(row) != len(key):
            invalid_rows.append(row_no)
            continue
        #check if each value is valid
        for col_no, value in enumerate(row):
            value = value.strip()
            
            #special check for the year value as its a string but will be treated as a number later
            if key[col_no] == 'traffic_year':
                if len(value) != 7:
                    invalid_rows.append(row_no)
                    break  
                try:
                    int(value[:4])
                except:
                    invalid_rows.append(row_no)
                    break
            
            if value == "":#check if empty
                invalid_rows.append(row_no)
                break
            
            if value in ('na', 'null', 'none'):
                invalid_rows.append(row_no)
                break
            
            #is value meant to be a number, if so is it valid?
            if col_no in num_index:
                if value in ('nan', 'inf', '-inf'):
                    invalid_rows.append(row_no)
                    break
                try:
                    n = float(value)
                except:
                    invalid_rows.append(row_no)
                    break
                
                if n < 0:
                    invalid_rows.append(row_no)
                    break
    
    #removes invalid rows        
    valid_list = []
    for row_no, row in enumerate(stripped_list):
        if row_no not in invalid_rows:
            valid_list.append(row)
    
    stripped_list = valid_list
    
    
    
    #set up dictionary matching site_nos with indexs of rows they appear in
    site_count = {}
    for row_no, row in enumerate(stripped_list):
        cur_sid = row[key.index('site_no')]
        if cur_sid in site_count:
            site_count[cur_sid].append(row_no)
        else:
            site_count[cur_sid] = [row_no]
    
    #identifies sites w duplicate site_no   
    dupes = []        
    for sid, indexs in site_count.items():
        if len(indexs) > 1:
            dupes.append(sid)
            
    #removes duplicates        
    clean_list = []
    for row in stripped_list:
        sid = row[key.index('site_no')]
        if sid not in dupes:
            clean_list.append(row)
            
    stripped_list = clean_list
    
    if len(stripped_list) == 0:
        return {}, {}, []
    
    #takes a matrix and column title, returns all the values in that column as floats 
    def column_float(x, column_title):
        output = []
        for i in range(len(x)):
            output.append(float(row_value(x, i, column_title)))
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
        
    #look up table for OP2    
    site_no_lut = {}
    siteno_lst = column_string(stripped_list, 'site_no')
    mon_sun_lst = column_string(stripped_list, 'mon_sun')
    gid_lst = column_string(stripped_list, 'globalid')
    
    for row, site_num in enumerate(siteno_lst):
        site_no_lut[site_num] = [mon_sun_lst[row], gid_lst[row]]
    
    
    
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
    for year in list(OP1.keys()):
        
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
    
    OP2 = {}
    #set up a nested dictionary of all the LGA's as outer keys and all the SIDs as inner keys
    for row in stripped_list:
        gov_area = row[key.index('lg_name')]
        site_id = row[key.index('site_no')]
        traf_vol = float(row[key.index('mon_sun')])
        heavy_perc = float(row[key.index('pct_heavy_mon_sun')])
        if gov_area not in OP2:
            OP2[gov_area] = {site_id: [traf_vol, heavy_perc]}
        else:
            OP2[gov_area][site_id] = [traf_vol, heavy_perc]

    #iterate through a list of all the outer keys we just created and delete the ones that have less than 3 sites.
    for lga in list(OP2.keys()):
        if len(OP2[lga]) < 3:
            del OP2[lga]
            
        #remaining keys we will add a rank    
        else:
            #make list of tuples with relevent values so we can use sorted
            cur_lga_data = []
            for site in OP2[lga].keys():
                mon_sun = OP2[lga][site][0]
                gid = site_no_lut[site][1]
                q2_tup = (site, mon_sun, gid)
                cur_lga_data.append(q2_tup)
                
            #sort as per requirement
            lga_sorted = sorted(cur_lga_data, key=lambda x: (-x[1], x[2]))

            #rebuild each lga with ranks
            ranked = {}
            rank = 1
            for tup in lga_sorted:
                site = tup[0]
                mon_sun = tup[1]
                gid = tup[2]
                pct_heavy = OP2[lga][site][1]
                ranked[site] = [mon_sun, pct_heavy, rank]
                rank += 1

            OP2[lga] = ranked
        
    #OP2 finished, OP3 code:
        
    
    monfri_means = []
    satsun_means = []
    year_heavy = {}
    
    #set up a dictionary for each included year as keys and the two heavy percent values
    
    year_lst = column_string(stripped_list, 'traffic_year')
    heavy_weekday_lst = column_float(stripped_list, 'pct_heavy_mon_fri')
    heavy_weekend_lst = column_float(stripped_list, 'pct_heavy_sat_sun')
    
    year_tup = list(zip(year_lst, heavy_weekday_lst, heavy_weekend_lst))
    
    for year, monfri, satsun in year_tup:
        if year not in year_heavy:
            year_heavy[year] = [(monfri, satsun)]
        else:
            year_heavy[year].append((monfri, satsun))
            
    #calculate both averages and add them to seprate lists along with relevent year        
    for year, values in year_heavy.items():
        year_int = int(year[:4])#convert year from string to int we can work with 
        mf_sum = 0
        ss_sum = 0
        for monfri, satsun in values:
            mf_sum += monfri
            ss_sum += satsun
            
        mf_mean = mf_sum / len(values)
        ss_mean = ss_sum / len(values)
        
        monfri_means.append([year_int, mf_mean])
        satsun_means.append([year_int, ss_mean])
        
    #sort by year ascending    
    monfri_means.sort(key=lambda x: x[0])
    satsun_means.sort(key=lambda x: x[0])
    
    #can get rid of the year values now as theyre not part of the output
    years, mf_data = map(list, zip(*monfri_means))
    years, ss_data = map(list, zip(*satsun_means))
    
    
    
    #helper functions for cosine similarity
    
    #given two vectors return dot product (this will be our numerator)
    def dot_prod(A, B):
        result = 0
        for A_i, B_i in zip(A, B):
            result += (A_i * B_i)
        return result
    
    #denominator requires vectors magnitude 
    def magnitude(v):
        n = 0.0
        for i in v:
            n += i ** 2
            
        return (n ** 0.5)
    
    #compute cosine similarity and add to OP3
    if magnitude(mf_data) == 0 or magnitude(ss_data) == 0:#handle div0 error
        cos_sim = 0
    else:
        cos_sim = round((dot_prod(mf_data, ss_data)) / (magnitude(mf_data) * magnitude(ss_data)), 4)
    
    #we didnt round earlier as we use this data to calculate cos sim
    mf_data_rounded = [round(value, 4) for value in mf_data]
    ss_data_rounded = [round(value, 4) for value in ss_data]
    
    #define OP3
    OP3 = [mf_data_rounded, ss_data_rounded, cos_sim]
    
    #all done! return all 3 outputs
    return OP1, OP2, OP3
        
    