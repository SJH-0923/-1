n = int(input('수를 입력하세요 :'))
is_prime = True
for num in range(2, n): # 2부터 (n-1) 사이의 수 num에 대하여
    if n % num == 0: # 이 수 중에서 n의 약수가 있으면
        is_prime = False
print(n,'is prime :', is_prime)


n = int(input('수를 입력하세요 :'))
is_prime = True
for num in range(2, int(n/2)):
    if n % num == 0:
        is_prime = False
print(n,'is prime :', is_prime)
