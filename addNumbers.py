# calculation is executed from left to right
# numbers are between 0 and 9
# numbers is string type.
# when number is 0 : you should do addiction
# when number is 1 : you should do addiction
# make bigger number by putting plus or time in-between numbers
numbers = "02984"


def addNumbers(numbers):
    leftNumber = int(numbers)[0]
    for number in numbers[1:]:
        number = int(number)
        if leftNumber == 0 or leftNumber == 1 or number == 0 or number == 1:
            print(leftNumber, "+=", number)
            leftNumber += number
        else:
            print(leftNumber, "*=", number)
            leftNumber *= number
    return leftNumber


print(addNumbers(numbers))
