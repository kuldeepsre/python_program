# Python program to sort an array with
# 0, 1 and 2 in a single pass

# Function to sort array


def sort012(a, arr_size):
    l = 0
    r= arr_size - 1
    current = 0
    # Iterate till all the elements
    # are sorted
    while current <= r:
        # If the element is 0
        if a[current] == 0:
            a[l], a[current] = a[current], a[l]
            l = l + 1
            current = current + 1
        # If the element is 1
        elif a[current] == 1:
            current = current + 1
        # If the element is 2
        else:
            a[current], a[r] = a[r], a[current]
            r = r - 1
    return a


# Function to print array


def printArray(a):
    for k in a:
        print(k, end=' ')


# Driver Program
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr_size = len(arr)
arr = sort012(arr, arr_size)
printArray(arr)

# Contributed by Harshit Agrawal
def sort_array(arr):
    counts = [0] * 5
    print(counts) # Initialize counts for values 0 to 4

    # Count the occurrences of each value
    for num in arr:
        counts[num] += 1

    print(counts)
    i = 0
    for value, count in enumerate(counts):
        for _ in range(count):
            arr[i] = value
            i += 1

    return arr

# Example usage:
input_array = [0, 1, 2, 1, 0, 2, 1, 0, 3, 3, 4, 4]
sorted_array = sort_array(input_array)
print(sorted_array)  # Output: [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4]