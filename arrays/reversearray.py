arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
print(*arr)
print("revesrse array is :\n")


def reverseArr(arr, n):
    if n==1:
        return arr
    else:
        for i in range(0, int(n / 2)):
            arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
            return arr



result =reverseArr(arr,n)
print(*result)