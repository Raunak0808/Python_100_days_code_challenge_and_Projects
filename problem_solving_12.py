#write a program to find max and min in a set.
a = {2,4,6,7,8}
minimum = min(a)
maximum = max(a)
minimum = print('The minimum number in set a is',minimum)
maximum = print('The minimum number in set a is',maximum)

#write a program to find common elements in three lists using sets.
p = [3,4,5,6,7]
q = [1,2,3,4,5]
r = [2,3,4,5,6]

print(set(p) & set(q) & set(r))

#write a program to find difference between two sets.
a = {'Delhi','Gurugram','NCR','Faridabad','Rajendranagar'}
b = {'Patna','Boring Road','Bailey Road','Rajendranagar','Kankarbagh'}
x = a.difference(b)
print(x)

#write a program to remove an item from a set if it is present in a set.
z = {'London','Paris','South Korea','Japan','Australia'}
t = z.discard('Australia')
print(z)

#write a program to check if a set is subset of another set.
a = {'Delhi','Gurugram','NCR','Faridabad','Rajendranagar'}
b = {'Patna','Boring Road','Bailey Road','Rajendranagar','Kankarbagh'}
h = a.issubset(b)
print(h)
