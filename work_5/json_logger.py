import functools
import json


def jsonlogger(file):
    def decorator(foo):
        @functools.wraps(foo)
        def wrapper(*args, **kwargs):
            res = foo(*args, **kwargs)
            dump = {
                'name': foo.__name__,
                'args': args,
                'kwargs': kwargs,
                'return': res
            }
            record = json.dumps(dump)
            print(record, file=open(file, 'a'))

        return wrapper
    return decorator
