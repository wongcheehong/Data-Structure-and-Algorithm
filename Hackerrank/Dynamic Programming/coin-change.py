import copy


def getAllTheWays(n: int, c: list[int], memo) -> int:
    if n in memo:
        return copy.deepcopy(memo[n])
    if n == 0:
        return [[]]
    if n < 0:
        return []  # No ways

    result = []
    for coin in c:
        possibleWays = getAllTheWays(n-coin, c, memo)
        if possibleWays:
            for way in possibleWays:
                way.append(coin)
                way.sort()
                if way not in result:
                    result.append(way)

    memo[n] = copy.deepcopy(result)
    return result  # This return all the possibleWays


def getWays(n: int, c: list[int]) -> int:
    result = getAllTheWays(n, c, {})
    return len(result)


# n = int(input().split()[0])
# c = [int(x) for x in input().split()]
n = 10
c = [2, 5, 3, 6]
# n = 85
# c = [50, 10, 17, 21, 8, 3, 12, 41, 9, 13, 43, 37,
#      49, 19, 23, 28, 45, 46, 29, 16, 34, 25, 2, 22, 1]
print(getWays(n, c))
