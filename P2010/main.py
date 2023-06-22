import calendar

# 解析日期字符串，返回年、月、日
def parse_date(date_str):
    year = int(date_str[0:4])
    month = int(date_str[4:6])
    day = int(date_str[6:8])
    return year, month, day

# 验证日期是否合法
def is_valid_date(date_str):
    year, month, day = parse_date(date_str)
    if month < 1 or month > 12:
        return False
    days_in_month = calendar.monthrange(year, month)[1]
    if day < 1 or day > days_in_month:
        return False
    return True

# 判断日期是否在指定的起始日期和终止日期之间
def is_between(start_date_str, end_date_str, date_str):
    return parse_date(start_date_str) <= parse_date(date_str) <= parse_date(end_date_str)

start_date_str = input()
end_date_str = input()

start_year, _, _ = parse_date(start_date_str)
end_year, _, _ = parse_date(end_date_str)

count = 0

# 遍历起始年份到终止年份的所有年份
for year in range(start_year, end_year + 1):
    # 构造回文日期
    palindrome_date = str(year) + str(year)[::-1]
    if is_between(start_date_str, end_date_str, palindrome_date) and is_valid_date(palindrome_date):
        count += 1

print(count)
