def is_anagram(str1, str2):
    # Remove any whitespace and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False

    # Create dictionaries to count the frequency of characters in both strings
    char_count1 = {}
    char_count2 = {}

    # Count the frequency of characters in the first string
    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1

    # Count the frequency of characters in the second string
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1

    # Compare the character frequencies
    return char_count1 == char_count2
string1 = "listen"
string2 = "silent"
print(is_anagram(string1, string2))  # Output: True

string3 = "hello"
string4 = "world"
print(is_anagram(string3, string4))  # Output: False