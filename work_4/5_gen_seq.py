from random import choice


def genseq(alphabet, length):
    while True:
        yield ''.join(choice(alphabet) for _ in range(length))
