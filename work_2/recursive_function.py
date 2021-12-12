def recursive(n):
    if n < 40:
        return n
    else:
        return recursive(n - 40) + recursive(n - 20) + recursive(n - 5) + recursive(n - 1)


print(recursive(int(input())))
