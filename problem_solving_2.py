#write a program to check number if a number is positive.
a = int(input("Enter the value of a: "))
if a >= 0:
    print("number is positive")
else:
    print("number is negative")

#write a program to check whether a number is odd or even.
a = int(input("Enter the value of a: "))
if a % 2 == 0:
    print("number is even")
else:
    print("number is odd")

#write a program to check whether the passed letter is a vowel or not.
letter = input("Enter the letter: ")
if letter in "aeiou":
    print("it is vowel")
else:
    print("it is not a vowel")

#write a program to check if a number is a single digit number, 2- digit number and so on upto 5 digits.
num = int(input("Enter the number: "))
if num >= 0 and num <= 9:
    print("number is a single digit")
elif num >= 10 and num <= 99:
    print("number is 2- digit number")
elif num >= 100 and num <= 999:
    print("number is 3- digit number")
elif num >= 1000 and num <= 9999:
    print("number is 4- digit number")
elif num >= 10000 and num <= 99999:
    print("number is 5- digit number")
else:
    print("something else")

#write a program to create area calculator.
print("****AREA CALCULATOR****")
print("Press 1 to get area of square")
print("Press 2 to get area of circle")
print("Press 3 to get area of rectangle")
print("Press 4 to get area of triangle")

choice = int(input("Enter the value between 1 to 4: "))
if choice == 1:
    side = float(input("Enter the value of side: "))
    area = side*side
    print("area of square", area)
elif choice == 2:
    radius = float(input("Enter the radius: "))
    area = 3.14*radius*radius
    print("area of circle", area)
elif choice == 3:
    length = float(input("Enter the length of rectangle: "))
    breadth = float(input("Enter the breath of rectangle:"))
    area = length * breadth
    print("area of rectangle", area)
elif choice == 4:
    base = float(input("Enter the base of triangle: "))
    height = float(input("Enter the height of triangle: "))
    area = 1/2*base*height
    print("area of triangle", area)
else:
    print("invalid input")

