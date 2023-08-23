WIN = 1
LOSE = -1
EVEN = 0

def reverse(state):
    if state == EVEN:
        return EVEN
    if state == WIN:
        return LOSE
    if state == LOSE:
        return WIN

state_map = [
    [EVEN, LOSE, WIN,  WIN,  LOSE],
    [None, EVEN, LOSE, WIN,  LOSE],
    [None, None, EVEN, LOSE, WIN],
    [None, None, None, EVEN, WIN],
    [None, None, None, None, EVEN],
]

# 读取输入
N, Na, Nb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

score_a, score_b = 0, 0
for i in range(N):
    i_a = i % Na  # 小 A 当前周期的索引
    i_b = i % Nb  # 小 B 当前周期的索引
    state_a = a[i_a]  # 小 A 当前出拳
    state_b = b[i_b]  # 小 B 当前出拳

    state = state_map[state_a][state_b]  # 判断当前出拳的胜负关系
    if state == None:
        state = reverse(state_map[state_b][state_a])  # 如果没有定义胜负关系，则取反
    if state == WIN:
        score_a += 1  # 小 A 胜利，得分加 1
    elif state == LOSE:
        score_b += 1  # 小 B 胜利，得分加 1

# 输出得分
print(score_a, score_b)
