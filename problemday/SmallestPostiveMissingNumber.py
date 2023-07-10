#naviv approch
arr = {-1,1,2,3,4,5}
sorted(arr)
for i in range(1,10):
    if i not in  arr:
        print(i)

        break
#kth missing number
K=15
A={1,2,4,5,6,19}
N=max(A)

l=[]
count=K

for i in range(1,N):
     if i not in A:
         K=K-1
         l.append(i)
         if(K==0):
             break
print(l)
print(l[K-1])
#
# #        b = arr
#         hash = set(b)
#         for i in range(1, n + k):
#             if i not in hash:
#                 return i
