#syntax of functions
def hello():
    print('Hello World!')

hello()

#parameters and arguements
def add(x,y):
    print(x + y)

add(4,7)

#arbitrary arguements
def hello(*name):
    print('My name is',name[1])

hello('John','Lisa','Peter','Lizael')

#factorial using function
def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n - 1))
    
print(fact(5))

#lambda function
a = lambda b: b * 5
print(a(4))