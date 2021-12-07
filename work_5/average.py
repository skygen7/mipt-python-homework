count = 0
lines = 0

with open(r'in.txt') as f:
    for line in f:
        count += line.count('a')
        lines += 1

print(count / lines, file=open(r'out.txt', 'w'))
