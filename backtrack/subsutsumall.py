def sum_of_subsets(arr, K):
    n = len(arr)
    res = [0]

    def backtrack(start, k, subset_sum):
        if k == K:
            res[0] += subset_sum
            return
        for i in range(start, n):
            backtrack(i + 1, k + 1, subset_sum + arr[i])

    backtrack(0, 0, 0)
    return res[0]


arr = [1, 2, 3, 4]
K = 2
result = sum_of_subsets(arr, K)
print(result)  # Output: 20
