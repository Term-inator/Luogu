def readline():
    s = input()
    if s == 'EOF':  # 输入终止标志
        return None
    line = []
    for i, c in enumerate(s):
        if c == '<':  # 退格键
            if len(line) != 0:  # 非空行可以执行退格操作
                line.pop()
                continue
        if (ord('a') <= ord(c) <= ord('z')) or c == ' ' or c == '.':  # 允许的字符：小写字母、空格、英文句号
            line.append(c)
    return ''.join(line)


target = []  # 范文
while True:
    s = readline()
    if s is None:
        break
    target.append(s)

text = []  # 输入的文本
while True:
    s = readline()
    if s is None:
        break
    text.append(s)

t = int(input())  # 打字花费的时间（秒）

correct = 0  # 正确的字符数
length = min(len(target), len(text))  # 行数取较小值
for i in range(length):
    line_length = min(len(target[i]), len(text[i]))  # 行内字符数取较小值
    for j in range(line_length):
        if target[i][j] == text[i][j]:  # 字符相同时计数加一
            correct += 1

kpm = int((correct / (t / 60)) + 0.5)  # KPM计算公式
print(kpm)
