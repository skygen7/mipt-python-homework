def print_count_debug(foo):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        global DEBUG
        if DEBUG:
            print(count)
        return foo(*args, **kwargs)
    return wrapper
