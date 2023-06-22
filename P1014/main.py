# 读取输入
n = int(input())

# 处理特殊情况，当 n 等于 1 时，直接输出结果为 "1/1"
if n == 1:
    print('1/1')
else:
    row = 0  # 当前行数
    total_sum = 0  # 前 row-1 行的总数
    for row in range(1, n):
        total_sum += row
        if total_sum >= n:
            total_sum -= row
            break

    offset = n - total_sum  # 在当前行中的偏移量
    if row % 2 == 0:
        # 如果当前行为偶数行，则结果为 offset / (row - (offset - 1))
        # 注意分母中的 offset 需要减去 1，因为在当前行中的偏移量不包括第一个元素
        print(f'{offset}/{row - (offset - 1)}')
    else:
        # 如果当前行为奇数行，则结果为 (row - (offset - 1)) / offset
        # 注意分子中的 offset 需要减去 1，因为在当前行中的偏移量不包括第一个元素
        print(f'{row - (offset - 1)}/{offset}')
