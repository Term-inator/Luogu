# 读取输入的整数 n 和 x
n, x = map(int, input().split())

# 初始化计数器
count = 0

# 遍历区间 [1, n] 中的每个整数
for num in range(1, n+1):
    # 将整数转换为字符串，并计算字符串中 x 出现的次数
    count += str(num).count(str(x))

# 输出 x 出现的总次数
print(count)
