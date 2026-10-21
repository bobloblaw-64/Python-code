#2021 exam

#question 1

def stringexpand(name):
    output = ""
    for letter in name:
        output += letter + " "
    return output[:-1]

#question 2

def palindrome(word):
    word = word.lower()
    reverse = ""
    for i in range(1, len(word) + 1):
        reverse += word[-i]
    print(reverse)    
    if reverse == word:
        return True
    else:
        return False
    
#question 3
    
def sortdict(dic):
    output = []
    for sid, wam in dic.items():
        output.append((sid, wam))
        
    output.sort(key=lambda x: -x[1])
    return output

#question 4

def sumdigits(n):
    if n // 10 == 0:
        return n
    else:
        return (n % 10) + sumdigits(n // 10)
    
#question 5
def fac(n):
    total = 1
    for i in range(1,n+1):
        total = total * i
    return total
 

def seriesexp(x, tol):
    n = 0
    total = 0
    term = 1
    while True:
        term = (x ** n) / fac(n)
        if abs(term) < tol:
            break
        total += term
        n += 1
    return total

#question 6

def multiply_lists(lst):
    total = 1
    for i in lst:
        if type(i) == list:
            total *= multiply_lists(i)
        else:
            total *= float(i)
            
    return total

#question 7

def team_maker(pool1, pool2, pool3):
    output = []
    for batter in pool1:
        for bowler in pool2:
            for wickie in pool3:
                output.append(batter + ' ' + bowler + ' ' + wickie)
    return output

#question 8
def user_account(filename):
    matrix = []
    file_dict = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                matrix.append(line.split().strip())
        headers = matrix[0]
         
            
        
    except:
        return None



    
        
    



                
        
    