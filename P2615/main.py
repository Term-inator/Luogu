def generate_magic_square(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # 初始化第一个数在第一行的中间位置
    row, col = 0, n // 2
    matrix[row][col] = 1

    for num in range(2, n * n + 1):
        # 判断四种填数情况
        if row == 0 and col != n - 1:
            new_row, new_col = n - 1, col + 1
        elif col == n - 1 and row != 0:
            new_row, new_col = row - 1, 0
        elif row == 0 and col == n - 1:
            new_row, new_col = row + 1, col
        else:
            if matrix[row - 1][col + 1] == 0:
                new_row, new_col = row - 1, col + 1
            else:
                new_row, new_col = row + 1, col

        # 填入当前数，更新位置
        matrix[new_row][new_col] = num
        row, col = new_row, new_col

    return matrix


def main():
    n = int(input())
    magic_square = generate_magic_square(n)

    # 输出幻方
    for row in magic_square:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()
