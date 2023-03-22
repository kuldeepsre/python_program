# Sliding windows are a common technique used in signal processing,
# image processing, and machine learning. In Python,
# sliding windows can be implemented using various libraries,
# including NumPy and TensorFlow.
#
# Here is an example of implementing sliding windows in Python using NumPy:

# Example usage
arr = [32, 49, 49, 30, 50]
# op/0 [32, 49, 49],[49, 49, 30],[49, 30, 50]
size = len(arr)
wondows_size = 23


def sliding_window(a, n, k):
    res = []
    if n < k:
        return "invaild windows size"

    for i in range(n - k + 1):
        res.append(a[i:i + k])

    return res


result = sliding_window(arr, size, wondows_size)
print("result ", result, end=" ")
