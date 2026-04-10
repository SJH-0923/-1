import json #모듈 부르기

with open("addressbook.json", "r", encoding = "utf-8")as f :
        addressbook = json.load(f) #파일 읽기

while True :

    print()
    print("주소록을 추가하시려면 1\n주소록을 불러오시려면 2\n특정인의  주소록을 찾으시려면 3\n종료하시려면 4")
    a = input("")

    if a == "1" :

        #기존 주소록 데이터 읽기
        with open("addressbook.json", "r", encoding = "utf-8")as f :
            addressbook = json.load(f)
        print()
        #주소록 추가
        name = None
        while True :
            name = input("이름을 입력하세요 :")
            if(name == "끝") :
                break
            number = input("전화번호를 입력하세요 :")
            addressbook[name] = number

        #파일 저장하기
        with open("addressbook.json", "w", encoding = "utf-8")as f :
            json.dump(addressbook, f, ensure_ascii = False, indent = 4)
        print()
        print("주소록이 저장되었습니다.")

        #파일 불러오기
        with open("addressbook.json", "r", encoding = "utf-8")as f :
            addressbook = json.load(f)

    if a == "2" :

        #파일 불러오기
        with open("addressbook.json", "r", encoding = "utf-8")as f :
            addressbook = json.load(f)

        #불러온 주소록 프린트하기
        print()
        print("저장된  주소록", "\n",
            addressbook) #모든 사람의 주소록

    if a == "3" :
        print()
        print("찾으시려는 사람의 이름을 입력하세요 :")
        c = input("")
    
        if c in addressbook :
            print(c, "님의  번호 :", addressbook[c]) #특정 사람의 주소록

        if c not in addressbook :
            print(c, "님은 등록되어 있지 않습니다.")

    if a == "4" :
        print("종료합니다.")
        break
