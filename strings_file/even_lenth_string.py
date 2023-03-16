string_data = "hi how are uoy is"
# output hi is
s = string_data.split(" ")
print(s)
for i in s:
    if len(i) % 2 == 0:
        print(i)
    else:
        print("old string", i)
