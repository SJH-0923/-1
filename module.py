import datetime
datetime.datetime.now()
print(datetime.datetime.now())
print(dir(datetime))

import datetime as dt
print(dt.datetime.now())

import math as m
print(dir(m))

m.pow(3,3) #지수함수
m.fabs(-99) #실수 절댓값
m.ceil(2.1) #올림
m.floor(2.1) #내림

a = m.sin(m.pi/2.0)
print(a)
b = m.sin(0.0)
print(b)
c = m.sin(90.0)
print(c)

import random as rd

a = rd.random()

print(a)

a = list(range(1,11))
rd.shuffle(a)
print(a)

#GUI의 일종
import turtle as t
t.shape("turtle")
t.setup(width = 400, height = 400)
for i in range(200) :
    t.forward(i)
    t.left(93)
t.done()
