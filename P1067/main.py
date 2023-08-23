n = int(input())  # 输入一元多项式的次数

coefficients = map(int, input().split())  # 输入多项式的系数列表

result = ''  # 初始化结果字符串

# 遍历系数列表
for i, coefficient in enumerate(coefficients):
    if coefficient == 0:  # 如果系数为0，则跳过当前项
        continue

    # 计算当前项的指数部分
    exponent = n - i

    if exponent == 0:  # 如果指数为0，则只需要输出系数部分
        term = str(abs(coefficient))
    elif exponent == 1:  # 如果指数为1，则指数部分为"x"
        term = 'x'
    else:  # 其他情况下，指数部分为"x^b"，其中b为指数
        term = f'x^{exponent}'

    if abs(coefficient) != 1 and exponent != 0:  # 如果系数不为1且指数不为0，则需要输出系数部分
        term = str(abs(coefficient)) + term

    if coefficient > 0:  # 如果系数为正数，则在结果字符串前添加"+"
        term = '+' + term
    else:  # 如果系数为负数，则在结果字符串前添加"-"
        term = '-' + term

    result += term  # 将当前项添加到结果字符串中

if result == '':  # 如果结果字符串为空，则多项式为0
    result = '0'

if result[0] == '+':  # 如果结果字符串的开头为"+"，则去掉开头的"+"
    result = result[1:]

print(result)  # 输出多项式的字符串表示形式
