def reverseInteger(number):
    isNegative = False
    if number < 0:
        isNegative = True
        number *= -1
    flipped = 0
    while number > 0:
        flipped = flipped * 10 + number % 10
        number /= 10
    if isNegative:
        return -1 * flipped
    else:
        return flipped

print reverseInteger(-1560)