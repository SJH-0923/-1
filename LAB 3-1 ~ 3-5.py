#LAB 3-1
#1.
game_score = int(input("점수를 입력하세요."))
if game_score >= 1000 :
    print("당신은 고수입니다.")

#2.
num_a = int(input("숫자 a를 입력하세요."))
num_b = int(input("숫자 b를 입력하세요."))
if num_a == num_b :
    print("두 값이 일치합니다.")

#LAB 3-2
#1.
n = int(input("숫자 n을 입력하세요."))
print("n =", n)
if n%2 == 0 :
    print("n은(는) 짝수입니다.")
#2.
x = int(input("숫자 x을 입력하세요."))
print("x =", n)
if x > 0 :
    print("x은 자연수입니다.")

#LAB 3-3
#1.
game_score = int(input("점수를 입력하세요."))
if game_score >= 1000 :
    print("당신은 고수입니다.")
else :
    print("입문자입니다.")
#2.
num_a = int(input("숫자 a를 입력하세요."))
num_b = int(input("숫자 b를 입력하세요."))
if num_a == num_b :
    print("두 값이 일치합니다.")
else :
    print("두 값이 일치하지 않습니다.")
#3.
adult = int(input("성인이면 1, 성인이 아니면 0을 입력하세요."))
if adult == 1 :
    marry = int(input("기혼이면 1, 미혼이면 0를 입력하세요."))
    if marry == 1 :
        print("당신은 결혼한 성인입니다.")
    if marry == 0 :
        print("당신은 결혼하지 않은 성인입니다.")
#LAB 3-4
#1.
num = int(input("숫자를 입력하세요."))
if num > 1 and num < 10 :
    print(True)
#2.
age = int(input("나이를 입력하세요."))
if age > 10 and age < 19 :
    print("청소년입니다.")

#LAB 3-5
#1.
speed = int(input("속도를 입력하세요."))
if speed >= 100 :
    print("고속")
elif speed > 60 and speed < 100 :
    print("중속")
else :
    print("저속")
