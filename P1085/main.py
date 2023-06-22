max_unhappy = 0  # 最不高兴的时间段
most_unhappy_day = 0  # 最不高兴的是周几

for day in range(1, 8):
    school_hours, cram_hours = map(int, input().split())  # 当天上学时间和妈妈安排的课程时间

    total_hours = school_hours + cram_hours  # 当天的总学习时间

    if total_hours > 8 and total_hours > max_unhappy:
        max_unhappy = total_hours  # 更新最不高兴的时间段
        most_unhappy_day = day  # 更新最不高兴的是周几

print(most_unhappy_day)
