person = {'이름' : '홍길동', '나이' : 26, '몸무게' : 82 }
person['국적'] = '대한민국'
print(person['이름'])
print(person)

students = { 2019001:'이순신', 2019002:'김유신', 2019003:'강감찬'}
print(students[2019001])

#과제
#3명 학번, 이름, 전화번호 입력받아서 딕셔너리로 만들고 프린트
#특정 학번이 나오면 루프 멈추기 end of input 지정

print(students == person)
print(students != person)

print(person.keys())
print(person.values())

for key in person :
    print('{} : {}'.format(key, person[key]))
#list는 요소를 받아오지만, dictionary는 key를 받아온다.

#print(person[])

