n, m = map(int, input().split())


class Toy:
    def __init__(self, direction, name):
        self.direction = int(direction)  # 玩具小人的朝向，0表示朝向圈内，1表示朝向圈外
        self.name = name  # 玩具小人的职业


toys = []  # 逆时针顺序
for i in range(n):
    direction, name = input().split()
    toys.append(Toy(direction, name))

current_index = 0  # 当前所在玩具小人的索引
for i in range(m):
    direction, offset = map(int, input().split())
    current_toy = toys[current_index]  # 当前所在玩具小人
    if current_toy.direction == 0:  # 当前所在玩具小人朝向圈内
        if direction == 0:  # 指令为向左数人
            current_index = (current_index - offset) % n
        else:  # 指令为向右数人
            current_index = (current_index + offset) % n
    else:  # 当前所在玩具小人朝向圈外
        if direction == 0:  # 指令为向左数人
            current_index = (current_index + offset) % n
        else:  # 指令为向右数人
            current_index = (current_index - offset) % n

print(toys[current_index].name)  # 输出最终到达的玩具小人的职业
