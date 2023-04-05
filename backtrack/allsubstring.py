def backtrack_substrings(s, start, path):
    # Base case: we've reached the end of the string
    if start == len(s):
        print(path)
        return

    # Recursive case: we can either include or exclude the current character
    # If we include the character, we add it to the current path
    backtrack_substrings(s, start + 1, path + s[start])
    # If we exclude the character, we leave the current path as is
    backtrack_substrings(s, start + 1, path)


def print_all_substrings(s):
    backtrack_substrings(s, 0, '')


print_all_substrings('abc')
