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
## 1-1. JSON 저장/불러오기 추가

핵심 개념: 프로그램을 껐다 켜도 데이터가 사라지지 않게 하려면, 메모리에 있는 prompts 리스트를 파일에 "저장"하고, 프로그램 시작할 때 파일에서 "불러와야" 합니다. 파이썬의 json 모듈을 쓰면 리스트/딕셔너리를 그대로 파일로 저장할 수 있어요.

### 1. 파일 맨 위에 import json을 추가하세요.
```
import json

DATA_FILE = "prompts.json"

def save_prompts():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)
    print("프롬프트를 저장했습니다.")

def load_prompts():
    global prompts, next_id
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            prompts = json.load(f)
        # 기존 데이터 중 가장 큰 id + 1을 다음 id로 설정
        if prompts:
            next_id = max(p["id"] for p in prompts) + 1
        print("프롬프트를 불러왔습니다.")
    except FileNotFoundError:
        print("저장된 파일이 없어 기본 데이터로 시작합니다.")
```
> 포인트) &nbsp; 맨위에 import json 추가 하여 json 모둘 가져오기 <br>

> ensure_ascii=False: 이게 없으면 한글이 \uac00 같은 유니코드 코드로 저장돼서 파일을 열어봐도 읽을 수가 없어요.

> indent=2: 사람이 읽기 좋게 들여쓰기해서 저장.

> try/except FileNotFoundError: 프로그램을 처음 실행하면 prompts.json 파일이 아직 없겠죠? 그때 에러 대신 기본값으로 시작하게 해주는 안전장치입니다.

> 저장 시점: add_prompt(), toggle_favorite()처럼 데이터를 바꾸는 함수 끝에 save_prompts()를 호출하거나, 아니면 main()에서 종료(8) 선택 시 한 번만 호출해도 됩니다. 초보자에게는 "데이터가 바뀔 때마다 저장"이 더 안전하고 이해하기 쉬워요.

> 불러오기 시점: if __name__ == "__main__": 아래, main() 호출 직전에 load_prompts() 한 번 실행.

---
### 2. save_prompts() 함수 만들기 추가 --> 반대로 프로그램에서 데이터를 변경했을 때 JSON 파일에 저장
```
def save_prompts():
    with open("prompts.json", "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=4)
```
> &emsp; &emsp; &emsp; open --> prompts.json 파일을 "w" 쓰기 하되, 한글 안깨지도록 utf-8형식 사용해서 저장해라 <br>
> &emsp; &emsp; &emsp; json.dump()--> Python의 prompts 데이터를 JSON 형식으로 파일에 저장해라 <br>
> &emsp; &emsp; &emsp; ensure_ascii=False 사용해야 한글이 정상적으로 저장됩 <br>
> &emsp; &emsp; &emsp;indent=4 는 JSON 파일을 보기 좋게 정렬함 <br>


---
### 3. load_prompts() 함수 만들기 : 기존 함수들 위쪽 prompts = [] 위에 추가
```
def load_prompts():
    global prompts, next_id
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            prompts = json.load(f)
        # 기존 데이터 중 가장 큰 id + 1을 다음 id로 설정
        if prompts:
            next_id = max(p["id"] for p in prompts) + 1
        print("프롬프트를 불러왔습니다.")
    except FileNotFoundError:
        print("저장된 파일이 없어 기본 데이터로 시작합니다.")


        prompts = []
```
> &emsp; &emsp; &emsp; global prompts --> 함수 안에서 바깥에 있는 prompts를 수정하겠다 prompts.json <br>
> &emsp; &emsp; &emsp; open --> prompts.json 파일을 "r" 읽기 모드로 열되, 한글 안깨지도록 utf-8형식 사용해서 열어라 <br>
> &emsp; &emsp; &emsp; json.load() --> JSON 파일의 내용을 Python 데이터로 변환해서 prompts에 넣어라 <br>
---



### 1-2. 카테고리별 Markdown 파일로 내보내기

핵심 개념: 같은 카테고리끼리 묶어서 각각 .md 파일로 만드는 겁니다. "카테고리별로 묶는다"는 것은 딕셔너리를 활용하면 편해요.

```
def export_to_markdown():
    if not prompts:
        print("내보낼 프롬프트가 없습니다.")
        return

    # 카테고리별로 묶기
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
            for p in items:
                mark = "★" if p["favorite"] else "☆"
                f.write(f"## [{p['id']}] {mark} {p['title']}\n\n")
                f.write(f"{p['content']}\n\n")
                f.write("---\n\n")
        print(f"'{filename}' 파일로 내보냈습니다.")
```
> categories.setdefault(cat, []).append(prompt)처럼 한 줄로 줄일 수도 있지만, 초보자에겐 if cat not in categories: 방식이 눈에 더 잘 들어옵니다.

> 마크다운 문법: #은 큰 제목, ##은 작은 제목, ---은 구분선. .md 파일을 열어보면 이 기호들이 자동으로 서식으로 변환돼서 보여요 (GitHub이나 VS Code 미리보기에서 확인해보세요).

> 파일명에 공백이나 특수문자가 들어간 카테고리가 있으면 파일 생성이 실패할 수 있으니, 궁금하면 cat.replace(" ", "_") 같은 처리를 추가로 시도해봐도 좋아요 (심화 학습용 힌트로만 언급).



## 2-1. 프롬프트 수정/삭제 (CRUD의 U, D)

수정(Update): 기존 값을 보여주고, 사용자가 엔터만 치면 "그대로 유지", 새로 입력하면 "값 교체"하는 패턴이 실무에서도 많이 쓰입니다.

```
def edit_prompt():
    prompt_id = int(input("수정할 프롬프트 ID: "))

    for prompt in prompts:
        if prompt["id"] == prompt_id:
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
            return

    print("해당 ID의 프롬프트가 없습니다.")
```

- 삭제(Delete): 실수로 지우는 걸 막기 위해 꼭 "정말 삭제하시겠습니까?" 확인을 넣어주세요.

```
def delete_prompt():
    prompt_id = int(input("삭제할 프롬프트 ID: "))

    for prompt in prompts:
        if prompt["id"] == prompt_id:
            confirm = input(f"'{prompt['title']}'을(를) 삭제하시겠습니까? (y/n): ")
            if confirm.lower() == "y":
                prompts.remove(prompt)
                print("삭제되었습니다.")
            else:
                print("삭제를 취소했습니다.")
            return

    print("해당 ID의 프롬프트가 없습니다.")
```

설명 포인트:

> for ... in prompts: 루프 안에서 prompts.remove(prompt)를 하고 바로 return으로 루프를 빠져나가는 게 중요해요. 루프를 계속 돌면서 리스트를 수정하면 인덱스가 꼬여서 버그가 날 수 있습니다 (심화 개념이라 지금은 "찾자마자 바로 return" 정도로만 이해해도 충분).

> 기존 코드의 if prompt["favorite"]: 패턴과 통일감 있게 for + if + return 구조를 그대로 따라갔습니다.



## 2-2. 조회수(사용 횟수) 기록

핵심 개념: 데이터에 새로운 항목 "views": 0을 추가하고, 상세 보기를 할 때마다 1씩 늘리면 됩니다.

먼저 prompts 초기 데이터와 add_prompt() 함수에 "views": 0을 추가하세요:
```
prompt = {
    "id": next_id,
    "title": title,
    "category": category,
    "content": content,
    "favorite": False,
    "views": 0
}
```
- 그리고 show_detail() 함수의 found = True 다음 줄에 이렇게 추가:
- ```
  def show_detail():
    prompt_id = int(input("프롬프트 ID: "))
    ...
    for prompt in prompts:
        if prompt['id'] == prompt_id:
            found = True
            prompt["views"] += 1   # ← 이 줄 추가

            ...
            print(f"조회수: {prompt['views']}")   # 출력에도 추가
  ```

  설명 포인트:

> 기존에 저장된 프롬프트(초기 데이터 3개)에는 "views" 키가 없기 때문에, JSON을 이미 저장해서 쓰고 있다면 prompt.get("views", 0)처럼 안전하게 접근하는 습관도 알려주면 좋아요. get()은 키가 없을 때 에러 대신 기본값(0)을 돌려줍니다.


## 2-3. 조회수 기준 정렬 (Top 목록)

핵심 개념: 파이썬의 sorted() 함수와 key 매개변수를 씁니다. key에는 "무엇을 기준으로 정렬할지"를 함수(보통 람다)로 알려줍니다.

```
def show_top_viewed():
    print("\n========================================")
    print("          조회수 TOP 목록")
    print("========================================")

    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    # views 기준 내림차순 정렬 (많이 본 순)
    sorted_prompts = sorted(prompts, key=lambda p: p.get("views", 0), reverse=True)

    for rank, prompt in enumerate(sorted_prompts[:5], start=1):
        mark = "★" if prompt["favorite"] else "☆"
        views = prompt.get("views", 0)
        print(f"{rank}위. [{prompt['id']}] {mark} {prompt['title']} (조회수: {views})")
```
설명 포인트:

> sorted(리스트, key=..., reverse=True): reverse=True면 큰 값이 먼저 오도록(내림차순) 정렬. 원본 prompts 리스트는 건드리지 않고 새 정렬된 리스트를 만들어 반환해요 (prompts.sort()와의 차이 — sort()는 원본을 직접 바꿔버립니다).

> lambda p: p.get("views", 0): "리스트의 각 항목(p)에서 views 값을 꺼내서 그걸 기준으로 정렬해줘"라는 뜻. def로 함수를 따로 만들 수도 있지만, 이렇게 짧은 건 람다로 한 줄에 쓰는 게 관례입니다.

> enumerate(리스트, start=1): 순위(1위, 2위, ...)를 매기고 싶을 때 자주 쓰는 패턴. sorted_prompts[:5]로 상위 5개만 잘라서 보여줍니다.


- 메뉴에 통합하기

show_menu()와 main()의 if/elif 체인에 새 항목들을 추가하면 됩니다:
```
def show_menu():
    print("...")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 프롬프트 수정")
    print("9. 프롬프트 삭제")
    print("10. 조회수 TOP 목록")
    print("11. 카테고리별 Markdown 내보내기")
    print("12. 종료")
```
> 번호가 늘어나니 main()의 elif choice == "8": 이후 번호들도 한 칸씩 밀어서 맞춰줘야 합니다. 그리고 main() 함수 진입 전에 load_prompts()를, choice == "종료" 브랜치에서 save_prompts()를 호출하도록 연결하면 전체 기능이 하나로 이어집니다.

---
---
---
# 보너스 모두 포함한 prompt_manager_bonus

```
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
```
> 바뀐 점 요약이에요:

> 메뉴 8~11번이 추가돼서 수정/삭제/조회수 TOP/Markdown 내보내기를 쓸 수 있어요. (기존 8번 "종료"는 12번으로 밀렸습니다)

> 모든 프롬프트에 "views": 0이 추가됐고, show_detail()(상세 보기)을 할 때마다 자동으로 1씩 올라가요.

> 데이터를 바꾸는 함수(add_prompt, edit_prompt, delete_prompt, toggle_favorite, show_detail) 끝에서 save_prompts()를 호출해서, 작업할 때마다 자동으로 prompts.json에 저장돼요. 프로그램을 다시 켜면 main() 시작할 때 load_prompts()가 그 파일을 불러옵니다.

> export_to_markdown()은 실행하면 카테고리 개수만큼 prompts_카테고리명.md 파일이 생성돼요 (예: prompts_여행.md).




---
---
---











