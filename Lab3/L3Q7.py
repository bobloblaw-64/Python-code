def bmi_risk(bmi, age):
    if bmi < 22:
        if age < 45:
            return "Low"
        else:
            return "Medium"
    else:
        if age < 45:
            return "Medium"
        else:
            return "High"
        
print(bmi_risk(21.5, 44))
print(bmi_risk(30, 27))
print(bmi_risk(30, 45))