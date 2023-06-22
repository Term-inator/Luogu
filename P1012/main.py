from functools import cmp_to_key

# 读取输入的数字个数
n = int(input())

# 读取输入的数字并分割为列表
numbers = input().split()


# 自定义比较函数
def compare(a, b):
    # 将数字a和数字b拼接成两种顺序
    order1 = a + b
    order2 = b + a

    # 如果order1大于order2，则a应该排在b之前，返回-1
    if order1 > order2:
        return -1
    # 如果order1小于order2，则b应该排在a之前，返回1
    elif order1 < order2:
        return 1
    # 如果order1等于order2，则a和b的顺序无所谓，返回0
    else:
        return 0


# 将数字列表按照自定义的比较函数进行排序
numbers.sort(key=cmp_to_key(compare))

# 拼接排序后的数字列表，并输出最大的整数
print(''.join(numbers))
