#LAB 7-1

import datetime as dt
today = dt.datetime.today()

if today.hour < 12 :
    a = "오전"
    hour = today.hour
    if hour == 0 : hour = 12

else :
    a = "오후"
    hour = today.hour - 12 if today.hour > 12 else 12

print(f"오늘의 날짜 : {today.year}년 {today.month}월 {today.day}일")
print(f"현재 시간 : {a} {today.hour}시 {today.minute}분 {today.second}초")

#LAB 7-2

import datetime as dt
today = dt.date.today()

#1
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
xMas = dt.datetime(2026, 12, 25)
time_gap_christmas = xMas- dt.datetime.now()
print('다음 크리스마스 까지는 {}일 {}시간 남았습니다.'.format( \
time_gap_christmas.days,time_gap_christmas.seconds // 3600))

#2
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
new_year = dt.datetime(2036, 1, 1)
time_gap_new_year = new_year - dt.datetime.now()
print('2036년 새해  까지는 {}일 {}시간 남았습니다.'.format( \
time_gap_new_year.days,time_gap_new_year.seconds // 3600))

#3
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
my_birthday = dt.datetime(2026, 9, 23)
time_gap_my_birthday = my_birthday - dt.datetime.now()
print('2026년 내 생일 까지는 {}일 {}시간 남았습니다.'.format( \
time_gap_my_birthday.days,time_gap_my_birthday.seconds // 3600))

#LAB 7-3

#1
import datetime as dt
today = dt.date.today()

thousand = dt.timedelta(days= 1000)
a = dt.datetime.now() + thousand
print(f"오늘로부터 1,000일 후 : {a}")

#2
import datetime as dt
data = input("처음올 사귄 연도와 월, 일을 입력하세요 :")
y, m, d = map(int, data.split())
first_day = dt.datetime(y, m, d)
hundred = dt.timedelta(days = 99)
couple_day = first_day + hundred
print(f"100일 기념일은 : {couple_day.year}년 {couple_day.month}월 {couple_day.day}일 입니다.")

#LAB 7-4

import math as m

#1
for i in range(2, 11) :
    print(f"4**{i} =", float(4**i))

#2
for j in range(0, 190, 10) :
    print(j, "degree =", m.radians(j), "radian")

#3
for k in range(0, 190, 10) :
    radian = m.radians(k)
    sin = m.sin(radian)
    if k == 180 :
        sin = 0
    print("sin", k, "=", sin)

#LAB 7-5

import random as rd

#1
a = list(range(0, 101, 5))
print(f"0에서 100 이하의 정수 중에서 5의 배수\n{rd.sample(a, 3)}")

#2
b = list(range(1, 11))
print(f"1에서 10 사이의 임의의 정수 : {rd.sample(b, 3)}")

#LAB 7-7

import turtle as t

#1
t.shape("turtle")
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.done()

#2
for i in range(3) :
    t.forward(100)
    t.left(120)

for i in range(3) :
    t.forward(200)
    t.left(120)
t.done()

#3
for length in [100, 200, 300]:
    for i in range(3):
        t.forward(length)
        t.left(120)
t.done()

#4
for i in range(4) :
    t.forward(100)
    t.left(90)
t.done()

#LAB 7-8

#1
import turtle as t
t.color('blue')
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
t.setheading(90)
t.color('red')
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
t.setheading(180)
t.color('yellow')
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
t.setheading(270)
t.color('green')
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.done()

#2
import turtle as t

def draw_rect(color) :
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4) :
        t.forward(100)
        t.left(90)
    t.end_fill()

colors = ['blue', 'red', 'yellow', 'green']

for j in range(4) :
    t.setheading(90*j)
    draw_rect(colors[j])

t.done()

#3
import turtle as t

def draw_circle(color) :
    t.pencolor(color)
    t.circle(50)
    t.end_fill()

colors = ['blue', 'red', 'yellow', 'green']

for j in range(4) :
    t.setheading(90*j)
    draw_circle(colors[j])

t.done()
