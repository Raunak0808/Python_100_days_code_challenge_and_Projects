#write a program to swap first and fourth element
A = ["Ross","Rachel","Monica","Joe"]
A[0],A[3] = A[3],A[0]
print(A)

#write a program to add a new value at second position
A = ["Ross","Rachel","Monica","Joe"]
A.insert(1,"Raunak")
print(A)

#write a program to delete a value from third position
A.pop(2)
print(A)

#write a program to multiply all the numbers in the list
b = [13,7,12,10]
mul = 1
for i in b:
    mul = mul * i
print(mul)

#write a program to get the largest number from the list
b.sort()
print(b)
print("The largest value in the list is",b[-1])

#write a program to get the smallest number from the list
b.sort()
print(b)
print("The smallest value in the list is",b[0])