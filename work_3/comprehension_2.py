m, n = list(map(int, input().split()))
print(min(map(lambda x: -x ** 5 - (5 * (x ** 4)) + 8 * (x ** 3) + 12 * (x ** 2) + 30 * x + 11, range(m, n + 1))))
