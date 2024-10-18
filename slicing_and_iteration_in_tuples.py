#slicing in tuples
a = ("Samsung", "Apple", "Lenovo", "Vivo", "oppo", "OnePlus", "Redmi")
print(type(a))
print(a)
print(a[:2])
print(a[2:])
print(a[2:5])
print(a[0:5:2])
print(a[1::2])
print(a[::-1])
print(a[2::-1])

#iteration in tuples
#with for loop
a = ("Samsung", "Apple", "Lenovo", "Vivo", "oppo", "OnePlus", "Redmi")
for i in a:
    print(i)

#along with range and length in for loop
for i in range(len(a)):
    print(a[i])

#along with while loop
i = 0
while i < len(a):
    print(a[i])
    i = i + 1 