'''score = [87, 84, 95, 67, 84, 94, 63]
print(score)
print(type(score))
for i in score :
    print(i)
names = ['재현', '찬희', '세진', '영수', '현우', '기근', '지훈']
print(type(names))
for i in names :
    print(i)
names = ['재현', '찬희', '세진', '영수', '현우', '기근', '지훈', score]
for i in names :
    print(i)
addesbook = [['재현', '24'], ['찬희', '24']]
for i in addesbook :
    print(i)


ri = list(range(5))
print(ri)


myString = "apple"

listString = list(myString)

for ch in myString :
    print(ch)

listString = list(myString)
print(listString[-1])

a_list = [10,20,30,40]
a_list.append(50)
print(a_list)
a_list.remove(10)
print(a_list)
'''
b_list = [11,22,33,44,55,66]
print(b_list)
b_list.pop(3)
print(b_list)
print(10 in b_list)
print(10 not in b_list)

list1 = [20,10,40,50,30]
list1.sort()
print(list1)
list2 = sorted(list1)
print(list2)
