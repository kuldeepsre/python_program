# You are given an array A of size N. Let us denote S as the
# sum of all integers present in the array.
# Among all integers present in the array,
# find the minimum integer X such that S ≤ N*X.

#BrutForce


def findMinimum(arr, S, N):
    list = []
    for i in range(N):
        print(arr[i])
        m = arr[i] * N

    if S <= m:
        list.append(arr[i])
        minmum = min(list)

        return minmum


arr = [1, 3, 2]
N = len(arr)

S = sum(arr)

result = findMinimum(arr, S, N)

print("Minimum Integer \n ", result)
