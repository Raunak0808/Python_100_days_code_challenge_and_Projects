a = ["Thor","Hulk","Ironman","Captain America"]
print(a)
#to find the length of a list
print(len(a))

#to count an occurence of a particular element
a = ["Thor","Hulk","Ironman","Captain America","Hulk"]
print(a.count("Hulk"))

#to add to a list
a.append("Superman")
print(a)

#to add to a specific location
a.insert(1,"Spiderman")
print(a)

#to remove from a list
a.remove("Superman")
print(a)

#to remove from a certain location
a.pop(5)
print(a)