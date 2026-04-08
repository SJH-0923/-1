a = 100
b = 200
print('Before swap :', a, b)
#a, b = b, a
#print('After swap :', a, b)
#패킹해서 한 번에 바꿈
#a=b
#b=a #위에서 이미 바꿔서 그냥 맞는 말임
#print('After swap :', a, b)
#걍 보는 그대로 순서대로 바꿈
a_origin = a
a = b
b = a_origin
print('After swap :', a, b)
