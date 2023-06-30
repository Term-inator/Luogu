# 利用记忆化搜索的方式计算合法的数列个数

# 创建一个列表用于存储计算结果
mem = [0 for _ in range(1005)]


# 定义递归函数gen，计算以num为起点的合法数列个数
def gen(num):
    # 如果num为1，即只有一个数字的数列，返回1
    if num == 1:
        return 1

    # 如果已经计算过num对应的结果，则直接返回结果
    if mem[num] != 0:
        return mem[num]

    # 初始化结果为1
    res = 1

    # 遍历从1到num的每个数，作为合法数列的下一个数字
    for i in range(1, num // 2 + 1):
        # 递归计算以i为起点的合法数列个数，并加到结果中
        res += gen(i)

    # 将计算结果保存到mem列表中
    mem[num] = res

    # 返回结果
    return res


# 读取输入的整数n
n = int(input())

# 调用gen函数计算合法的数列个数，并输出结果
print(gen(n))
