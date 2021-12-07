with open(r'input.txt') as f:
    m, n, k = map(int, f.readline().split())
    res = [i for i in range(m, n + 1) if i % k == 2]
    for i in res:
        print(i)
