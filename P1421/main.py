# 读取输入的整数 a 和 b
a, b = map(int, input().split())

# 计算总钱数（以角为单位）
total_money = a * 10 + b

# 计算小玉最多能购买的签字笔数量
max_pens = total_money // 19

# 输出结果
print(max_pens)
