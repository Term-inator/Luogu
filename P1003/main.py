carpets = []

# 输入地毯数量
n = int(input())

# 输入每张地毯的信息
for i in range(1, n + 1):
    # 输入地毯左下角坐标和长度
    a, b, g, k = map(int, input().split())
    carpets.append([a, b, g, k])

# 输入查询点的坐标
x, y = map(int, input().split())

# 初始化结果为-1，表示没有被地毯覆盖
res = -1

# 遍历每张地毯
for i, [a, b, g, k] in enumerate(carpets):
    # 判断查询点是否被当前地毯覆盖
    if a <= x <= a + g and b <= y <= b + k:
        res = i + 1  # 更新结果为当前地毯的编号

# 输出结果
print(res)
