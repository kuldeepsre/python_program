str = "hellow"
print(len(str))


# without using len function


def recursiveLench(str):
    count = 0
    for i in str:
        count += 1
    return count


print(recursiveLench(str))
