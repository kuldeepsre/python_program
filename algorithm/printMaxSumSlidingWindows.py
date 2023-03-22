arr = [23, 3, 45, 23, 34, 34, 45]
windows_size = 3
n = len(arr)


# o/p 45,45,45,34,45

def max_sum_sliding_window(arr,n, window_size):
    window_sum = sum(arr[0:window_size])
    list =[]
    max_sum=window_sum
    for i in range(window_size,n):
        window_sum+= arr[i] - arr[i - window_size]
        list.append(window_sum)
        max_sum = max(list)

    return max_sum


result = max_sum_sliding_window(arr, n, windows_size)
print(result)
