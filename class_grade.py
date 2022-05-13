




""" PlAIN ENGLISH
Start
Create a list to store 5 numbers (float)
Capture user's input 5 times for their grades 
Each time we capture the user's input, we append the number to the list 
Sort the list ascending, then splice the items starting at index 2
Once we have three highest numbers in the list, we sum them up and divide by 3 
Output a messafe to the user 
End
"""

""" PSUEDOCODE
Create list 

Capture input 
Append number to list 

Capture input 
Append number to list 

Capture input 
Append number to list 

Capture input 
Append number to list 

Capture input 
Append number to list 

Sort the list, then splice out the two lowest numbers
Print message to user
"""

grades = []

grade = input("Enter the 1st grade: ")
grades.append(float(grade))

grade = input("Enter the 2nd grade: ")
grades.append(float(grade))

grade = input("Enter the 3rd grade: ")
grades.append(float(grade))

grade = input("Enter the 4th grade: ")
grades.append(float(grade))

grade = input("Enter the 5th grade: ")
grades.append(float(grade))

grades.sort()

grades= grades[2: ]

grades = sum(grades)

result = grades / 3

print("Average Grade {0:.2f}%".format(result))
#print(grades, 'resutls', result)
