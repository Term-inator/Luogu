mod = int(input())  # 输入模数M

# 初始化斐波拉契数列的前两项
fib_arr = [-1] * (10000000)  # 斐波拉契数列数组
fib_arr[0] = 0
fib_arr[1] = 1


# 定义递归函数计算斐波拉契数列的第n项，并将结果取模M
def fib(n):
    if fib_arr[n] != -1:
        return fib_arr[n]
    else:
        fib_arr[n] = (fib(n - 1) + fib(n - 2)) % mod
        return fib_arr[n]


res = 0  # 存储结果的变量
for i in range(2, len(fib_arr)):
    if fib(i) == 0 and fib(i + 1) == 1:  # 找到满足条件的n
        res = i
        break

print(res)  # 输出结果
