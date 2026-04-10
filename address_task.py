import json #모듈 부르기

#파일 불러오기
with open("addressbook.json", "r", encoding = "utf-8")as f :
        addressbook = json.load(f) #파일 읽기

while True :
    print()
    print("[추가 / 조회 / 검색 / 삭제 / 종료]")
    a = input("작업을 선택하세요 :")

    if a == "추가" :
        print()
        #주소록 추가
        while True :
            name = input("이름을 입력하세요.\n(작업 종료를 원하시는 경우 '종료'를 입력):")
            if(name == "종료") :
                break
            
            while True :
                number = input("전화번호를 입력하세요 :")
                if len(number) != 11 :
                    print("잘못 입력했습니다. 다시 입력하세요.")
                if len(number) == 11 :
                    break
            addressbook[name] = number

        #파일 저장하기
        with open("addressbook.json", "w", encoding = "utf-8")as f :
            json.dump(addressbook, f, ensure_ascii = False, indent = 4)
        print()
        print("주소록이 저장되었습니다.")

    if a == "조회" :

        #파일 불러오기
        with open("addressbook.json", "r", encoding = "utf-8")as f :
            addressbook = json.load(f)

        #불러온 주소록 프린트하기
        print()
        print("저장된  주소록\n")
        for key in addressbook :
            print('{} : {}'.format(key, addressbook[key]))#모든 사람의 주소록

    if a == "검색" :
        while True :
            print()
            print("찾으시려는 사람의 이름을 입력하세요 :")
            c = input("")
    
            if c in addressbook :
                print(c, "님의  번호 :", addressbook[c]) #특정 사람의 주소록

            if c == "종료" :
                print("종료합니다.")
                break

            if c not in addressbook :
                print(c, "님은 등록되어 있지 않습니다.")

    if a == "삭제" :
        print("저장된  주소록\n")
        for key in addressbook :
            print('{} : {}'.format(key, addressbook[key]))
        print()
        print("삭제할 사람 이름을 입력하세요 :")
        d = input("")
        if d in addressbook :
            del addressbook[d]
        with open("addressbook.json", "w", encoding = "utf-8")as f :
            json.dump(addressbook, f, ensure_ascii = False, indent = 4)
            print("삭제되었습니다.")


    if a == "종료" :
        print("종료합니다.")
        break
