n = 7 # 외부 for 루프는 n번 수행, i는 0,1,2,3,4,5,6 까지 증가
for i in range(n):
    st = ''
    for j in range(i): # 내부 for 루프는 i번 수행
        st = st + ' ' # 공백을 i개 추가함
    print(st + '#') # 공백 추가 후 '#'출력



n = 7 # 외부 for 루프는 n번 수행, i는 0,1,2,3,4,5,6 까지 증가
for i in range(n):
    print (' ' * i + '#') # 공백을 i번 추가한 후 '#'출력

n = 3
for i in range(n) :
    print(' '*i + '#')
print(end = ' ')
n = 3
for i in range(n) :
    print(' '*i + '#')
