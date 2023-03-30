arr = [20, 30, 40, 40, 20, 10]




def findFirstLast(A):
    n = len(arr)
    key = 40
    temp = []
    for i in range(n):
        if key in A[i]:
            print(i)
            temp.append(i)
        else:
            return "not found"
    return temp[0]



result = findFirstLast(arr)
print(result)
