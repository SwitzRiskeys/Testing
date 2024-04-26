import math
'''average_age=100
age=int(input("Age \n"))

print(f'Your answer = {average_age - age} ')'''

#2
'''print("Welcome!\n Would you like to calculayte your age?")
CurrentYear=int(input("Input year current \n"))
YearOfBirth=int(input("Input year of birth\n"))

print(f'Your current age is {CurrentYear-YearOfBirth}')'''

#3
'''Yes = "Yes"
No = "No"

print("Would you like to calculayte your age?")
Response=input("")

CurrentYear=int(input("Input current year \n"))
YearOfBirth=int(input("Input year of birth\n"))
if Response == Yes:
    print(f'Your current age is {CurrentYear-YearOfBirth}')

else:
     Response==No
     print("Oh really?\nGet out then!!!")'''


Yes = "Yes"
No = "No"

print("Welcome!\n Would you like to calculayte your age?")
Response = input("")

if Response == Yes:
    
    CurrentYear = int(input("Input current year:\n"))
    YearOfBirth = int(input("Input year of birth:\n"))
    print(f'Your current age is {CurrentYear-YearOfBirth}')

elif  Response==No:
     print("Oh really?\nGet out then!!!")
else:
    print("Invalid response")