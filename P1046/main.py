apple_heights = list(map(int, input().split()))  # 读取苹果到地面的高度列表
hand_height = int(input())  # 读取陶陶把手伸直的最大高度

reachable_apples1 = 0  # 记录陶陶能够直接摘到的苹果数目
reachable_apples2 = 0  # 记录陶陶通过踩板凳后能够摘到的苹果数目

for apple in apple_heights:
    if hand_height >= apple:  # 如果陶陶能够直接摘到苹果
        reachable_apples1 += 1

    if hand_height + 30 >= apple:  # 如果陶陶通过踩板凳后能够摘到苹果
        reachable_apples2 += 1

# 输出陶陶能够摘到的苹果数目，取两种方式中的最大值
print(max(reachable_apples1, reachable_apples2))
