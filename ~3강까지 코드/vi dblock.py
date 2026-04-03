num = int(input("숫자를 입력하세요 :"))

if num < 0 :
    print(num, "은(는) 음수입니다.")
elif num % 2 == 0 :
    print(num, "은(는) 짝수입니다.")
else :
    print(num, "은(는) 홀수입니다.")
