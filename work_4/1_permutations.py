from itertools import permutations

print(' '.join(sorted(''.join(i) for i in permutations(input(), 2))))
