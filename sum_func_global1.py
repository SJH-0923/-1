def print_sum():
    a = 1
    b = 2
    result = a + b
    print('print_sum() 내부 :', a, '과', b, '의 합은', result, '입니다.')

a = 10 # 전역변수 a
b = 20 # 전역변수 b
print_sum()
result = a + b
print('print_sum() 외부 :', a, '과', b, '의 합은', result, '입니다.')
