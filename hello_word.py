print("welcome to Kuldeep")
s1 = "kuldeep"
# Assign a String
a = 10
b = 10.3
print("My name is " + " " + "Kumar")

print(a)
print(b)
print(a - b)
print(b * a)
print(a % b)
message = "I love Python."
print(message)
# Access String Characters in Python
greet = 'hello'

# access 1st index element
print(greet[1])  # "e"
print(greet[0])  # "h"
print("lenth of string ", len(greet))
# access character from 1st index to 3rd index
print(greet[1:4])  # "ell"

greet = 'Hello'

# iterating through greet string
for letter in greet:
    print(letter.islower())
# Check
print('a' in 'program')  # True
print('at' not in 'battle')  # False

# Reverse string
name = "kuldeep kumar"


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


s = "kuldeep kumar"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))
# check string is palindrom or not
x = "ggg4"

w = ""
for i in x:
    w = i + w

if x == w:
    print("yes")

else:
    print("not")


# function to check if two strings are
# anagram or not
def check(s1, s2):
    # the sorted strings are checked
    if sorted(s1) == sorted(s2):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


# driver code
s1 = "listen"
s2 = "silent"
check(s1, s2)
