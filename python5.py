
#-----------<  Assignment 1  >----------
# Q1
num1 = int(input("Enter the number One\n"))
num2 = int(input("Enter the number Second\n"))
num3 = int(input("Enter the number Third\n"))
sum = (num2 + num1+num3)/3
print("The average of three number :", sum)
# Q2
# Taking input as float
income = float(input("Enter annual income: \n"))
# taking  input as no. of depondents
f = int(input("Enter number of dependents\n"))
# calculating tax amount had to paid
tax = ((income*0.20)-10000-(3000*f))
# printing tax amount
print("Your tax payabale amount is: ", tax)


# -----------------++++++++++++------------------

# Q3
SID = int(input("Enter the SID \n"))
Name = input("Enter the Name\n ")
Gender = input("Enter the Gender\n")
Course = input("Enter the Course Name\n")
Grade = float(input("Enter the CGPA\n"))

# --------------------++++++++++++++------------------
# Q4

# Taking marks as array:
student_marks = [223, 834, 146, 446, 635, 335, 752]
print("\ndecending Order"),
print(sorted(student_marks, reverse=True))

# -----------------++++++++++++++_____________________
# Q5
# a)
colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("Orignal colour : ", colour)
del colour[3]
print("After removing 4th element:  ", colour)


# b)
colour2 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("Original colour", colour2)
del colour2[3]
colour2[3] = 'Purple'
print("After replacing colour and removing ", colour2)


# -------------------------+++++++++++--------------------
