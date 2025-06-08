print("== 명언 앱 ==")

last_id = 0
wise_sayings = []

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

        wise_saying = {
            "id": id,
            "content": content,
            "author": author
        }

        wise_sayings.append(wise_saying)

        print(f"{id}번 명언이 등록되었습니다.")
    elif cmd == "목록":
        print("번호 / 작가 / 명언")
        print("----------------------")

        for wise_saying in wise_sayings:
            print(f"{wise_saying['id']} / {wise_saying['author']} / {wise_saying['content']}")