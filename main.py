class WiseSaying:
    def __init__(self, id, content, author):
        self.id = id
        self.content = content
        self.author = author

    def __str__(self):
        return f"WiseSaying(id={self.id}, content='{self.content}', author='{self.author}')"

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

        wise_saying = WiseSaying(id, content, author)

        wise_sayings.append(wise_saying)

        print(f"{id}번 명언이 등록되었습니다.")
    elif cmd == "목록":
        print("번호 / 작가 / 명언")
        print("----------------------")

        for wise_saying in wise_sayings:
            print(f"{wise_saying.id} / {wise_saying.author} / {wise_saying.content}")
    elif cmd == "삭제?id=1":
        id = 1

        found_wise_saying = None

        for wise_saying in wise_sayings:
            if wise_saying.id == id:
                found_wise_saying = wise_saying
                break

        wise_sayings.remove(found_wise_saying)

        print("1번 명언이 삭제되었습니다.")