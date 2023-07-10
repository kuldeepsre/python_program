A = [2, 3, 4, 5]
N = len(A)
# Last Elemt
lastElement = N - 1
print(A[lastElement])
# display array

for i in range(0, N):
    print("ITEM:", i)
sumOfElement = 0
# summ of array element
A = [2, 3, 4, 5, "3232333"]
for k in range(0, N):
    sumOfElement = sumOfElement + A[k]
print("sumOfElement is :", sumOfElement)

# Reverse the array
print(A[::-1])

"Remove element from array"


def remove_duplicates(array):
    unique_array = []
    for element in array:
        if element not in unique_array:
            unique_array.append(element)

    return unique_array


# Example usage
my_array = [1, 2, 3, 4, 2, 3, 5]
result = remove_duplicates(my_array)
print(result)  # Output: [1, 2, 3, 4, 5]
