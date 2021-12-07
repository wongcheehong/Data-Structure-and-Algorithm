
def firsRecurringCharacter(array: list[int]) -> int | None:
    seenBefore = {}
    for char in array:
        if char in seenBefore:
            return char
        else:
            seenBefore[char] = True

    return None


a = [2, 5, 5, 2, 3]
print(firsRecurringCharacter(a))

# Fibonaci function

