tuple1 = (1,2,3)
print(tuple1[0])
#tuple1[0] = 1
#print(tuple1[0])

def plusminus(a1, a2) :
    return a1+a2, a1-a2

output = plusminus(1,2)
print(type(output)) #함수의 아웃풋은 튜플임
output_list = list(output) #아웃풋을 리스트로 바꾸는 코드
print(type(output_list))
