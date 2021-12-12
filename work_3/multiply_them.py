answer = lambda x: -x * answer(x - 1) if x % 3 == 0 else x * answer(x - 1) if x > 1 else x
print(answer(int(input())))
