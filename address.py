
import json

'''
#파일 저장하기
addressbook = {"서재현" :"01022222222"}

with open("addressbook.json", "w", encoding = "utf-8")as f :
    json.dump(addressbook, f, ensure_ascii = False, indent = 4)

print("주소록이 저장되었습니다.")

'''
#파일 불러오기
with open("addressbook.json", "r", encoding = "utf-8")as f :
    addressbook = json.load(f)

print("불러온 주소록 :", addressbook)
print("서재현 번호 :", addressbook["서재현"])

print("git bash test")
