from time import perf_counter


def print_time(foo):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        res = foo(*args, **kwargs)
        end = perf_counter()
        print(end - start)
        return res
    return wrapper
