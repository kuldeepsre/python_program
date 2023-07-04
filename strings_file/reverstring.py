myname = input("enter string : ")
split = myname.split()[::-1]
l = []

for i in split:
    l.append(i)
print(l)
print(" ".join(l))
reversestring = "".join(l)
if myname == reversestring:
    print("palindrome")
else:
    print("not palindrome")

