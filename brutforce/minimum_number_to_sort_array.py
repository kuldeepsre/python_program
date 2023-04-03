# Input: {4, 3, 2, 1}
# Output: 2
# Explanation: Swap index 0 with 3 and 1 with 2 to form the sorted array {1, 2, 3, 4}
#
# Input: {1, 5, 4, 3, 2}
# Output: 2

A = [4, 3, 2, 1]
n = len(A)
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
            count += 1
print("minimum swap require ,", A, count)
