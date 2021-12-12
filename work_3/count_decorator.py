def call_count(foo):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        return foo(*args, **kwargs)
    return wrapper
