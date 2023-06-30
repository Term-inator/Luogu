# 输入N和K
N, K = map(int, input().split())

# 初始化动态规划数组
dp = [0 for _ in range(N + 1)]
dp[0] = 1  # 初始状态：到达第0级台阶的方式数为1
dp[1] = 1  # 初始状态：到达第1级台阶的方式数为1
mod = 100003  # 取模的值


def count_ways():
    """
    计算到达第N级台阶的不同方式数
    """
    for i in range(2, N + 1):
        for j in range(1, K + 1):
            if i >= j:
                dp[i] = (dp[i] + dp[i - j]) % mod  # 状态转移方程：dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-K]


count_ways()
print(dp[N])  # 输出到达第N级台阶的不同方式数
