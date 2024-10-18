#local variable
x = 24
print("First Variable",x)            
def hello():
    x = 25
    return x
print(hello())

print(x)

#global variable
x = 24
print("First Variable",x)            
def hello():
    global x
    x = 25
    return x
print(hello())

print(x)