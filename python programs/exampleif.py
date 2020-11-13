# if - else block
# used for conditional programming

#ex1
'''
marks = int(input("Enter marks:"))

if marks > 35:
    print("Fail")
    print("study hard for the next year")
else:
    print("pass")
    print("lets celebrate")
'''

# elif
'''
marks = int(input("Enter marks:"))

if marks < 35:
    print("Grade D")
elif marks >= 35 and marks < 60:
    print("Grade c")
elif marks >= 60 and marks < 85:
    print("Grade B")
elif marks >= 85 and marks < 100:
    print("Grade A")
else:
    print("Invalid marks")
'''

# ex3

'''
Enter phone number: 9000468563
valid number

Enter phone number: 47gsdt
Invalid number

use -> isdecimal()
'''

phone = input("Enter phone number:")

if phone.isdecimal() == True:
    print("Valid number")
else:
    print("Invalid number")

'''

'''
phone = input("Enter phone number:")

if phone.isdecimal() and len(phone)
    print("Valid number")
else:
    print("Invalid number")

'''





# ex4
'''

Enter name: phani
valid name
Enter name: phani123
invalis number
use :- isaplha()
'''
