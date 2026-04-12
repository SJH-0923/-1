import json #모듈 부르기

#파일 불러오기
with open("addressbook.json", "r", encoding = "utf-8")as f :
        addressbook = json.load(f) #파일 읽기

while True :
    print()
    print("[추가 / 조회 / 검색 / 삭제 / 종료]")
    a = input("작업을 선택하세요 :")
    
    #다른 입력 감지
    if a != "추가" and  a != "조회" and  a != "검색" and a != "삭제" and a != "종료" :
        print("\n잘못된 입력입니다. 다시 입력해주세요.")
        continue

    #추가
    if a == "추가" :
        print()
        #주소록 추가
        while True :
            name = input("이름 (작업을  종료하려면  '이전'):")
            if name == "" :
                print("잘못된 입력입니다. 다시 입력해 주세요.")
                continue

            if name == "이전" :
                break
                
            if name in addressbook :
                print("이미 저장된 이름입니다. 새로 저장하시겠습니까? (y/n)")
                e = input("")
                if e == "y" :
                    pass

                if e == "n" :
                    print("기존 주소록에 덮어씌우시겠습니까? (y/n)")
                    g = input("")
                    if g == "y" :
                        pass
                    
                    if g == "n" :
                        continue
                    
                if e == "" :
                    print("잘못된 입력입니다. 다시 입력해 주세요..")
                    continue

            number = input("전화번호 (작업을 종료하려면 '이전') :")
            if(number == "이전") :
                break

            if number == "" :
                print("잘못된 입력입니다. 다시 입력해 주세요.")
                continue

            if len(number) != 11 :
                print("잘못된 입력입니다. 다시 입력해 주세요.")
                continue

            addressbook[name] = number


            #파일 저장하기
            with open("addressbook.json", "w", encoding = "utf-8")as f :
                json.dump(addressbook, f, ensure_ascii = False, indent = 4)
            print()
            print("주소록이 저장되었습니다.")

    #조회
    if a == "조회" :

        #파일 불러오기
        with open("addressbook.json", "r", encoding = "utf-8")as f :
            addressbook = json.load(f)
        sorted_addressbook = dict(sorted(addressbook.items()))

        #불러온 주소록 프린트하기
        print()
        print("저장된  주소록\n")
        for key in sorted_addressbook :
            print('{} : {}'.format(key, sorted_addressbook[key]))#모든 사람의 주소록

    #검색
    if a == "검색" :
        while True :
            print()
            print("찾는  사람의 이름 (작업을 종료하려면 '이전') :")
            c = input("")
    
            if c in addressbook :
                print(c, "님의  번호 :", addressbook[c]) #특정 사람의 주소록

            if c == "이전" :
                break

            if c not in addressbook :
                print(c, "님은 등록되어 있지 않습니다.")

    #삭제
    if a == "삭제" :
        while True :
            print("저장된  주소록\n")
            sorted_addressbook = dict(sorted(addressbook.items()))
            for key in sorted_addressbook :
                print('{} : {}'.format(key, sorted_addressbook[key]))
            print()
            print("삭제할 사람 이름 (작업을 종료할려면 '이전' 입력) :")
            d = input("")
            print()
 
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
        print("종료합니다.")
        break



 # !!! 동명이인일 경우 어떻게 해야 하는지 아직 난제임
 # !!! 그냥 엔터를 쳤을 때 잘못된 입력입니다. 하고 리턴할 수 있게 다시 만들기
 # !!! 추가 파트만 조금 더 세분화 하면 될 듯 ! 나머지는 괜찮다.
