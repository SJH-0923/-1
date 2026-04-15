
try:
    a, b = input('두 수를 입력하시오: ').split()
    result = int(a) / int(b)
except ZeroDivisionError:
    print('오류 : 0으로 나눔을 시도했습니다.')
except ValueError:
    print('오류 : 입력 값이 정수나 실수가 아닙니다.')
except:
    print('오류 : 102와 같이 두 정수를 입력하세요.')
else:
    print('{} / {} = {}'.format(a, b, result))


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('0으로 나누는 오류발생')
    else:
        print('결과 :', result)
    finally:
        print('수행완료')
print('divide(100, 2) 함수호출 :')
divide(100, 2)
print('divide(100, 0) 함수호출 :')
divide(100, 0)

#에러를 만들 수도 있다. raise 사용
