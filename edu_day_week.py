def day_week_x(days_week,month_cnt,k):
    days_sum, number_month = 0, 0
    for month in month_cnt:
        if days_sum < k:
            days_sum += month
            number_month += 1
    day_x = month_cnt[number_month - 1] - (days_sum - k)
    if day_x > 7:
        print(days_week[day_x % 7])
    else:
        print(days_week[day_x])

days_week = {1:'Понедельник',
             2:'Вторник',
             3:'Среда',
             4:'Четверг',
             5:'Пятница',
             6:'Суббота',
             7:'Воскресенье'}
month_cnt = [31,28,31,30,31,30,31,31,30,31,30,31]
k = int(input())

day_week_x(days_week,month_cnt,k)