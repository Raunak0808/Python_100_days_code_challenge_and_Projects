#endswith function
a = "Harry Potter and the Prisoner of Azkaban"
print(a.endswith("r"))
print(a.endswith("t",6,9))

#startswith function
print(a.startswith("H"))
print(a.startswith("P",1,9))

#swapcase function
print(a.swapcase())

#strip function
b = "    ****Harry Potter****    "
print(b.strip("*, "))

#split function
c = "#00FD#BRB#OMW#TB"
d = "hello. my name is john. i am 23 years old"
print(c.split("#"))
print(d.split("."))

#ljust function
x = a.ljust(20)
print(x,"is my favourite movie")

#rjust function
y = a.rjust(20)
print(y,"is my favourite movie")

#replace function
print(d.replace("john","lisa"))

#rindex function
print(a.rindex("Prisoner"))

#rfind function
print(a.rfind("Potter"))

#