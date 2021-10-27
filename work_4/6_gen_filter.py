def filter7lessN(a, N):
    for i in a:
        if i % 7 == 0 and i < N:
            yield i
