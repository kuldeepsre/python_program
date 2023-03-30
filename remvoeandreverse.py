def remove_and_reverse(s):
    seen = set()
    for i in range(len(s)):
        if s[i] in seen:
            s = s[:i] + s[i + 1:]
            return remove_and_reverse(s[::-1])
        seen.add(s[i])
    print(seen)

    return s


# Example usage
s = "leet code"
final_string = remove_and_reverse(s)
print(final_string)
