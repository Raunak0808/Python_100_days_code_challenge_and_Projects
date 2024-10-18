#write a program to get fibonacci series upto 10 numbers
a = 0
b = 1
n = int(input("Enter the number: "))
if n == 1:
    print(1)
else:
    print(a)
    print(b)
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)

#write a program to check if a number is prime or not
num = int(input("Enter the number: "))
if num <= 1:
    print("It is not Prime Number")
else:
    for i in range(2,num):
        if num % i == 0:
            print("It is not Prime Number")
            break
        else:
            print("It is a Prime Number")
            break
        
#write a program to find a palindrome of Integers
num = int(input("Enter the number: "))
temp = num
rev = 0
while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if rev == temp:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")

#write a program to create an area calculator
print("****AREA CALCULATOR****")
while True:
    print("Press 1 to get area of square")
    print("Press 2 to get area of circle")
    print("Press 3 to get area of rectangle")
    print("Press 4 to get area of triangle")

    choice = int(input("Enter the value between 1 to 4: "))
    if choice == 1:
        while True:
            side = float(input("Enter the value of side: "))
            area = side*side
            print("area of square", area)
            repeat = input("Do you want to try again with square?")
            if repeat == "no":
                break
    elif choice == 2:
        while True:
            radius = float(input("Enter the radius: "))
            area = 3.14*radius*radius
            print("area of circle", area)
            repeat = input("Do you want to try again with circle?")
            if repeat == "no":
                break
    elif choice == 3:
        while True:
            length = float(input("Enter the length of rectangle: "))
            breadth = float(input("Enter the breath of rectangle:"))
            area = length * breadth
            print("area of rectangle", area)
            repeat = input("Do you want to try again with rectangle?")
            if repeat == "no":
                break
    elif choice == 4:
        while True:
            base = float(input("Enter the base of triangle: "))
            height = float(input("Enter the height of triangle: "))
            area = 1/2*base*height
            print("area of triangle", area)
            repeat = input("Do you want to try again with triangle?")
            if repeat == "no":
                break
    else:
        print("invalid input")

    repeat1 = input("Do you want to repeat again?")
    if repeat1 == "no":
        break