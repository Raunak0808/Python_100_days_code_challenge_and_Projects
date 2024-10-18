#write a function to find the maximum of three numbers in python
def max(x,y,z):
    if x > y and x > z:
        print('X is greater',x)
    elif y > x and y > z:
        print('Y is greater',y)
    else:
        print('Z is greater')
max(3,6,9)

#write a function to create and print a list where the values are a square of numbers between 1 and 30
def create_list():
    l = []
    for i in range(1,31):
        l.append(i**2)
    return l
print(create_list())

#write a python function that takes number as a parameter and check if the number is prime or not
def check_prime(x):
    if x == 1:
        print('It is not a prime number')
    elif x == 2:
        print('It is a prime number')
    elif x > 2:
        for i in range(2,x):
            if x % i == 0:
                print('It is not a prime number')
                break
        else:
            print('It is a prime number')
check_prime(5)

#write a python function to sum all the numbers in a list
def sum(x):
    total = 0
    for i in x:
        total = total + i
    return total
print(sum([10,20,30,40]))

#using recursion
def sum(num):
    if len(num) == 1:
        return (num[0])
    else:
        return (num[0] + sum(num[1:]))

print(sum([10,20,30,40]))

#write a program to solve the fibonacci sequence using recursion
def fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return (fibonacci(num - 1) + fibonacci(num - 2))
    
print(fibonacci(7))
    

    
