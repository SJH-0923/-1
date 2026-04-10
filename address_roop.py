import json

#주소록 데이터
addressbook = {} #또는 addressbook = dic()

#주소록 추가
name = None
while(True) :
    name = input("이름을 입력하세요 :")
    if(name == "끝") :
        break
    number = input("전화번호를 입력하세요 :")
    addressbook[name] = number

#파일 저장하기
with open("addressbook.json", "w", encoding = "utf-8")as f :
    json.dump(addressbook, f, ensure_ascii = False, indent = 4)

print("주소록이 저장되었습니다.")

#파일 불러오기
with open("addressbook.json", "r", encoding = "utf-8")as f :
    addressbook = json.load(f)

print("불러온 주소록 :", addressbook)
print("서재현 번호 :", addressbook["서재현"])
