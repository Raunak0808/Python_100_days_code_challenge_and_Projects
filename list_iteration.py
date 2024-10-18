#Iteration using for loop
a = ["Thor","Hulk","Captain America","Ironman"]
for i in a:
    print(i)

#Iteration using for loop with range and length function
for i in range(len(a)):
    print(a[i])

#iteration using while loop
i = 0
while i < len(a):
    print(a[i])
    i = i + 1

#using short hand for loop
[print(i) for i in a]