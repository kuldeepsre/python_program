s = "sferfwerwrwerrtt"
l = []

for ch in s:

    if ch not in l:
        l.append(ch)

for ch in sorted(l):
    print('{} occurs {} times'.format(ch, s.count(ch)))
# secondary dictionary

d = {'A': 100, 'B': 300}
d.get('A')
print(d)
print(d.get('x'))
print(d.get('x',220))
d['A']=d.get('A',2)+1
print(d)

#printing for each items in list

for K,V  in d.items():
    print(K,V)
#back to program


s="hrfhewuirweufuhewrhw"
result=''
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1

for K,V in sorted(d.items()):
    print(K,V)
    result=result+str(V)+K
print(result.title())