from itertools import groupby
from collections.abc import Iterable


def generator(args):
    for i in args:
        if isinstance(i, Iterable):
            w, group = tuple(i)
            count = len(tuple(group))
            if count > 1:
                yield from (w, str(count))
            else:
                yield w
        else:
            yield i


print(''.join(generator(groupby(input()))))
