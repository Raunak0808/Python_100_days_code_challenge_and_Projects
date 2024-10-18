#conversion of tuples
a = ("Oppo", "Redmi", "Oneplus")
print("before conversion",type(a))
print(a)

a = list(a)
a.append("Samsung")
print("after conversion",type(a))
print(a)

a = tuple(a)
print(type(a))

#tuple function
print(a.count("Samsung"))
print(a.index("Redmi"))