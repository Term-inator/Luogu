target_word = input().lower()  # 给定的单词，转换为小写
sentence = input().lower() + ' '  # 给定的文章，转换为小写，最后加上一个空格以处理最后一个单词

word_list = []  # 存储文章中的单词和对应的位置

buffer = ''  # 缓存当前正在读取的单词
index = 0  # 当前字符的位置索引

# 遍历文章中的字符
for i, char in enumerate(sentence):
    if char == ' ':  # 如果当前字符是空格，说明一个单词结束
        if buffer != '':  # 如果缓存非空，说明读取到了完整的单词
            word_list.append((buffer, index))  # 将完整的单词和位置添加到列表中
            buffer = ''  # 清空缓存
        index = i + 1  # 更新位置索引，指向下一个单词的起始位置
    else:
        buffer += char  # 将当前字符添加到缓存中，构建当前单词

times = 0  # 统计目标单词在文章中出现的次数
first_pos = -1  # 目标单词第一次出现的位置

# 遍历文章中的单词和位置
for word, pos in word_list:
    if word == target_word:  # 如果当前单词与目标单词匹配
        times += 1  # 统计次数加一
        if first_pos == -1:  # 如果是第一次匹配
            first_pos = pos  # 更新第一次出现的位置

if first_pos == -1:  # 如果目标单词没有在文章中出现过
    print(-1)
else:
    print(f'{times} {first_pos}')  # 输出出现次数和第一次出现的位置
