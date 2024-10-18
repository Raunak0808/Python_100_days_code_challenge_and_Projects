#take an input from a user as a string, then reverse it.
a = input("Enter anything here: ")
print(a[::-1])

#write a program to check if a string contains only digits
a = input("Enter the value here: ")
print(a.isdigit())

#write a program to check if a string is palindrome
a = input("Enter your string here: ")
rev = a[::-1]
if a == rev:
    print("String is Palindrome")
else:
    print("String is not a palindrome")

#write a program to find a vowels in a string.
a = input("Enter your String here: ")
vowel = 0
for i in a:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowel = vowel + 1
print("Vowels are there",vowel)
    
#write a program to check if every word in a string begins with a capital letter.
a = input("Enter the string: ")
print(a.istitle())

