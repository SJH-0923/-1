import json #모듈 부르기

#파일 불러오기
with open("addressbook.json", "r", encoding = "utf-8")as f :
        addressbook = json.load(f) #파일 읽기
        content = f.read()

if content == "" :
    addressbook = {}
else :
    addressbook = json.loads(contents)

while True :
    print("[추가 / 조회 / 검색 / 삭제 / 종료]")
    a = input("작업을 선택하세요 :")
    
    #다른 입력 감지
    if a != "추가" and  a != "조회" and  a != "검색" and a != "삭제" and a != "종료" :
        print("\n잘못된 입력입니다. 다시 입력해주세요.")
        print()
        continue

    #추가
    if a == "추가" :
        print()
        #주소록 추가
        while True :
            name = input("이름 (작업을  종료하려면  '이전'):")
            print()
            if name == "" :
                print("잘못된 입력입니다. 다시 입력해 주세요.\n")
                continue

            if name == "이전" :
                break

            #새로 저장하면 리스트를 이용해서 새로운 저장. dic은 key값이 하나만 됨.    
            if name in addressbook :
                b = input("이미 저장된 이름입니다. 새로 저장하시겠습니까? (y/n)")
                if b == "" :
                    print("잘못된 입력입니다. 다시 입력해 주세요.\n")
                    continue

                if b == "y" :
                    pass

                if b == "n" :
                    e = input("기존 주소록에 덮어씌우시겠습니까? (y/n)")
                    if e == "" :
                        print("잘못된 입력입니다. 다시 입력해 주세요.\n")
                        continue

                    if e == "y" :
                        pass
                    
                    if e == "n" :
                        break
                    
                if b == "" :
                    print("잘못된 입력입니다. 다시 입력해 주세요..")
                    continue

            number = input("전화번호 (작업을 종료하려면 '이전') :")
            print()
            if(number == "이전") :
                break

            if number == "" :
                print("잘못된 번호입니다. 다시 입력해 주세요.\n")
                continue

            if len(number) != 11 :
                print("잘못된 번호입니다. 다시 입력해 주세요.")
                continue

            addressbook[name] = number


            #파일 저장하기
            with open("addressbook.json", "w", encoding = "utf-8")as f :
                json.dump(addressbook, f, ensure_ascii = False, indent = 4)
            print()
            print("주소록이 저장되었습니다.")
            print()

    #조회
    if a == "조회" :

        #파일 불러오기
        with open("addressbook.json", "r", encoding = "utf-8")as f :
            addressbook = json.load(f)
        sorted_addressbook = dict(sorted(addressbook.items()))

        #불러온 주소록 프린트하기
        print()
        if not addressbook :
            print("저장된 주소록이 없습니다.")
            print()

        else :
            print("저장된  주소록\n")
            for key in sorted_addressbook :
                print('{} : {}'.format(key, sorted_addressbook[key]))#모든 사람의 주소록
            print()

    #검색
    if a == "검색" :
        if not addressbook :
            print()
            print("저장된 주소록이 없습니다.")
            print()
        else :
            while True :
                print()
                c = input("찾는 사람의 이름 (작업을 종료하려면 '이전') :")
                print()
                if c == "" :
                    print("잘못된 입력입니다. 다시 입력해 주세요.")
                    continue

                if c in addressbook :
                    print(c, "님의  번호 :", addressbook[c]) #특정 사람의 주소록

                if c == "이전" :
                    break

                if c not in addressbook :
                    print(c + "님은 등록되어 있지 않습니다.")

    #삭제
    if a == "삭제" :
        if not addressbook :
            print()
            print("저장된 주소록이 없습니다.")
            print()

        else :
            while True :
                print("저장된  주소록\n")
                sorted_addressbook = dict(sorted(addressbook.items()))
                for key in sorted_addressbook :
                    print('{} : {}'.format(key, sorted_addressbook[key]))
                print()
                d = input("삭제할 사람의 이름 (작업을 종료하려면 '이전') :")
                print()
                if d == "" :
                    print("잘못된 입력입니다. 다시 입력해 주세요.")
                    continue

                if d == "이전" :
                    break

                if d not in addressbook :
                    print(d, "님은 등록되어 있지 않습니다.")
                    print()

                if d in addressbook :
                    del addressbook[d]
                    print("삭제되었습니다.")
                    print()

                with open("addressbook.json", "w", encoding = "utf-8")as f :
                    json.dump(addressbook, f, ensure_ascii = False, indent = 4)

    #종료
    if a == "종료" :
        print()
        print("종료합니다.")
        break



 # !!! 동명이인일 경우 어떻게 해야 하는지 아직 난제임 --> value 값을 list로 바꾸면 해결
 # !!! 그냥 엔터를 쳤을 때 잘못된 입력입니다. 하고 리턴할 수 있게 다시 만들기
 # !!! 추가 파트만 조금 더 세분화 하면 될 듯 ! 나머지는 괜찮다.
