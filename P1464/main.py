# 定义一个字典 mem 用于存储计算结果，避免重复计算
mem = {}


def w(a, b, c):
    # 如果 a、b、c 中有任意一个小于等于 0，则返回 1
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    # 如果 a、b、c 中有任意一个大于 20，则返回 w(20, 20, 20)
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    # 如果 (a, b, c) 已经在 mem 中存在，直接返回结果
    if (a, b, c) in mem:
        return mem[(a, b, c)]

    res = 0
    # 如果 a < b < c，则根据条件计算结果
    if a < b < c:
        res = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    # 其他情况下，根据条件计算结果
    else:
        res = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

    # 将计算结果存储在 mem 中
    mem[(a, b, c)] = res
    return res


# 读取输入并进行计算，直到输入为 -1,-1,-1
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
