# 从输入中读取两个正整数 L 和 R，表示统计范围 [L, R]
L, R = map(int, input().split())

# 初始化结果变量，用于存储数字 2 出现的总次数
total_occurrences = 0

# 遍历从 L 到 R 的每个整数
for num in range(L, R + 1):
    # 从个位开始逐位分析数字
    while num != 0:
        # 判断当前位是否是数字 2
        if num % 10 == 2:
            # 如果是数字 2，增加出现次数计数
            total_occurrences += 1
        # 去掉已经分析过的最低位
        num //= 10

# 输出数字 2 在范围内出现的总次数
print(total_occurrences)
