#iteration in dictionaries
employee_data = {"name":"John","age":24,"gender":"male"}
print(employee_data["gender"])


#printing all the key names one by one
for i in employee_data:
    print(i)

#printing all the values one by one
for x in employee_data:
    print(employee_data[x])

#using value function
for x in employee_data.values():
    print(x)
    
#using items function
for x,y in employee_data.items():
    print(x,":",y)