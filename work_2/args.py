def find_even(*args):
    res = [i for i in args if i % 2 == 0]
    if not res:
        return 'Not found'
    return res


print(find_even(*map(int, input().split())))
