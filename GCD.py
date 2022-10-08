# get Greatest Common Divider of 2 numbers
# GCD of a and b, is the same as GCD of Remainder of a divided by b. (a > b)
def getBigger(a, b):
    if a - b >= 0:
        return a, b
    else:
        return b, a


def getGCD(a, b):
    x, d = getBigger(a, b)
    r = x % d

    if r == 0:
        return d
    else:
        return getGCD(d, r)


print(getGCD(2, 3))
