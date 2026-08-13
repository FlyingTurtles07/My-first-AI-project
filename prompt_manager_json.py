import json

def load_prompts():
    global prompts

    try:
        with open("prompts.json", "r", encoding="utf-8") as file:
            prompts = json.load(file)

    except FileNotFoundError:





def save_prompts():
    with open("prompts.json", "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=4)







prompts = [
    {
        "id": 1,
        "title": "블로그 글 작성",
        "category": "글쓰기",
        "content": "AI를 활용해서 블로그 글을 작성해줘.",
        "favorite": False
    },
    {
        "id": 2,
        "title": "여행 일정 추천",
        "category": "여행",
        "content": "서울 여행 일정을 추천해줘.",
        "favorite": True
    },
    {
        "id": 3,
        "title": "상품 설명 작성",
        "category": "마케팅",
        "content": "온라인 쇼핑몰 상품 설명을 작성해주세여.",
        "favorite": True
        }
]
next_id = 1





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
    print("8. 종료")

show_menu()




    
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
    "favorite": False
    }

    prompts.append(prompt)

    next_id += 1

    print("프롬프트가 추가되었습니다.")


    

    
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

            if prompt["favorite"]:
                favorite_mark = "★"
            else:
                favorite_mark = "☆"

            print(f"ID: {prompt['id']}")
            print(f"제목: {prompt['title']}")
            print(f"카테고리: {prompt['category']}")
            print(f"즐겨찾기: {favorite_mark}")
            print("\n내용:")
            print(prompt["content"])

            break

    if not found:
        print("해당 ID의 프롬프트가 없습니다.")





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






def main():
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
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다")    


    print("당신이 선택한 번호: ", choice)





if __name__ == "__main__":
    main()


