#Project - 2 - Tip Calculator

print("*****Project - 2 - Tip Calculator*****")
print("Welcome to Tip Calculator!")

bill_amount = float(input("What was the total bill?: $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12 or 15?"))
number_of_people = int(input("How many people to split the bill?"))

total_amount = (bill_amount*tip_percentage)/100 + bill_amount
amount_to_be_split = total_amount/number_of_people
print("Each person should pay:$",amount_to_be_split)