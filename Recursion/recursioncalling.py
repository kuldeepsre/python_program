
def printTest(test):
    if test < 1:
        return
    else:
        print(test, end=" ")
        printTest(test - 1)  # statement 2
        print(test, end=" ")
        return


test = 3
printTest(test)
