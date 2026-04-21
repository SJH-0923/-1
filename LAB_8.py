#LAB 8-1

#1
#error : list index out of range
#error : invalid literal for int() with base 10: '20%'
#error : unsupported operand type(s) for +: 'int' and 'str'

#2
try :
    a = [10, 20, 30]
    a[3]
except Exception as e :
    print("error :", e)

try :
    n = int("20%")
except Exception as e :
    print("error :", e)

try :
    a = 100 + "200"
except Exception as e :
    print("error :", e)

#LAB 8-2

#1
try :
    10 * (30/0)
    X = int(input("정수 X를 입력하세요 :"))
    import sys

    f = open("myfile.txt")
    s = f.readline()
except Exception as e :
    print("error :", e)

#LAB 8-3
a = [1, 2, 3, 4, 5]
print(a)

try :
    user_input = input("a의 요소를 하나 선택하세요 :")
    num = int(user_input)
    idx = a.index(num)

    print(f"{num}은(는) {a[idx]} 요소입니다.")

#2
except ValueError :
    print("오류 : 입력 값이 정수나 실수가 아님")

except Exception as e :
    print("오류 : 리스트에 없는 요소이거나 기타 오류 발생")
