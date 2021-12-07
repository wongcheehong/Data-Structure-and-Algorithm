def getWays(n: int, c: list[int]) -> int:
    ways = [0 for _ in range(n + 1)]
    ways[0] = 1

    for i in range(len(c)):
        # Start from c[i] to n inclusive where i start from 0 to len(c)
        for j in range(c[i], n + 1):
            ways[j] += ways[j - c[i]]

    return ways[n]


n = 85
c = [50, 10, 17, 21, 8, 3, 12, 41, 9, 13, 43, 37,
     49, 19, 23, 28, 45, 46, 29, 16, 34, 25, 2, 22, 1]

print(getWays(n, c))
