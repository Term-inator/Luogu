# 从输入读取一个整数
n = input()

# 判断第一位是否为负号
if n[0] == '-':
    # 如果是负数，则将负号保留，并将其余位数反转
    reversed_num = int('-' + n[:0:-1])
else:
    # 如果是正数，则直接将所有位数反转
    reversed_num = int(n[::-1])

# 输出反转后的新数
print(reversed_num)
