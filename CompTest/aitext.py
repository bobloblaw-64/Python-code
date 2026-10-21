#question 1:

def ssq_even(lst):
    total = 0
    for value in lst:
        if value % 2 == 0:
            total += value ** 2
    return total

#question 2:

def grade(marks):
    if marks > 100 or marks < 0:
        return "Invalid"
    elif marks >= 80:
        return "HD"
    elif marks >= 70:
        return "D"
    elif marks >= 60:
        return "CR"
    elif marks >= 50:
        return "P"
    else:
        return "F"

#question 3:
def stocks(filename):
    output = 0
    with open(filename, 'r') as infile:
        for line in infile:
            stripped_line = line.strip().split(",")
            for value in stripped_line:
                if value > 5:
                    output += value
    return output
    
#question 4

def inputmarks(subject):
    while True:
        n = float(input("enter a mark for " + subject))
        if n > 100:
            print("Too High")
        elif n < 0:
            print("Too Low")
        else:
            return n
inputmarks('maths')
    
    
    

                        
                
                
        
        
        