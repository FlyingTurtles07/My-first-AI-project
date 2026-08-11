### 첫 번째 AI 프로젝트프로젝트 제목과 설명입니다.

---
---

# === 나만의 프롬프트 관리 프로그램===

Python으로 만든 콘솔 기반 프롬프트 관리 프로그램입니다.

## 주요 기능

1. 프롬프트 추가
2. 프롬프트 목록
3. 카테고리별 조회
4. 프롬프트 검색
5. 프롬프트 상세 보기
6. 즐겨찾기 관리
7. 즐겨찾기 목록
0. 종료
선택:

## 실행 방법

```bash
python prompt_manager.py
```

---
---

## 진행 과정 

### 1. 먼저 함수로 기능을 나눈다
```
프로그램
│
├── 메뉴 보여주기
├── 프롬프트 추가
├── 프롬프트 목록
├── 카테고리 조회
├── 검색
├── 상세 보기
├── 즐겨찾기 변경
├── 즐겨찾기 목록
└── 프로그램 실행
```

---

### 2. 각각을 함수로 만든다
```
def show_menu():
    pass

def add_prompt():
    pass

def show_list():
    pass

def show_by_category():
    pass

def search_prompt():
    pass

def show_detail():
    pass

def toggle_favorite():
    pass

def show_favorites():
    pass

def main():
    pass
```

---

### 3. show_menu()부터 pass 자리에 각각 항목을 넣는다 (정의만 하면 안나오므로 마지막에 메뉴 호출 넣어줘야 함)

```
def show_menu():
    print("\n========================================")
    print("        프롬프트 관리 프로그램")
    print("========================================")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 종료")


show_menu()
```
---

### 4. main()에 input과 if choice, elif, else 넣어서 완성하기

```
def main():
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
    else:
        print("잘못된 선택입니다.")
```

---

### 5. add_prompt() 만들기 전에 "데이터 저장 구조 만들기"(프롬프트 저장할 공간 만들기)
사용자가 프롬프트를 입력한다 → 저장한다 → 나중에 목록에서 다시 본다 → 검색한다 → 즐겨찾기 한다.

 - prompt 틀 작성 방법
list안에 여러개의 dictionary넣는 방식, list : [  ], dictionary :{  }
예) 
```
prompt = [
    {
        "id": 1,
        "title": "블로그 글 작성",
        "category": "글쓰기",
        "content": "AI를 활용하여 블로그 글을 작성해주세요.",
        "favorite": False
    },
    {
        "id": 2,
        "title": "여행 일정 추천",
        "category": "여행",
        "content": "서울 2박3일 여행 일정을 추천해주세요",
        "favorite": True
    }
]

```

- 주의)  아래 예시처럼 "prompts = []"가 밖에 있어야 하고 아직 프롬프트 없다는 의미, next_id는 1부터 시작할 거란 뜻임.

```
prompts = []
next_id = 1

def show_menu():
    print("\n========================================")
    print("       프롬프트 관리 프로그램")
    print("========================================")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 종료")
    print("========================================")
```

- 실제 add_prompt() 작성  
아래에 global next_id 넣어야 "이 함수에서 사용하는 next_id는 새로 만드는 변수가 아니라, 위에 있는 next_id를 사용할 거야." 라는뜻 

```
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
```
> 포인트) &nbsp; prompts.append(prompt)           
> &emsp; &emsp; &emsp; add_prompt():안에 "global next_id"

---

### 6. show_list() 만들기

```
def show_list():
    print("\n========================================")
    print("             프롬프트 목록               ")
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
```
> 포인트) &nbsp; f-string --> f"이름: {name}"하면 {name} 부분에 실제 값이 들어감  
> &emsp; &emsp;&emsp; 

---

### 7. show_by_category() 카테고리별 조회 만들기

```
def show_by_category():
    category = input("조회할 카테고리: ")

    print("\n========================================")
    print(f"       {category} 카테고리 목록")
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
```
> 포인트) &nbsp;for문 앞에 "found = False", if문 안에 found = True 해야 카테고리랑 같은것만 출력<br>
> &emsp; &emsp;&emsp; if not found:

---

### 8. search_prompt() 프롬프트 검색 만들기

```
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
```
> 포인트) &nbsp; in -->  if keyword in prompt["title"] or keyword in prompt["content"] 제목 or 내용 안에 키워드 있으면<br>
> &emsp; &emsp; &emsp; 나중에 keyword.lower() 해보기 : 영어 대소문자 구별 못하는 경우

- 이번 함수의 흐름
```
  검색어 입력
    ↓
keyword
    ↓
prompts를 하나씩 확인
    ↓
제목에 검색어가 있는가?
    ↓
       또는
    ↓
내용에 검색어가 있는가?
    ↓
YES ─────→ 화면에 출력
 │
NO
 │
다음 프롬프트 확인
    ↓
모든 프롬프트 확인 완료
    ↓
found가 False인가?
    ↓
YES → "검색 결과가 없습니다."
```

---

### 9. show_detail() 프롬프트 상세 보기 만들기
```
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
```

> 포인트) &nbsp; break 의미 : 프롬프트 확인 해서 ID와 같은가? 같으면 상세정보 출력 후 for문 종료  <br>
> &emsp; &emsp; &emsp; input 앞에 int넣어야 함. --> int()는 문자열을 숫자로 바꿔주는 함수 <br>
> &emsp; &emsp; &emsp; prompt_id = int(input("프롬프트 ID: "))  : : input에서 받은 '문자' 가 '숫자' 로 <br>
> 주의 ) int에 문자가 들어가면 오류 생김 --> 나중에 try/except를 사용해 이런 입력 오류도 처리 해 보기

---

### 10. toggle_favorite() 즐겨찾기 관리 만들기
```
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
```


구조를 보면:
```
                 prompts
                    │
        ┌───────────┼────────────┐
        ↓           ↓            ↓
   show_list()  show_detail()  search_prompt()
        │           │            │
        └───────────┼────────────┘
                    │
             favorite 값
                    ↑
                    │
          toggle_favorite()
                    │
              True ↔ False
```

> 포인트) &nbsp; 현재 프로그램에서 show_list(), show_by_category(), search_prompt(), show_detail() 모두 같은 마크 사용  <br>
 ```
if prompt["favorite"]:
    favorite_mark = "★"
else:
    favorite_mark = "☆"
```
> &emsp; &emsp; &emsp; 따라서 toggle_favorite()에서 값을 변경하면 다른 기능에서도 자동으로 바뀐 상태가 표시됨. <br>
> &emsp; &emsp; &emsp; 이게 바로 하나의 데이터를 여러 함수가 함께 사용하게 하는 것을 아는게 중요. <br>
> &emsp; &emsp; &emsp; 나중에 not을 이용해 보기 <br>
> &emsp; &emsp; &emsp; --> prompt["favorite"] = not prompt["favorite"] 이 한줄이 False → True, True → False 해줌

---

### 11. show_favorite() 즐겨찾기 목록 만들기

```
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
```





> 포인트) &nbsp; 기존 가지고 있는 데이터에서 if prompt["favorite"]:로 필터링 <br>
예시)
```
prompts
│
├── ID 1 → favorite = False
├── ID 2 → favorite = True
├── ID 3 → favorite = False
└── ID 4 → favorite = True
```
에서
```
ID 2
ID 4
```
만 골라내기 필터링

> 주의 ) 이대로면 main()은 딱 한번만 실행 함

---

### 12. while 반복문을 이용해서 main()을 완성하기

```
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
```

> 포인트) &nbsp; while True: 로 무한 반복 <br>
> &emsp; &emsp; &emsp; 8번 실행하면 break 로 프로그램 종료 <br>
> &emsp; &emsp; &emsp; 마지막 main()앞에 if __name__ == "__main__": 추가로 종료 전까지 메인 계속 출력 <br>

- 프로그램의 구조
```
main()
 │
 └── while True
       │
       ├── show_menu()
       │
       ├── 1 → add_prompt()
       │
       ├── 2 → show_list()
       │
       ├── 3 → show_by_category()
       │
       ├── 4 → search_prompt()
       │
       ├── 5 → show_detail()
       │
       ├── 6 → toggle_favorite()
       │
       ├── 7 → show_favorite()
       │
       └── 8 → break
```

---
---

# 보너스
## 1. JSON 저장/불러오기 추가

> 포인트) &nbsp; 맨위에 import json 추가 하여 json 모둘 가져오기 <br>
---
> &emsp; &emsp; &emsp; load_prompts() 함수 만들기 : 기존 함수들 위쪽 prompts = [] 위에 추가 <br>
```
def load_prompts():
    global prompts

    try:
        with open("prompts.json", "r", encoding="utf-8") as file:
            prompts = json.load(file)

    except FileNotFoundError:
        prompts = []
```
> &emsp; &emsp; &emsp; global prompts --> 함수 안에서 바깥에 있는 prompts를 수정하겠다 prompts.json <br>
> &emsp; &emsp; &emsp; open --> prompts.json 파일을 "r" 읽기 모드로 열되, 한글 안깨지도록 utf-8형식 사용해서 열어라 <br>
> &emsp; &emsp; &emsp; json.load() --> JSON 파일의 내용을 Python 데이터로 변환해서 prompts에 넣어라 <br>
---
> &emsp; &emsp; &emsp; save_prompts() 함수 만들기 추가 --> 반대로 프로그램에서 데이터를 변경했을 때 JSON 파일에 저장 <br>
```
def save_prompts():
    with open("prompts.json", "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=4)
```
> &emsp; &emsp; &emsp; open --> prompts.json 파일을 "w" 쓰기 하되, 한글 안깨지도록 utf-8형식 사용해서 저장해라 <br>
> &emsp; &emsp; &emsp; json.dump()--> Python의 prompts 데이터를 JSON 형식으로 파일에 저장해라 <br>
> &emsp; &emsp; &emsp; ensure_ascii=False 사용해야 한글이 정상적으로 저장됩 <br>
> &emsp; &emsp; &emsp;indent=4 는 JSON 파일을 보기 좋게 정렬함 <br>


여행 일정 추천


## 2. Markdown 내보내기 추가


> 포인트) &nbsp; while True: 로 무한 반복 <br>
> &emsp; &emsp; &emsp; 8번 실행하면 break 로 프로그램 종료 <br>
> &emsp; &emsp; &emsp; 마지막 main()앞에 if __name__ == "__main__": 추가로 종료 전까지 메인 계속 출력 <br>












