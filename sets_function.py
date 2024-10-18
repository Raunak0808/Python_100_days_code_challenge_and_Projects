a = {'Ironman','Captain America','Hulk','Thor'}

#to add an element in a set
a.add('Spiderman')
print(a)

#to pop an element from a set
a.pop()
print(a)

#to remove an element from a set
a.remove('Captain America')
print(a)

#to discard an element
a.discard('Hulk')
print(a)

#to copy an elements of a set
b = a.copy()
print(b) 