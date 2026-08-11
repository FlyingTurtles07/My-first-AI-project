### 첫 번째 AI 프로젝트프로젝트 제목과 설명입니다.

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

> 포인트) &nbsp; input 앞에 int넣어야 함. --> int()는 문자열을 숫자로 바꿔주는 함수  <br>
> &emsp; &emsp; &emsp; prompt_id = int(input("프롬프트 ID: "))  : : input에서 받은 '문자' 가 '숫자' 로 <br>
> 주의 ) int에 문자가 들어가면 오류 생김 --> 나중에 try/except를 사용해 이런 입력 오류도 처리 해 보기


### 10. toggle_favorite() 즐겨찾기 관리 만들기



> 포인트) &nbsp; input 앞에 int넣어야 함. --> int()는 문자열을 숫자로 바꿔주는 함수  <br>
> &emsp; &emsp; &emsp; prompt_id = int(input("프롬프트 ID: "))  : : input에서 받은 '문자' 가 '숫자' 로 <br>
> 주의 ) int에 문자가 들어가면 오류 생김 --> 나중에 try/except를 사용해 이런 입력 오류도 처리 해 보기



















