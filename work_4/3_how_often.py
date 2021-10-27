from itertools import combinations


string, k = input().split()
k = int(k)

t_indexes = {i for i, s in enumerate(string) if s == 't'}

positions = list(combinations(range(len(string)), k))
result = len(list(pos for pos in positions if any((True for i in pos if i in t_indexes)))) / len(positions)

print(f'{round(result, 3):.3f}')
