#nested_if_statement
marks = int(input("Enter the marks: "))
if marks >= 80:
    print("You'll get a treat")
    if marks >= 90:
        print("You'll get a phone")
else:
    print("You'll get nothing")
print("Thanks!!")