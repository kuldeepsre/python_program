# Python3 code to demonstrate working of
# Longest String in list
# using recursive function

# defining recursive function
def find_maximum(lst, start=0, max_word=''):
    if start == len(lst):  # base condition
        return max_word
    if len(lst[start]) > len(max_word):
        max_word = lst[start]
    return find_maximum(lst, start + 1, max_word)  # calling recursive function


# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks','ssssr']

# printing original list
print("The original list : " + str(test_list))

# Longest String in list
# using recursive function
res = find_maximum(test_list)

# printing result
print("Maximum length string is : " + res)
# This code is contributed by tvsk
# Python3 code to demonstrate working of
# Longest String in list
# using loop

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# Longest String in list
# using loop
max_len = -1
for ele in test_list:
    if len(ele) > max_len:
        max_len = len(ele)
        res = ele

# printing result
print("Maximum length string is : " + res)