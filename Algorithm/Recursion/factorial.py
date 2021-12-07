def findFactorialRecursive(number):
    if number == 1:
        return 1
    return number * findFactorialRecursive(number-1)


def findFactorialIterative(number):
    product = 1
    for i in range(2, number+1):
        product *= i
    return product


print(findFactorialRecursive(10))
print(findFactorialIterative(10))
