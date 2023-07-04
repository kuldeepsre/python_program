n = 1
x = str(n)
a = list(map(int, x))
b=sum(a)
print(b)
a.append(b)
c = 0
for i in a:
    if n % i == 0:
        c += 1
if c == len(a):
    print("Yes")
else:
    print("No")
