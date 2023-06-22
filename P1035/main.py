# 输入整数 k
k = int(input())

# 初始化和与计数变量
sum = 0
n = 0

# 循环直到和大于 k
while sum <= k:
    # 增加计数
    n += 1
    # 累加当前项的倒数到和中
    sum += 1 / n

# 输出最小的 n
print(n)
