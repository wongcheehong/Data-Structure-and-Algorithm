def fibonacciIterative(n):
    array = [0, 1]
    for i in range(2, n+1):
        array.append(array[i-1] + array[i-2])

    return array[n]


def fibonacciRecursive(n):
    if n < 2:
        return n
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)


print(fibonacciRecursive(10))
print(fibonacciIterative(10))
