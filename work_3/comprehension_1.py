m, n, k = list(map(int, input().split()))
print(sum(x for x in range(m, n + 1) if x % k == 2))
