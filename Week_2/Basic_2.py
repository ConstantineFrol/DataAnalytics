import math

"""
(1)
(Basic if/elif statements)
The area of a rectangle is the length multiplied by width. Write a program that asks for the
length and width of two rectangles. The program should tell the user which rectangle has the
greater area or if the areas are the same.
"""
try:
    print("This programme will ask length and width for 2 rectangles")
    length1 = int(input("Please input length of the first rectangle\t"))
    width1 = int(input("Please input width of the first rectangle\t"))
    length2 = int(input("Please input length of the second rectangle\t"))
    width2 = int(input("Please input width of the second rectangle\t"))
    if (length1 * width1) > (length2 * width2):
        print("First rectangles area is bigger than second one")
    elif (length1 * width1) == (length2 * width2):
        print("First rectangles area are same as second one")
    else:
        print("First rectangles area is smaller than second one")
except:
    print("Oops, wrong input, please run the program again")
print("Thank you for using my programme")

"""
(2)
(Nested if Statements and Logical Operators)
A development company will only employ an individual if they have a minimum of 4 years
of commercial software development experience, a Microsoft certification and a first class
honours undergraduate computing degree.
(i) Write a program that will use nested if statements to determine if a user is
sufficiently qualified to be employed. The first if statement should check if the
user has 4 years of commercial software development experience, the second
nested if statement should check if they have a Microsoft certification and the
final nested if statement should check if the user has a first class honours
undergraduate computing degree.
If the user does not satisfy one of the conditions the program should inform the
user that they not eligible and should also inform the user of the requirement they
have failed. The program should then exit.
"""
exp = (int(input("How many years of commercial software development experience do you have:\t")))
if exp >= 4:
    micCert = input("Do you hold a Microsoft certification y/n:\t")
    if micCert == "y":
        compDeg = input("Do you have a first class honours undergraduate computing degree y/n:\t")
        if compDeg == "y":
            print("We would be grateful if you will join our team")
        else:
            print("We are sorry, You are not eligible.You need to hold a first class honours undergraduate computing degree.")
    else:
        print("We are sorry, You are not eligible.You are not eligible. You need to hold a Microsoft certification.")
else:
    print("We are sorry, You are not eligible.You have not enough experience in commercial software development")

"""
(ii) Rewrite the above program so you only use only a single if statement to check that
the user satisfies the above conditions to be employed (you will need to use an
and logical operator). Please note this version of the program will ask the user to
enter all relevant information first and will then inform the user if they are eligible
or not. Note it does not need to inform the user of the specific reasons as to why
they were not accepted.
"""
exp = (int(input("How many years of commercial software development experience do you have:\t")))
microCert = input("Do you hold a Microsoft certification y/n:\t")
degree = input("Do you have a first class honours primary degree y/n:\t")
if (exp < 4 and microCert != "y" and degree != "y") or (exp >= 4 and microCert != "y" and degree != "y") or (exp >= 4 and microCert == "y" and degree != "y") or (
        exp >= 4 and microCert != "y" and degree == "y") or (exp < 4 and microCert == "y" and degree == "y"):
    print("You are not eligible for this position.")

"""
(3)
(if elif Statements)
A software company sells a package that retails for €99. Quantity discounts are given
according to the following table.
Quantity     Discount
1 – 9........0%
10 – 19......20%
20 – 49......30%
50 – 99......40%
100 or more..50%
Write a program that will ask the user to enter the number of packages purchased. The
program should display the amount of the discount (if any) and the total amount of the
purchase after the discount. Please note that if a user indicates a negative quantity then they
should be told that the quantity value should be greater than zero.
Please use if elif statements to solve this problem and note that your solution to this problem
should make use of the and logical operator where possible.
"""
itemPrice = 99
userInput = False
try:
    while not userInput:
        items = (int(input("Please input number of purchased items\t")))
        if items < 0:
            print("Invalid input - input must be greater than 0 (zero)")
        else:
            if 0 < items < 10:
                print("Total.........\u20ac", items * itemPrice)
                userInput = True
            elif items >= 10 and items < 20: # better use: 10 <= items <= 20, but need to use AND
                print("Discount\t20%\nTotal\t\u20ac", (items * itemPrice) - (items * itemPrice) * 20 / 100)
                userInput = True
            elif items >= 20 and items < 50:
                print("Discount\t30%\nTotal\t\u20ac", (items * itemPrice) - (items * itemPrice) * 30 / 100)
                userInput = True
            elif items >= 50 and items < 100:
                print("Discount\t40%\nTotal\t\u20ac", (items * itemPrice) - (items * itemPrice) * 40 / 100)
                userInput = True
            elif items >= 100:
                print("Discount\t50%\nTotal\t\u20ac", (items * itemPrice) - (items * itemPrice) * 50 / 100)
                userInput = True
except Exception as e:
    print("Invalid input - Please check your input\n", e)

"""
(4)
(for loops and functions)
(i)
You should write a function that will print out the ‘times’ table for a number up to a specific
limit. The function should take in two parameters. The first value, num, is the number that we
will multiply by 0, 1, 2, 3, etc. The second number, limit, is the number at which we will stop
multiplying.So if the user enters 3 as the value of num and 5 as the value of limit then the 
program will output the 3 times table from 0 to 5 as shown below.
• 3*0
• 3*1
• 3*2
• 3*3
• 3*4
• 3*5
"""


def drawTable(num, limit):
    for i in range(limit + 1):
        print(num, "*", i, "=", num*i)


try:
    userValue = False
    while not userValue:
        number = (int(input("Please enter time tables for printing:\t")))
        if number < 0:
            print("Invalid input - Your input must be greater than 0 ( zero )")
        else:
            last = (int(input("Please enter upper limit for multiplication:\t")))
            if last < 0:
                print("Invalid input - Your input must be greater than 0 ( zero )")
            else:
                drawTable(number, last)
                userValue = True

except Exception as e:
    print("invalid input - please check input value\n", e)

"""
(ii)
Implement a function called printNumTriangle. The function should ask the user to enter a
single integer. It should then print a triangle of that size specified by the integer so that each
row in the triangle is made up of the integer displayed.
"""


def printNumTriangle():
    try:
        user = False
        while not user:
            singleInt = (int(input("Please enter an integer for triangle size:\t")))
            if singleInt < 0:
                print("Invalid input - Incorrect input, Please check input must be greater than 0 ( zero )")
            else:
                for i in range(singleInt + 1):
                    for k in range(i):
                        print(i, end="")
                    print("\n")
                user = True
    except Exception as e:
        print("!ERROR!\n", e)


printNumTriangle()

"""
(5)
Write a program that asks the user to enter the rainfall for the first X months of the year into a
list, where X is an int value between 1 and 12. (Obtaining the rainfall input from the user
should be done using a loop).
The program should calculate and display:
• The average monthly rainfall
• The highest rainfall value received
• The lowest rainfall value received
"""

ok = False


def calcRainfall(num):
    value = 0
    rainList = []
    for i in range(1, num + 1):
        rainData = (float(input("Please enter rainfall for month " + str(i) + " ")))
        rainList.append(rainData)
        value += rainData
    rainList.sort(reverse=True)
    print("Highest rainfall value:\t", rainList[0])
    rainList.sort()
    print("Lowest rainfall value:\t", rainList[0])
    print("Average is:\t", value / len(rainList))


try:
    while not ok:
        monthNum = (int(input("How many months of data do you wish to enter:\t")))
        if monthNum < 0:
            print("Incorrect input - input must be 0 or greater")
        elif monthNum == 0:
            print("Thanks for using my program")
            ok = True
        elif monthNum > 0:
            calcRainfall(monthNum)
            ok = True
except ValueError:
    print("Invalid input - Please check your input, must be an integer")

"""
(6)
The Fibonacci numbers are the numbers in the following integer sequence:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each
subsequent number is the sum of the previous two.
Create a program that creates a list and will populate it with the first 40 Fibonacci numbers
(this can be done with just three lines of code).
The program should then ask the user to enter an integer value between 1 and 40 to indicate
which number in the Fibonacci series they would like to see and the application should
display that number. For example, if the user enters 13, the 13th number is 144.
"""

fibList = []


def fib(n):
    count = 0
    a, b = 0, 1
    while count < n:
        a, b = b, a + b
        fibList.append(a)
        count += 1


fib(40)
userNumber = int(input("Enter the start number here "))
for i in fibList:
    print(i, " ")
print("Your chose was position: ", userNumber, " this is: ", fibList[userNumber - 1])

"""
(7)
Write a program that will act as a basic calculator for the user. The program should first ask
the user for two separate numerical values. It should then give the user an option to perform
one of four operations: addition, subtraction, division or multiplication. Therefore, if the user
selects multiplication then your program should print out the product of the two values. The
following is sample output from this program.
"""


def checkValue(value, text):
    try:
        ok = False
        while not ok:
            if value.isdigit():
                ok = True
                return int(value)
                break
            else:
                getInput(text)
    except ValueError:
        print("Invalid input - you must enter a numeric value")


def getInput(text):
    valueX = input(text)
    return checkValue(valueX, text)


def displayResult(value1, value2, res, text):
    print(text, " of ", value1, " and ", value2, " is ", res)


def showMenu(choice, value1, value2):
    if choice == 1:
        displayResult(value1, value2, value1 + value2, "Addition")
    elif choice == 2:
        displayResult(value1, value2, value1 - value2, "Subtraction")
    elif choice == 3:
        displayResult(value1, value2, value1 * value2, "Multiplication")
    elif choice == 4:
        displayResult(value1, value2, value1 / value2, "Division")


valueOne = getInput("Please enter a numerical value: ")
valueTwo = getInput("Please enter a numerical value: ")
userChoice = getInput("Would you like to perform:\n1 Addition\n2 Subtraction\n3 Multiplication\n4 Division\n> ")
showMenu(userChoice, valueOne, valueTwo)
