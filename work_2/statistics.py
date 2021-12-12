import statistics

data = list(map(int, input().split()))
k = int(input())


def stats_moment(array, moment=1):
    m = len(array)
    mean = statistics.mean(array)
    res = 1 / m * sum(((i - mean) ** moment for i in array))
    return res


def main(data, k):
    mean = statistics.mean(data)
    moment = stats_moment(data, moment=k)
    return f'{mean} {moment}'


print(main(data, k))
