# 读取输入
n, m, k = map(int, input().split())

# 创建一个二维列表，用于记录每个人每天有空的模拟赛题目编号
time_sheet = [[False for _ in range(m)] for _ in range(k)]

# 读取每个人的时间安排
for _ in range(n):
    days = list(map(int, input().split()))
    for i in range(m):
        day = days[i]
        time_sheet[day - 1][i] = True

# 创建一个列表，用于记录每天需要准备的模拟赛场数
prep_count = [0] * k

# 统计每天需要准备的模拟赛场数
for i in range(k):
    for j in range(m):
        if time_sheet[i][j]:
            prep_count[i] += 1

# 输出结果
print(*prep_count)
