print("hello python")
#----------------------------------------------------
a = print("hello world")

print(a) #입력은 있는데 출력이 없는 경우
#----------------------------------------------------
b = "hello"
print(b)
#----------------------------------------------------
def plus(a,b):
    c = a+b
    return c

ans = plus(4,3)

print(ans)
#return을 해야 함 : 후에 계산에서도 사용하기 위해
#----------------------------------------------------
print('hello world')
print('hello','world')
print('hello'+'world') # 공백 생성 안됨
print(100)

print(2+4)

x = 105
y = 10

print(x//y)#몫
print(x%y)#나머지
#----------------------------------------------------
radius = 4.0
print('원의 반지름',radius)
print('원의 면적', 3.14*radius*radius)
print('원의 둘레', 2.0*3.14*radius)
#radius 라는 변수를 하나 만들어서 반지름5이 바뀌더라도 편하게 계산 가능
