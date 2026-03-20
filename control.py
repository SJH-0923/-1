'''
num = 100
print("num =", num)
num = 200
print("num =", num)
num = 300
print("num =", num)
'''

'''
num = 0
for i in range(1000):
    num +=100
    print("ith num =", i, num)
'''


age = int(input("나이를 입력하세요."))
if age < 20 :
    print("청소년 할인")
else :
    print("청소년 할인 안됨.")


walk = int(input("걸음 수"))
if walk >=1000 :
    print("목표 달성")
else :
    print("ㅋ")



import time
from datetime import datetime

time = str(datetime.now())
if time < 12 :
    print("오전입니다.")
elif time > 12 :
    print("오후입니다.")
