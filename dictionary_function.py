#dictionary functions
employee_data = {"name":"Radha","age":24,"gender":"Female","emp_id":41132}
print(type(employee_data))

#get function
x = employee_data.get("emp_id")
print(x)

#items function
a = employee_data.items()
print(a)

#keys function
b = employee_data.keys()
print(b)

#values function
c = employee_data.values()
print(c)

#copy function
d = employee_data.copy()
print(d)