road_length, num_regions = map(int, input().split())

trees = [1 for _ in range(road_length + 1)]  # 初始化马路上的树木列表，初始值为1（表示有树）

for _ in range(num_regions):
    start, end = map(int, input().split())  # 区域的起始点和终止点
    for i in range(start, end + 1):
        trees[i] = 0  # 将该区域内的树木标记为0（表示没有树）

remaining_trees = trees.count(1)  # 计算马路上剩余的树木数量

print(remaining_trees)
