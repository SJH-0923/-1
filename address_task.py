import json #모듈 부르기

#파일 불러오기
with open("addressbook.json", "r", encoding = "utf-8")as f :
        addressbook = json.load(f) #파일 읽기

if not addressbook :
    addressbook = {}

else :
    with open("addressbook.json", "r", encoding = "utf-8")as f :
        addressbook = json.load(f)

while True :
    print("[추가 / 수정 / 조회 / 검색 / 삭제 / 종료]")
    a = input("작업을 선택하세요 :")
    
    #다른 입력 감지
    if a != "추가" and  a != "조회" and  a != "검색" and a != "삭제" and a != "종료" and a != "수정" :
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
            
            name = f"{name}1"
            final_name = name
            is_cancel = False

            #새로 저장하면 리스트를 이용해서 새로운 저장. dic은 key값이 하나만 됨.    
            if name in addressbook :
                b = input("이미 저장된 이름입니다. 새로 저장하시겠습니까? (y/n)")
                if b == "" :
                    print("잘못된 입력입니다. 다시 입력해 주세요.\n")
                    continue

                if b == "y" :
                    count = 2
                    while f"{name}{count}" in addressbook :
                        count += 1
                    final_name = f"{name}{count}"

                if b == "n" :
                    e = input("기존 주소록에 덮어씌우시겠습니까? (y/n)")
                    if e == "" :
                        print("잘못된 입력입니다. 다시 입력해 주세요.\n")
                        continue

                    if e == "y" :
                        final_name = name
                    
                    if e == "n" :
                        is_cancel = True

                if is_cancel :
                    continue
                    
                if b == "" :
                    print("잘못된 입력입니다. 다시 입력해 주세요..")
                    continue

            while True :
                number = input("전화번호 (-)제외 (작업을 종료하려면 '이전') :")
                print()
                
                if(number == "이전") :
                    break

                if number == "" :
                    print("잘못된 번호입니다. 다시 입력해 주세요.\n")
                    continue

                if len(number) != 11 :
                    print("잘못된 번호입니다. 11자리 숫자를 입력해 주세요.\n")
                    continue

                if not number.isdigit() :
                    print("숫자만 입력 가능합니다. 다시 입력해 주세요.\n")
                    continue

                #파일 저장하기
                addressbook[final_name] = number

                with open("addressbook.json", "w", encoding = "utf-8")as f :
                    json.dump(addressbook, f, ensure_ascii = False, indent = 4)
                
                break
            print()
            print("주소록이 저장되었습니다.")
            print()
    #수정
    if a == "수정" :

        if not addressbook :
            print("\n수정할 주소록이 없습니다.\n")

        else :
            while True :
                keys = sorted(addressbook.keys())
                for i, key in enumerate(keys, start = 1) :
                    display_name = key.rstrip("0123456789")
                    print(f"{i}번. {display_name} : {addressbook[key]}")

                choice = input("수정할 주소록  번호를 선택하세요. (작업을  종료하려면 '이전') :")

                if choice == "이전" :
                    break

                if not choice.isdigit() :
                    print("숫자만 입력해 주세요.\n")
                    continue

                idx = int(choice) - 1

                if idx < 0 or idx >= len(keys) :
                    print("목록에 있는 번호를 입력하세요.\n")
                    continue

                target = keys[idx]
                modify = input("수정할 항목을 입력하세요 (이름, 전화번호) :")

                if modify == "이름" :
                    new_name = input("이름을 입력하세요 :")
                    if new_name == "" :
                        print("잘못된 입력입니다.\n")
                        continue

                    count = 1
                    new_key = f"{new_name}{count}"
                    while new_key in addressbook :
                        count += 1
                        new_key = f"{new_name}{count}"

                    current_number = addressbook[target]
                    del addressbook[target]
                    addressbook[new_key] = current_number
                    print("이름이 수정되었습니다.")

                if modify == "전화번호" :
                    new_number = input("새로운 전화번호를 입력하세요. (- 제외 11자리) :")
                
                    if len(new_number) == 11 and new_number.isdigit() :
                        addressbook[target] = new_number
                        print("전화번호가 수정되었습니다.")
                
                    else :
                        print("잘못된 번호 형식입니다.\n")
                        continue

                with open("addressbook.json", "w", encoding = "utf-8")as f :
                    json.dump(addressbook, f, ensure_ascii = False, indent = 4)

                break


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
            print("저장된 주소록\n")
            for key in sorted_addressbook :
                display_name = key.rstrip("0123456789")
                print('{} : {}'.format(display_name, sorted_addressbook[key]))#모든 사람의 주소록
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
                
                if c == "이전" :
                    break

                if c == "" :
                    print("잘못된 입력입니다. 다시 입력해 주세요.")
                    continue
                
                found = False
                for key in addressbook :
                    if c in key :
                        display_name = key.rstrip("0123456789")
                        print(f"{display_name} : {addressbook[key]}")
                        found = True

                if not found :
                    print(f"{c}님은 등록되어 있지 않습니다.")
                
                print()

    #삭제
    if a == "삭제" :
        if not addressbook :
            print("\n저장된 주소록이 없습니다.\n")

        else :
            while True :
                print("저장된  주소록\n")
                sorted_addressbook = dict(sorted(addressbook.items()))
                for key in sorted_addressbook :
                    display_name = key.rstrip("0123456789")
                    print(f'{display_name} : {sorted_addressbook[key]}')
                print()
                d = input("삭제할 사람의 이름 (작업을 종료하려면 '이전') :")
                print()

                if d == "이전" :
                    break
                
                if d == "" :
                    print("잘못된 입력입니다. 다시 입력해 주세요.")
                    print()
                    continue

                found_keys = []
                found = False

                for key in addressbook :
                    if d in key :
                        found_keys.append(key)
                        display_name = key.rstrip("0123456789")
                        print(f"{len(found_keys)}번. {display_name} : {addressbook[key]}")
                        found = True
                if not found :
                    print(f"{d}님을 찾을 수 없습니다.")
                    continue

                choice = input("삭제할 주소록  번호를 선택하세요. (작업을  종료하려면 '이전') :")

                if choice == "이전" :
                    continue
                
                if choice.isdigit() :
                    idx = int(choice) - 1
                    if 0 <= idx < len(found_keys) :
                        target = found_keys[idx]
                        del addressbook[target]
                    
                        with open("addressbook.json", "w", encoding = "utf-8")as f :
                            json.dump(addressbook, f, ensure_ascii = False, indent = 4)

                        print("삭제되었습니다.")
                        print()
                        break

    #종료
    if a == "종료" :
        print()
        print("종료합니다.")
        break



 # !!! 동명이인일 경우 어떻게 해야 하는지 아직 난제임 --> value 값을 list로 바꾸면 해결
 # !!! 그냥 엔터를 쳤을 때 잘못된 입력입니다. 하고 리턴할 수 있게 다시 만들기
 # !!! 추가 파트만 조금 더 세분화 하면 될 듯 ! 나머지는 괜찮다.
