import functools


def sum_mul(numbers, action):
    if action == '+':
        return sum(numbers)
    if action == '*':
        return functools.reduce(lambda a, b: a * b, numbers)


s = input()
digits = '0123456789'
nums = [int(i) for i in s if i in digits] or [0]
if '+' in s:
    act = '+'
else:
    act = '*'
print(sum_mul(nums, act))
