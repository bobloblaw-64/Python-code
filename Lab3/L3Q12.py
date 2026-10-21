def locate_person(age_list, name_list, age, name):
    for i in range(len(name_list)):
        if name_list[i] == name and age_list[i] == age:
            return i
            break

print(locate_person([15, 7, 3, 9, 11, 6, 8], ["David", "Tom", "Mary", "Sam", "Harry", "Abby", "Nigel"], 3, "Mary"))
print(locate_person([15, 7, 3, 9, 11, 6, 8], ["David", "Tom", "Mary", "Sam", "Harry", "Abby", "Nigel"], 11, "Harry"))            
    