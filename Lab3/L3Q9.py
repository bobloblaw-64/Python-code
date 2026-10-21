def record_check(age, gender, location):
    """ Function to find a male person depending on their age, gender and location """
    if age > 18 and gender == 'M' and (location == "Perth" or location == "Sydney"):
        print("Found him!")
    else:
        print("Did not find him.")
    
        
record_check(16, 'F', 'Brisbane')
record_check(19, 'M', 'Perth')
record_check(19, 'F', 'Melbourne')