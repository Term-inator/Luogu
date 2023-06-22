# 读取输入的整数个数
n = int(input())

# 读取输入的正整数列表，并将其转换为集合
numbers = set(map(int, input().split()))

# 创建一个集合，用于存储所有可能的和
sum_set = set()

# 遍历正整数集合中的每个数
for i in numbers:
    # 再次遍历正整数集合中的每个数
    for j in numbers:
        # 排除相同的数，避免重复计算
        if i != j:
            # 将两个数的和添加到和集合中
            sum_set.add(i + j)

# 计算正整数集合与和集合的交集元素个数，即满足条件的数的个数
answer = len(numbers.intersection(sum_set))

# 输出答案
print(answer)
