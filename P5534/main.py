a1, a2, n = map(int, input().split())

d = a2 - a1  # 等差值

arr = [a1, a2]  # 存储等差数列的列表
for i in range(n - 2):
    next_term = arr[-1] + d  # 计算下一项的值
    arr.append(next_term)  # 将下一项添加到列表中

sum_of_terms = sum(arr)  # 计算等差数列的各项之和

print(sum_of_terms)
