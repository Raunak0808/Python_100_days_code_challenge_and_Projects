#In-built modules

#datetime Function
import datetime
x = datetime.datetime.now()
print(x)

y = datetime.datetime(1997,5,15)
print(y)

z = datetime.datetime.now()
print(z.year)
print(z.strftime('%A'))

#Random Function
import random
x = random.randint(1,100)
print(x)

y = ["Heads","Tails"]
z = random.choice(y)
print(z)

#Math Function
import math
x = max(10,20,30)
print(x)
y = min(10,20,30)
print(y)
z = pow(2,3)
print(z)
w = math.sqrt(16)
print(w)
a = abs(-1)
print(a)

#ceil Function
k = math.ceil(2.4)
print(k)

#floor function
m = math.floor(2.4)
print(m)