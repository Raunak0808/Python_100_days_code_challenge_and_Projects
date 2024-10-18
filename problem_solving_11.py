#write a python program to sort a dictionary by value
a = {'a':10,'b':20,'c':30}
a = sorted(a.values())
print(a)

#write a python script to print a dictionary where the keys are numbers between 1 and 15 and the values are square of keys
a = {}
for i in range(1,16):
    a[i] = i * i
print(a)

#write a program to multiply all the items in a dictionary
a = {'a':10,'b':20,'c':30,'d':40}
product = 1
for i in a:
    product = a[i] * product

print(product)

#write a python program to sort a dictionary by key
a = {'b':10,'z':100,'a':1,'c':20}
a = sorted(a.keys())
print(a)
