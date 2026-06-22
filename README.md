# 패키지 만들기


## 프로젝트 개요

한 달 간의 거래 내역을 관리하는 객체를 만들고 내용을 추가하여 csv 파일로 출력하는 패키지 입니다.

## 패키지 설치 방법

* 파일을 다운 받은 뒤 압축을 해제하고 해당 경로에서 터미널을 열고 아래와 같이 실행한다.
```sh
pip install .
```


## 빠른 시작(quick start)

패키지를 설치 했다면 다음 코드를 이용하여 한 달 가계부를 생성하고 CSV파일로 내보낼 수 있습니다.
```sh
from my_package.subclass import CreateAccountBook

# 1. 5월 가계부 객체 생성
account_book = CreateAccountBook(month=5)

# 2. 거래 내역 추가
account_book.add_history(day=1, amount=50000, category="용돈", memo="정기 용돈")
account_book.add_history(day=2, amount=-20000, category="쇼핑", memo="티셔츠")
account_book.add_history(day=3, amount=-4500, category="식비", memo="커피")

# 3. 현재까지의 총합 계산 및 출력
print(f"5월 총 합계: {account_book.calculate_total()}원")

# 4. CSV 파일로 내보내기 ('5월_가계부.csv' 파일이 생성됨)
account_book.make_csv()
```


## 주요 기능 설명

* **가계부 데이터 관리 및 합산** (MonthlyHistory)

    * add_history: 날짜, 금액, 카테고리, 메모를 딕셔너리 형태로 안전하게 구조화하여 누적 저장합니다.

    * calculate_total: 누적된 모든 수입과 지출을 합산하여 현재 잔액을 리턴합니다. 문자열 등 잘못된 데이터 타입이 유입되는 엣지 케이스 발생 시 예외 처리가 적용되어 있습니다.

    * get_history: 데이터 무결성을 위해 원본 리스트 대신 복사본을 반환하여 캡슐화를 유지합니다.

* **CSV 파일 포맷팅 내보내기** (CreateAccountBook)

    * make_csv: 수입 금액과 지출 금액을 별도의 열(Column)로 정교하게 분리하여 저장합니다.

    * 지출 금액(음수)은 시각적 편의를 위해 마이너스 기호가 제거된 절대값으로 변환되어 기록됩니다.

    * Excel 등에서 한글이 깨지는 현상을 방지하기 위해 utf-8-sig 인코딩 사양을 준수합니다.
    

## 테스트 실행 방법
프로젝트의 최상위 디렉터리에서 아래 명령어를 실행합니다.
```sh
python -m pytest
```

**테스트 결과 예시**
```planintext
================================================= test session starts =================================================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\a\Desktop\WorkSpace\my_project
collected 8 items

tests\test_all_package.py ........                                                                               [100%]

================================================== 8 passed in 0.05s ==================================================
```


## 작성자 정보
[Git Hub 저장소 URL] (https://github.com/lemming417/python_project)
