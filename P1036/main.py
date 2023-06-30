import math


def is_prime(num):
    """判断一个数是否为素数"""
    if num == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


n, k = map(int, input().split())  # 输入n和k
numbers = list(map(int, input().split()))  # 输入n个整数
res = 0  # 记录素数和的种类数


def dfs(start_index, total_sum, depth):
    """
    深度优先搜索，遍历所有可能的组合
    :param start_index: 当前遍历的起始位置
    :param total_sum: 当前已选整数的和
    :param depth: 当前已选整数的个数
    """
    global k, res

    if depth == k:  # 已选满k个整数
        if is_prime(total_sum):  # 判断和是否为素数
            res += 1
        return

    for i in range(start_index, n):  # 从当前位置开始继续选择下一个整数
        dfs(i + 1, total_sum + numbers[i], depth + 1)


dfs(0, 0, 0)  # 从第一个整数开始深度优先搜索
print(res)  # 输出结果：素数和的种类数
