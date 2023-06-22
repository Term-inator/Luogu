def calculate_check_sum(isbn):
    """
    计算 ISBN 号码的识别码
    :param isbn: ISBN 号码（不包含识别码）
    :return: 识别码
    """
    check_sum = sum((i + 1) * int(x) for i, x in enumerate(isbn)) % 11
    return 'X' if check_sum == 10 else str(check_sum)


def validate_isbn(isbn):
    """
    验证 ISBN 号码的识别码是否正确
    :param isbn: 完整的 ISBN 号码
    :return: 如果识别码正确，返回 'Right'，否则返回正确的 ISBN 号码
    """
    isbn_digits = ''.join(isbn[:-1].split('-'))  # 去除分隔符并拼接数字
    calculated_check_sum = calculate_check_sum(isbn_digits)
    if calculated_check_sum == isbn[-1]:
        return 'Right'
    else:
        return isbn[0:-1] + calculated_check_sum


# 读取输入的 ISBN 号码
isbn = input()
# 验证 ISBN 号码的识别码并输出结果
result = validate_isbn(isbn)
print(result)
