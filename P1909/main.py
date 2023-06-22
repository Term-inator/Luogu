income = 300  # 每月的零花钱
savings = 0  # 津津的储蓄金额
balance = 0  # 当前余额

for month in range(12):
    expense = int(input())  # 当月的预算
    balance += income - expense  # 更新当前余额

    if balance < 0:
        # 如果余额不够支付当月预算，则输出出现这种情况的第一个月
        print(f'-{month + 1}')
        break

    to_store = balance // 100 * 100  # 需要存入储蓄的金额
    savings += to_store  # 更新储蓄金额
    balance -= to_store  # 更新当前余额

else:
    # 如果循环正常结束，即储蓄计划可以执行完整
    total_savings = int(savings * 1.2 + balance)  # 年末津津手中的总金额
    print(total_savings)
