# 读取输入的一串整数，以空格间隔
numbers = list(map(int, input().split()))

# 移除列表中的最后一个元素，即数字0
numbers.pop()

# 反转列表中的元素顺序
numbers.reverse()

# 遍历列表并输出每个元素，以空格间隔
for num in numbers:
    print(num, end=' ')
