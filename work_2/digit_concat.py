def dig_concat(n, k):
    return sum(int(str(n) * i) for i in range(1, k + 1))


print(dig_concat(int(input()), int(input())))
