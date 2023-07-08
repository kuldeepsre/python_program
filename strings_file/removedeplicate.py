
s =input("enter string")

result=''
for ch in s:
    if ch not in result:
        result=result+ch
print("Remvie Duplicate elemet " ,ch)

# Second way
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)

print("".join(l))
# using set
s="kjjkjferjjertje"
s1=set(s)
print("Set remove","".join(s1))