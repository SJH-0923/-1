#LAB 3-6
for i in range(5) :
    print("Hello, Python!")
print('\n')
for i in range(5) :
    print(i)
print('\n')

#LAB 3-7
#1
a = list(range(1,101))
print('100 이하의 자연수 리스트 :', a)
print('\n')
#2
a = list(range(2,101,2))
print('100 이하의 짝수 리스트 :', a, end = "\n")
print('\n')
#3
a = list(range(1,101,2))
print('100 이하의 홀수 리스트 :', a)
print('\n')
#4
a = list(range(-100,0,1))
print('음수 리스트 :', a)
print('\n')

#LAB 3-8
#1
a = 0
for i in range(1,101) :
    a = a+i
print('1에서 100까지 정수의 합 :', a)
#2
a = 0
for i in range(0,101,2) :
    a = a+i
print('1에서 100까지 짝수의 합 :', a)
#3
a = 0
for i in range(1,101,2) :
    a = a+i
print('1에서 100까지 홀수의 합 :', a)
print('\n')

#LAB 3-9
n = 7
for i in range(n, 0, -1) :
    print(' '*(i-1) + '#')
