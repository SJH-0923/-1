n = int(input('10 ~ 60 사이의 n을 입력하세요 :'))


for i in range(n // 2, n + 1, 2):
    print(" " * ((n - i) // 2), end="")
    print("#" * i, end="")
    print(" " * (n - i), end="")
    print("#" * i)

for i in range(n * 2, 0, -4):
    if i % 2 == 0:
        print(" " * (n - i // 2), end="")
        print("#" * (i))
