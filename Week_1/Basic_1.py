"""
1. Write a program that will output the text “Hello There” to screen. Create a String
variable to store your name and an int variable to store your age. Print this out to
screen using the Script mode.
"""
userName = "John Smith"
userAge = 85
print("Hello There ", userName, " your age is: ", userAge)


"""
2. Write a program that asks the user to enter a distance in kilometres and then converts
that distance to miles (Miles = Kilometres * 0.6214).
"""
distanceKM = int(input("Please enter a distance\t"))
distanceMIL = distanceKM * 0.6214
print("Your distance in KM:\t", distanceKM, "\nYour distance in Miles:\t", round(distanceMIL, 2))


"""
3. Write a program that will ask a student for their first name and then for their surname.
It should then ask the student to enter the int numerical grade they received in each of
their three subjects.The program should then print out the full name of the student along with their
average numerical grade (Use only a single print statement)
"""
studFName = input("Please input your first name\t")
studLName = input("Please input your surname\t")
enGrade = int(input("Please input your grade for English\t"))
bioGrade = int(input("Please input your grade for Biology\t"))
sciGrade = int(input("Please input your grade for Science\t"))
print("Student:\n", studFName, " ", studLName, "\nYour Grades:\nEnglish\t", enGrade, "\nBiology\t", bioGrade, "\nScience\t", sciGrade, "\nYour average score:\t", (enGrade + bioGrade + sciGrade) / 3)


"""
4. Write a program to calculate and display a person’s body mass index (BMI). A persons
BMI is calculated with the following formula:
• BMI = (weight/ height2 ) * 703
Where weight in in pounds and height in in inches.
"""
weight = int(input("Please input your weight\t"))
height = int(input("Please input your height\t"))
bmi = (weight / height**2) * 703
convertedBMI = ((weight * 2.20462) / (height * 0.393701)**2) * 703
print("Your body mass index is:\t", round(bmi, 4), "\nand converted version is:\t", round(convertedBMI, 4))


"""
5. There are three seating categories at a stadium. For a football games, Class A seat’s
cost €25, Class B seat’s cost €20 and Class C seat’s cost €30. Write a program that
asks how many tickets for each class of seats were sold, and then display the amount
of income generated from ticket sales.
"""
aClass = int(input("Please input number of sold tickets in A Class"))
bClass = int(input("Please input number of sold tickets in B Class"))
cClass = int(input("Please input number of sold tickets in C Class"))
amount = 0
if aClass != 0:
    amount = amount + aClass * 25
if bClass != 0:
    amount = amount + bClass * 20
if cClass != 0:
    amount = amount + cClass * 30
print("Total amount is:\t", amount)
