import json

prompts = [
    {
        "id": 1,
        "title": "블로그 글 작성",
        "category": "글쓰기",
        "content": "AI를 활용해서 블로그 글을 작성해줘.",
        "favorite": False,
        "views": 0
    },
    {
        "id": 2,
        "title": "여행 일정 추천",
        "category": "여행",
        "content": "서울 여행 일정을 추천해줘.",
        "favorite": True,
        "views": 0
    },
    {
        "id": 3,
        "title": "상품 설명 작성",
        "category": "마케팅",
        "content": "온라인 쇼핑몰 상품 설명을 작성해주세여.",
        "favorite": True,
        "views": 0
    }
]
next_id = 1

DATA_FILE = "prompts.json"


def show_menu():
    print("\n=======================================")
    print("     나만의 프롬프트 관리 프로그램       ")
    print("=======================================")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 프롬프트 수정")
    print("9. 프롬프트 삭제")
    print("10. 조회수 TOP 목록")
    print("11. 카테고리별 Markdown 내보내기")
    print("12. 종료")


def add_prompt():
    global next_id

    title = input("제목: ")
    category = input("카테고리: ")
    content = input("내용: ")

    prompt = {
        "id": next_id,
        "title": title,
        "category": category,
        "content": content,
        "favorite": False,
        "views": 0
    }

    prompts.append(prompt)

    next_id += 1

    print("프롬프트가 추가되었습니다.")

    save_prompts()


def show_list():

    print("\n========================================")
    print("             프롬프트 목록                ")
    print("========================================")

    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    for prompt in prompts:

        if prompt["favorite"]:
            favorite_mark = "★"
        else:
            favorite_mark = "☆"

        print(f"[{prompt['id']}] {favorite_mark} {prompt['title']}")
        print(f"    카테고리: {prompt['category']}")
        print()


def show_by_category():
    category = input("조회할 카테고리: ")

    print("\n========================================")
    print(f"           {category} 카테고리 목록")
    print("========================================")

    found = False

    for prompt in prompts:

        if prompt["category"] == category:

            if prompt["favorite"]:
                favorite_mark = "★"
            else:
                favorite_mark = "☆"

            print(f"[{prompt['id']}] {favorite_mark} {prompt['title']}")
            print(f"     카테고리: {prompt['category']}")

            found = True

    if not found:
        print("해당 카테고리의 프롬프트가 없습니다.")


def search_prompt():
    keyword = input("검색어: ")

    print("\n========================================")
    print(f"          {keyword} 검색결과")
    print("========================================")

    found = False

    for prompt in prompts:
        if keyword in prompt["title"] or keyword in prompt["content"]:
            found = True

            if prompt["favorite"]:
                favorite_mark = "★"
            else:
                favorite_mark = "☆"

            print(f"[{prompt['id']}] {favorite_mark} {prompt['title']}")
            print(f"     카테고리: {prompt['category']}")
            print()

    if not found:
        print("검색 결과가 없습니다.")


def show_detail():
    prompt_id = int(input("프롬프트 ID: "))

    print("\n========================================")
    print(f"          프롬프트 상세 보기")
    print("========================================")

    found = False

    for prompt in prompts:
        if prompt['id'] == prompt_id:
            found = True

            # 상세 보기를 할 때마다 조회수 1 증가
            prompt["views"] = prompt.get("views", 0) + 1

            if prompt["favorite"]:
                favorite_mark = "★"
            else:
                favorite_mark = "☆"

            print(f"ID: {prompt['id']}")
            print(f"제목: {prompt['title']}")
            print(f"카테고리: {prompt['category']}")
            print(f"즐겨찾기: {favorite_mark}")
            print(f"조회수: {prompt['views']}")
            print("\n내용:")
            print(prompt["content"])

            break

    if not found:
        print("해당 ID의 프롬프트가 없습니다.")
    else:
        save_prompts()


def toggle_favorite():
    prompt_id = int(input("프롬프트 ID: "))

    print("\n========================================")
    print("          즐겨찾기 관리")
    print("========================================")

    found = False

    for prompt in prompts:
        if prompt["id"] == prompt_id:
            found = True

            if prompt["favorite"]:
                prompt["favorite"] = False
                print(f"'{prompt['title']}'을(를) 즐겨찾기에서 해제했습니다.")
            else:
                prompt["favorite"] = True
                print(f"'{prompt['title']}'을(를) 즐겨찾기에 추가했습니다.")

            break

    if not found:
        print("해당 ID의 프롬프트가 없습니다.")
    else:
        save_prompts()


def show_favorite():
    print("\n========================================")
    print("          즐겨찾기 목록")
    print("========================================")

    found = False

    for prompt in prompts:
        if prompt["favorite"]:
            found = True

            print(f"[{prompt['id']}] {prompt['title']}")
            print(f"    카테고리: {prompt['category']}")
            print("    즐겨찾기: ★")
            print()

    if not found:
        print("즐겨찾기한 프롬프트가 없습니다.")


# ---------------- 보너스 2-1. 수정 / 삭제 ----------------

def edit_prompt():
    prompt_id = int(input("수정할 프롬프트 ID: "))

    print("\n========================================")
    print("          프롬프트 수정")
    print("========================================")

    found = False

    for prompt in prompts:
        if prompt["id"] == prompt_id:
            found = True

            print(f"현재 제목: {prompt['title']}")
            new_title = input("새 제목 (변경 없으면 엔터): ")
            if new_title:
                prompt["title"] = new_title

            print(f"현재 카테고리: {prompt['category']}")
            new_category = input("새 카테고리 (변경 없으면 엔터): ")
            if new_category:
                prompt["category"] = new_category

            print(f"현재 내용: {prompt['content']}")
            new_content = input("새 내용 (변경 없으면 엔터): ")
            if new_content:
                prompt["content"] = new_content

            print("수정이 완료되었습니다.")
            break

    if not found:
        print("해당 ID의 프롬프트가 없습니다.")
    else:
        save_prompts()


def delete_prompt():
    prompt_id = int(input("삭제할 프롬프트 ID: "))

    print("\n========================================")
    print("          프롬프트 삭제")
    print("========================================")

    found = False

    for prompt in prompts:
        if prompt["id"] == prompt_id:
            found = True

            confirm = input(f"'{prompt['title']}'을(를) 삭제하시겠습니까? (y/n): ")
            if confirm.lower() == "y":
                prompts.remove(prompt)
                print("삭제되었습니다.")
                save_prompts()
            else:
                print("삭제를 취소했습니다.")

            break

    if not found:
        print("해당 ID의 프롬프트가 없습니다.")


# ---------------- 보너스 2-3. 조회수 TOP 목록 ----------------

def show_top_viewed():
    print("\n========================================")
    print("          조회수 TOP 목록")
    print("========================================")

    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    # views 값을 기준으로 내림차순(많이 본 순) 정렬
    sorted_prompts = sorted(prompts, key=lambda p: p.get("views", 0), reverse=True)

    rank = 1
    for prompt in sorted_prompts[:5]:
        if prompt["favorite"]:
            favorite_mark = "★"
        else:
            favorite_mark = "☆"

        views = prompt.get("views", 0)
        print(f"{rank}위. [{prompt['id']}] {favorite_mark} {prompt['title']} (조회수: {views})")
        rank += 1


# ---------------- 보너스 1-1. JSON 저장 / 불러오기 ----------------

def save_prompts():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)


def load_prompts():
    global prompts, next_id

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            loaded = json.load(f)

        prompts = loaded

        # 불러온 데이터 중 favorite/views 키가 없는 옛날 데이터를 위한 안전장치
        for prompt in prompts:
            if "favorite" not in prompt:
                prompt["favorite"] = False
            if "views" not in prompt:
                prompt["views"] = 0

        if prompts:
            next_id = max(prompt["id"] for prompt in prompts) + 1
        else:
            next_id = 1

        print("저장된 프롬프트를 불러왔습니다.")

    except FileNotFoundError:
        print("저장된 파일이 없어 기본 데이터로 시작합니다.")


# ---------------- 보너스 1-2. 카테고리별 Markdown 내보내기 ----------------

def export_to_markdown():
    print("\n========================================")
    print("       카테고리별 Markdown 내보내기")
    print("========================================")

    if not prompts:
        print("내보낼 프롬프트가 없습니다.")
        return

    # 카테고리별로 프롬프트를 묶는다
    categories = {}
    for prompt in prompts:
        cat = prompt["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(prompt)

    for cat, items in categories.items():
        filename = f"prompts_{cat}.md"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {cat} 프롬프트 목록\n\n")

            for prompt in items:
                mark = "★" if prompt["favorite"] else "☆"
                views = prompt.get("views", 0)

                f.write(f"## [{prompt['id']}] {mark} {prompt['title']}\n\n")
                f.write(f"- 조회수: {views}\n\n")
                f.write(f"{prompt['content']}\n\n")
                f.write("---\n\n")

        print(f"'{filename}' 파일로 내보냈습니다.")


def main():
    load_prompts()

    while True:
        show_menu()

        choice = input("선택: ")

        if choice == "1":
            add_prompt()

        elif choice == "2":
            show_list()

        elif choice == "3":
            show_by_category()

        elif choice == "4":
            search_prompt()

        elif choice == "5":
            show_detail()

        elif choice == "6":
            toggle_favorite()

        elif choice == "7":
            show_favorite()

        elif choice == "8":
            edit_prompt()

        elif choice == "9":
            delete_prompt()

        elif choice == "10":
            show_top_viewed()

        elif choice == "11":
            export_to_markdown()

        elif choice == "12":
            save_prompts()
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다")

    print("당신이 선택한 번호: ", choice)


if __name__ == "__main__":
    main()
