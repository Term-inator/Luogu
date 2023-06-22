# 读取输入字符串
s = input()

# 初始化计数器
count = 0

# 遍历字符串的每个字符
for char in s:
    # 如果字符不是空格和换行符，则增加计数器
    if char != ' ' and char != '\n':
        count += 1

# 输出计数器的值，即作文标题的字符数（不含空格和换行符）
print(count)
