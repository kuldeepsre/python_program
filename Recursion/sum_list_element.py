number = [20, 39, 40, 40]
sum = 0
for s in number:
    sum += s

print("the sum is", sum)


def sumOfList(list, size):
    if size == 0:
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)


# Driver code
total = sumOfList(number, len(number))

print("Sum of all elements in given list: ", total)

# # range functions
# x = range(6)
# print(x)
# for i in x:
#     print(i,end=' ')
#
# # create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:
y = range(3, 20, 2)
for n in y:
    print(n,end=' ')
