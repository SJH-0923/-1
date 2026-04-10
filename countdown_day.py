import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year,
                                  today.month, today.day))
xMas = dt.datetime(2026, 12, 25)
time_gap = xMas- dt.datetime.now()
print('다음 크리스마스 까지는 {}일 {}시간 남았습니다.'.format(
    \
time_gap.days,time_gap.seconds // 3600))
# \ 는 다음 줄 까지 연결해서 확장해서 실행해라
