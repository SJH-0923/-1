'''
n = 7 # 외부 for 루프는 n번 수행, i는 0,1,2,3,4,5,6 까지 증가
for i in range(n):
    st = ''
    for j in range(i): # 내부 for 루프는 i번 수행
        st = st + ' ' # 공백을 i개 추가함
    print(st + '#') # 공백 추가 후 '#'출력

n = 7 # 외부 for 루프는 n번 수행, i는 0,1,2,3,4,5,6 까지 증가
for i in range(n):
    print (' ' * i + '#') # 공백을 i번 추가한 후 '#'출력
'''

'''
n = 7
for i in range(n):
    print (' ' * i + '#')

n = 7
for i in range(n - 1, -1, -1):
    print (' ' * i + '#')

n = 7
for i in range(n):
    print (' ' * i + '#')
'''

'♥'
'(x**2 + y**2 - 1)**3 - x**2 * y**3 = 0'

'''
n = 10
print(' '*2 + '#'*5 + ' '*2 + '#'*5)
print(' ' + '#' + ' '*(n-2) + '#' + '#' + ' '*(n-2) + '#')
for i in range(n, -1, -1) :
    print(' '*(n-i) + '#' + ' '*i + ' '*i + '#')
'''

'''
import matplotlib.pyplot as plt
(x**2 + y**2 - 1)**3 - x**2 * y**3 == 0
plt.plot(x, y)
plt.show()
'''

'''
n = 10
print(' '*2 + '#'*8 + ' '*2 + '#'*8)
print(' ' + '#' + ' '*(n-2) + '#' + '#' + ' '*(n-2) + '#')
for i in range(n, -1, -1) :
    print(' '*(n-i) + '#' + ' '*i + ' '*i + '#')
'''



n = int(input('10 ~ 60 사이의 n을 입력하세요 :'))

# 1. 하트의 윗부분 (둥근 부분)
for i in range(n // 2, n + 1, 2):
    print(" " * ((n - i) // 2), end="") # 왼쪽 여백
    print("#" * i, end="")               # 왼쪽 반원
    print(" " * (n - i), end="")         # 가운데 여백
    print("#" * i)                       # 오른쪽 반원

# 2. 하트의 아랫부분 (역삼각형)
for i in range(n * 2, 0, -4):
    # i가 2씩 줄어들도록 조절하여 경사를 완만하게 만듭니다.
    if i % 2 == 0:
        print(" " * (n - i // 2), end="")
        print("#" * (i))
