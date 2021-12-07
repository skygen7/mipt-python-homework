import functools


def logger(file):
    def decorator(foo):
        @functools.wraps(foo)
        def wrapper(*args, **kwargs):
            res = foo(*args, **kwargs)
            print(f'{foo.__name__}:{res}', file=open(file, 'a'))
        return wrapper
    return decorator
