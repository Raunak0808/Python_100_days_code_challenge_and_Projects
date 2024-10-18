#write a program to find a sum of all the even numbers up to 50.
sum = 0
for i in range(1,51):
    if i % 2 == 0:
        sum = sum + i
print(sum)

#write a program to write first 20 numbers and their squared numbers.
for i in range(1,21):
    square = i ** 2
    print(i, "x", i, "=",square)

#write a program to find the sum of first 10 odd numbers using while loop.
sum = 0
n = 0
while n <= 20:
    if n % 2 != 0:
        sum = sum + n
    n = n + 1
print(sum)

#write a program to check if a number is divisible by 8 and 12, upto 100 numbers.
for i in range(1, 101):
    if i % 8 == 0 and i % 12 == 0:
        print(i)

#write a program to create a billing system at supermarket.
while True:
    name = input("Enter Customer's name: ")
    total = 0
    while True:
        amount = float(input("Enter the amount: "))
        quantity = int(input("Enter the quantity: "))
        total += (amount * quantity)
        repeat = input("Do you want to add more items? (Yes/No)")
        if repeat == "No" or repeat == "no":
            break
    print("-" * 40)
    print("Name: ", name)
    print("Amount to be paid: ", total)
    print("-" * 40)
    print("******Happy Shopping******")
    repeat1 = input("Do you want to move to next customer? (Yes/No)")
    if repeat1 == "No" and repeat == "no":
        break



    

