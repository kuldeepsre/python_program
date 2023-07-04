# Example usage:
num = 153


def is_armstrong_number(number):
    return sum(int(d) ** len(str(number)) for d in str(number)) == number


if is_armstrong_number(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
