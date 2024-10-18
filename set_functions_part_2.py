a = {'Switzerland','New Zealand','Australia','USA','India','Russia'}
b = {'India','South Korea','Japan','USA','Azerbaijan'}
c = {'Azerbaijan','Russia','Ukraine','Australia','South Korea'}

#Using IsDisjoint function
print(b.isdisjoint(a))

#Using IsSubset Function
print(c.issubset(a))

#Using IsSuperset Function
print(a.issuperset(c))

#Using Update method
a.update(c)


#Union function
x = a.union(c)
print(x)

#difference function
print(a.difference(b))

#difference update function
print(a.difference_update(b))

#intersection function
print(a.intersection(c))

#intersection_update function
print(a.intersection_update(b))

#symmetric difference function
x = a.symmetric_difference(c)
print(x)

#symmetric difference update
a.symmetric_difference_update(b)
print(a)





