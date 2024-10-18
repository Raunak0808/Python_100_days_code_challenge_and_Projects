#if_elif_else_statement
marks = int(input("Enter the marks: "))
if marks >= 90:
    print("You'll get a Laptop")
elif marks >= 80 and marks < 90:
    print("You'll get a phone")
else:
    print("You'll get a treat")
print("Congrats!!")