import json

# 프로그램 시작 시 데이터 불러오기
try:
    with open("addressbook.json", "r", encoding="utf-8") as f:
        addressbook = json.load(f)
except FileNotFoundError:
    addressbook = {}

while True:
    print("--- [메인 메뉴] ---")
    print("1. 추가  2. 조회  3. 검색  4. 수정  5. 삭제  6. 종료")
    a = input("작업을 선택하세요: ")

    # [추가]
    if a == "추가" or a == "1":
        while True:
            raw_name = input("\n이름 (메뉴로 돌아가려면 '이전'): ").strip()
            if raw_name == "이전": break
            if not raw_name:
                print("이름을 입력해 주세요.")
                continue

            final_name = f"{raw_name}1"
            is_cancel = False

            # 중복 이름 확인
            candidates = [k for k in addressbook if k.startswith(raw_name)]

            if candidates:
                print(f"\n'{raw_name}' 님과 유사한 이름이 {len(candidates)}개 있습니다.")
                b = input("1.새로 추가 / 2.기존 정보에 덮어쓰기 / 3.취소: ")
                
                if b == "1":
                    count = 1
                    while f"{raw_name}{count}" in addressbook:
                        count += 1
                    final_name = f"{raw_name}{count}"
                elif b == "2":
                    print(f"\n누구의 정보를 덮어씌울까요?")
                    for i, k in enumerate(candidates, start=1):
                        print(f"{i}번. {k.rstrip('0123456789')} : {addressbook[k]}")
                    
                    choice = input("번호 선택 (취소 '이전'): ")
                    if choice == "이전": is_cancel = True
                    elif choice.isdigit() and 0 < int(choice) <= len(candidates):
                        final_name = candidates[int(choice)-1]
                    else:
                        print("잘못된 선택입니다. 추가를 취소합니다.")
                        is_cancel = True
                else:
                    is_cancel = True

            if is_cancel: continue

            # 전화번호 입력
            while True:
                number = input(f"[{final_name.rstrip('0123456789')}] 전화번호 (11자리, '이전' 시 취소): ").strip()
                if number == "이전":
                    is_cancel = True
                    break
                if len(number) == 11 and number.isdigit():
                    addressbook[final_name] = number
                    with open("addressbook.json", "w", encoding="utf-8") as f:
                        json.dump(addressbook, f, ensure_ascii=False, indent=4)
                    print(f"'{final_name.rstrip('0123456789')}' 저장 완료\n")
                    is_cancel = False
                    break
                else:
                    print("잘못된 번호 형식입니다. 다시 입력해 주세요.")
            
            if not is_cancel: break

    # [조회]
    elif a == "조회" or a == "2":
        print("\n--- [전체 주소록] ---")
        if not addressbook:
            print("저장된 주소록이 없습니다.")
        else:
            sorted_keys = sorted(addressbook.keys())
            for key in sorted_keys:
                display_name = key.rstrip("0123456789")
                print(f"{display_name} : {addressbook[key]}")
        print()

    # [검색]
    elif a == "검색" or a == "3":
        if not addressbook:
            print("\n저장된 데이터가 없습니다.\n")
            continue
        while True:
            c = input("\n찾는 이름 (메뉴로 '이전'): ").strip()
            if c == "이전": break
            if not c: continue

            found = False
            for key in addressbook:
                if c in key:
                    print(f"{key.rstrip('0123456789')} : {addressbook[key]}")
                    found = True
            if not found:
                print(f"'{c}'님은 등록되어 있지 않습니다.")

    # [수정]
    elif a == "수정" or a == "4":
        if not addressbook:
            print("\n수정할 데이터가 없습니다.\n")
            continue
        while True:
            keys = sorted(addressbook.keys())
            for i, key in enumerate(keys, start=1):
                print(f"{i}번. {key.rstrip('0123456789')} : {addressbook[key]}")
            
            choice = input("\n수정할 번호 (메뉴로 '이전'): ")
            if choice == "이전": break
            if not choice.isdigit() or not (0 < int(choice) <= len(keys)):
                print("잘못된 번호입니다.")
                continue

            target = keys[int(choice)-1]
            mode = input("수정 항목 (1.이름 / 2.전화번호): ")

            if mode == "1" or mode == "이름":
                new_name = input("새 이름: ").strip()
                if not new_name: continue
                count = 1
                new_key = f"{new_name}{count}"
                while new_key in addressbook:
                    count += 1
                    new_key = f"{new_name}{count}"
                
                num = addressbook[target]
                del addressbook[target]
                addressbook[new_key] = num
                print("이름 수정 완료")
            elif mode == "2" or mode == "전화번호":
                new_num = input("새 번호 (11자리): ").strip()
                if len(new_num) == 11 and new_num.isdigit():
                    addressbook[target] = new_num
                    print("전화번호 수정 완료")
                else:
                    print("형식이 잘못되었습니다.")
                    continue
            
            with open("addressbook.json", "w", encoding="utf-8") as f:
                json.dump(addressbook, f, ensure_ascii=False, indent=4)
            break

    # [삭제]
    elif a == "삭제" or a == "5":
        if not addressbook:
            print("\n삭제할 데이터가 없습니다.\n")
            continue
        print("\n--- [전체 주소록] ---")
        if not addressbook:
            print("저장된 주소록이 없습니다.")
        else:
            sorted_keys = sorted(addressbook.keys())
            for key in sorted_keys:
                display_name = key.rstrip("0123456789")
                print(f"{display_name} : {addressbook[key]}")
        print()

        while True:
            d = input("\n삭제할 이름 (메뉴로 '이전'): ").strip()
            if d == "이전": break
            if d == "" :
                print("잘못된 입력입니다.")
                continue
            
            found_keys = [k for k in addressbook if d in k]
            if not found_keys:
                print(f"'{d}'님을 찾을 수 없습니다.")
                continue

            for i, k in enumerate(found_keys, start=1):
                print(f"{i}번. {k.rstrip('0123456789')} : {addressbook[k]}")
            
            choice = input("\n삭제할 번호 선택 (취소 '이전'): ")
            if choice == "이전": continue
            if choice.isdigit() and 0 < int(choice) <= len(found_keys):
                target = found_keys[int(choice)-1]
                del addressbook[target]
                with open("addressbook.json", "w", encoding="utf-8") as f:
                    json.dump(addressbook, f, ensure_ascii=False, indent=4)
                print("삭제되었습니다.")
                break
            else:
                print("잘못된 번호입니다.")

    # [종료]
    elif a == "종료" or a == "6":
        print("\n종료합니다.")
        break

    else:
        print("\n잘못된 선택입니다. 메뉴 번호를 입력해 주세요.\n")
