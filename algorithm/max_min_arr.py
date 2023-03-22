def max_min_sliding_window(arr, window_size):
    max_values = []
    min_values = []

    # Initialize the first window
    window = arr[:window_size]
    max_values.append(max(window))
    min_values.append(min(window))

    # Slide the window and update max and min values
    for i in range(window_size, len(arr)):
        window = arr[i - window_size + 1:i + 1]
        max_values.append(max(window))
        min_values.append(min(window))

    return max_values, min_values


arr = [1, 3, -1, -3, 5, 3, 6, 7]
window_size = 3

max_vals, min_vals = max_min_sliding_window(arr, window_size)

print("Maximum values:", max_vals)
print("Minimum values:", min_vals)
