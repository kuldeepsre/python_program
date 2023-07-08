n = 6
k = 4
a = [1, 2, 3, 4, 5, 6]
res = []

for i in range(n - k + 1):
    ''' res.append(a[i:i + k])'''
    subarray = a[i:i + k]
    maxsum = max(subarray)
    res.append(maxsum)

print(max(res))
