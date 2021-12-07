res = 0
error = False

with open(r'in.txt') as file:
    for line in file:
        try:
            line = float(line)
        except (TypeError, ValueError):
            error = True
        else:
            res += line

if error:
    res = 'nan'
print(res, file=open(r'out.txt', 'w'))
