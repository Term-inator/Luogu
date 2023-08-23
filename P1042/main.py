game_end = False  # 标志比赛是否结束


def check_game(score, format):
    low = min(score[-1])  # 比分最低分
    high = max(score[-1])  # 比分最高分
    if high >= format and high - low >= 2:  # 如果最高分达到规定分数并且分差大于等于2
        score.append([0, 0])  # 开始新的一局比赛


score_11 = [[0, 0]]  # 记录11分制下的比分
score_21 = [[0, 0]]  # 记录21分制下的比分
while not game_end:  # 当比赛未结束时循环
    s = input()  # 输入比赛信息
    for c in s:  # 遍历比赛信息中的每个字符
        if c == 'E':  # 如果字符为'E'，表示比赛结束
            game_end = True  # 将比赛结束标志设为True
            break  # 跳出循环
        if c == 'W':  # 如果字符为'W'，表示华华得分
            score_11[-1][0] += 1  # 11分制下华华得分加1
            score_21[-1][0] += 1  # 21分制下华华得分加1
        if c == 'L':  # 如果字符为'L'，表示对手得分
            score_11[-1][1] += 1  # 11分制下对手得分加1
            score_21[-1][1] += 1  # 21分制下对手得分加1
        check_game(score_11, 11)  # 检查11分制比分情况
        check_game(score_21, 21)  # 检查21分制比分情况

for score in score_11:  # 遍历11分制下的比分
    print(f'{score[0]}:{score[1]}')  # 输出比分

print()  # 输出空行

for score in score_21:  # 遍历21分制下的比分
    print(f'{score[0]}:{score[1]}')  # 输出比分
