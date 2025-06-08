print("== 명언 앱 ==")

last_id = 0

while True:
    print("명언) ", end="")
    cmd = input()

    if cmd == "종료":
        print("명언 앱을 종료합니다.")
        break
    elif cmd == "등록":
        print("명언 : ", end="")
        content = input()
        print("작가 : ", end="")
        author = input()
        last_id += 1
        id = last_id
        print(f"{id}번 명언이 등록되었습니다.")
