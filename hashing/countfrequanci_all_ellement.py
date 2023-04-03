A = [10, 20, 20, 10, 10, 20, 5, 20]
n = len(A)


def findFrequency(A, n):
    mp = dict()

    for i in range(n):
        if A[i] in mp.keys():
            mp[A[i]] += 1
        else:
            mp[A[i]]=1

    for x in mp:
        print(x, " ", mp[x])


findFrequency(A, n)

