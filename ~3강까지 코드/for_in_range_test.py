for i in range(5) :
    print(i)
for i in range(5) :
    print(i, end = ' ')
print()
for i in range(0,10,2) :
    print(i, end = ' ')
print()
for i in range(-2,-10,-2) :
    print(i, end = ' ')
print()

s = 0
for i in range(1, 11) :
    s = s + i
print(s)
print('1에서 10까지의 합:', s)

s = 0
for i in range(1, 11) :
    s = s + i
    print('i = {}, s = {}'.format(i, s) )
print('1에서 10까지의 합:', s)

n = int(input('합계를 구할 수를 입력하세요 : '))
s = 0
for i in range(0, n) :
    s = s + (i+1)

print('1부터 {}까지의 합은 {}'.format(n, s))
