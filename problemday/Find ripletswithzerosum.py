arr = [1, 3, 2, -2, -1, -3, 5]


def findtriplet(arr):
    triplets = []
    size = len(arr)
    right = size - 1
    print(arr[right])
    arr.sort()
    print(arr)
    for i in range(size - 2):
        # Skip duplicates to avoid duplicate triplets
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = size - 1
        while left < right:
            tripletsum = arr[i] + arr[left] + arr[right]
            if tripletsum < 10:
                left = left + 1
            elif tripletsum > 10:
                right = right - 1
            else:
                triplets.append((arr[i], arr[left], arr[right]))
                # Skip duplicates to avoid duplicate triplets
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return triplets


output = findtriplet(arr)
print(output)
