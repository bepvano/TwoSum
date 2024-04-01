x = [5, 6, 3, 2, 8, 11, 12, 23]
target = 35


def twoSum(x, target):
    for a in range(len(x) - 1):
        for b in range(a + 1, len(x)):
            if target == x[a] + x[b]:
                answer = str(a) + 'и' + str(b)
    return answer


print(twoSum(x, target))
