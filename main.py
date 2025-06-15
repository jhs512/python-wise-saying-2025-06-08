last_id = 0
wise_sayings = []

class WiseSaying:
    def __init__(self, id, content, author):
        self.id = id
        self.content = content
        self.author = author

    def __str__(self):
        return f"WiseSaying(id={self.id}, content='{self.content}', author='{self.author}')"

def find_by_id(id):
    for wise_saying in wise_sayings:
        if wise_saying.id == id:
            return wise_saying
    return None

print("== 명언 앱 ==")

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
    elif cmd.startswith("삭제?id="):
        id = int(cmd.split("?id=")[1])

        found_wise_saying = find_by_id(id)

        if found_wise_saying is None:
            print(f"{id}번 명언은 존재하지 않습니다.")
            continue

        wise_sayings.remove(found_wise_saying)

        print(f"{id}번 명언이 삭제되었습니다.")
    elif cmd.startswith("수정?id="):
        id = int(cmd.split("?id=")[1])

        found_wise_saying = find_by_id(id)

        if found_wise_saying is None:
            print(f"{id}번 명언은 존재하지 않습니다.")
            continue

        print(f"명언(기존) : {found_wise_saying.content}")
        print("명언 : ", end="")
        content = input()

        print(f"작가(기존) : {found_wise_saying.author}")
        print("작가 : ", end="")
        author = input()

        found_wise_saying.content = content
        found_wise_saying.author = author

        print(f"{id}번 명언이 수정되었습니다.")