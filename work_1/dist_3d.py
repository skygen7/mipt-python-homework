a = list(map(float, input().split()))
b = list(map(float, input().split()))

print(round(((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2) ** 0.5, 6))
