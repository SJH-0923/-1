try :
    a = 1/0
except :
    print("0으로 나누지 마라")

while True :

    try :
#        a, b = input("두 수를 입력하세요 :").split()
#        result = int(a) / int(b)
        a, b = map(int,input("두 수를 입력하세요 :").split(","))
        result = a/b
        print("{} / {} = {}".format(a, b, result))

    except :
        print("수가 정확한지 확인하세요.")
