#LAB 5-1
#1
even_list = [2,4,6,8,10]
print(even_list)
#2
for i in range(1,6) :
    print(2*i)
#3
nations = ['Korea', 'China', 'India', 'Nepal']
print(nations)
#4
friends = ['찬희', '세진', '영수', '기근', '지훈']
print(friends)
#5
string = ['X', 'Y', 'Z']
print(string)

#LAB 5-2
#1
prime_list = [2,3,5,7]
print('prime_list의 첫 원소 :', prime_list[0])
#2
print('prime_list의 마지막 원소 :', prime_list[3])
#3
print('prime_list의 마지막 원소 :', prime_list[-1])
#4
nations = ['Korea', 'China', 'Russia', 'Malaysia']
print('nations의 첫 원소 :', nations[0])
#5
print('nations의 마지막 원소 :', nations[-1])
#6
print('nations의 마지막 원소 :', nations[len(nations) + -1])

#LAB 5-3
#1
print('소수 목록 :', prime_list)
prime_list.append(11)
print('추가 후 소수 목록 :', prime_list)
#2
print('삭제 전 소수 목록 :', prime_list)
prime_list.remove(3)
print('삭제 후 소수 목록 :', prime_list)
#3
print('국가 목록 :', nations)
nations.append('Nepal')
print('추가 후 국가 목록 :', nations)
#4
if 'Japan' not in nations :
    print('Japan 는(은) 국가 목록에 없습니다.')
if 'Russia' in nations :
    print('Russia 는(은) 국가 목록에 있습니다.')

#LAB 5-4
#1
print('1에서 10까지의 소수 :', prime_list)
print('최솟값 :', min(prime_list))
print('최댓값 :', max(prime_list))
print('합계 :', sum(prime_list))
print('평균 :', len(prime_list))
#2
nations.remove('Nepal')
print('국가 목록 :', nations)
print('사전에 가장 먼저 나오는 나라 :', min(nations))
print('사전에 가장 나중에 나오는 나라 :', max(nations))

#LAB 5-5
#1
a = [1,2,3]
b = [10,20,30]
a.append(b)
print(a)
a.remove(b)
a.extend(b)
print(a)
#2
nlist = [1,2,3,4,5,6,7,8,9,10]
print(nlist)
#3
nlist.insert(0,0)
print(nlist)
#4
nlist.sort(reverse = True)
print(nlist)
#5
print('마지막 원소 :', nlist[-1])
nlist.pop(-1)
print(nlist)

#LAB 5-6
#1
a = [1,2,3]
print('반복할 정수를 입력하시오 :', 3)
print(a*3)
#2
print('반복할 정수를 입력하시오 :', 4)
print(a*4)

#LAB 5-7
#1
n_list = list(range(15))
print('n_list =', n_list)
#2
print('s_list1 =', n_list[0:5])
print('s_list2 =', n_list[5:11])
print('s_list3 =', n_list[11:])
print('s_list4 =', n_list[2:11:2])
print('s_list5 =', n_list[10:5:-1])
n_list.sort(reverse = True)
print('s_list6 =', n_list[4:13:2])
