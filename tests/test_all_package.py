import os
import pytest
from my_package.core import MonthlyHistory
from my_package.subclass import CreateAccountBook
from my_package.utils import _check_in_out


# --- 1. core.py (MonthlyHistory) 테스트 ---
def test_add_history_and_get_history():
    """
    MonthlyHistory.add_history 및 get_history 기능 테스트.

    Given: 5월 데이터를 관리하는 MonthlyHistory 객체 생성
    When: 거래 내역을 하나 추가했을 때
    Then: get_history() 호출 시 올바른 데이터 구조(딕셔너리)가 리스트에 담겨 반환되는지 확인합니다.

    Example:
        >>> history = MonthlyHistory(month=5)
        >>> history.add_history(
            day=15, amount=-10000, category="식비", memo="점심값")
        >>> len(history.get_history())
        1
        >>> history.get_history()[0]['amount']
        -10000
    """
    history = MonthlyHistory(month=5)
    history.add_history(day=15, amount=-10000, category="식비", memo="점심값")

    data = history.get_history()

    assert len(data) == 1
    assert data[0]["month"] == 5
    assert data[0]["day"] == 15
    assert data[0]["amount"] == -10000
    assert data[0]["category"] == "식비"
    assert data[0]["description"] == "점심값"


def test_calculate_total():
    """
    MonthlyHistory.calculate_total의 합산 기능 테스트.

    Given: 5월 데이터를 관리하는 MonthlyHistory 객체 생성 후
    When: 수입(+50000)과 지출(-20000, -5000)을 각각 추가했을 때
    Then: 모든 내역의 합산 금액이 25,000원이 맞는지 확인합니다.

    Example:
        >>> history = MonthlyHistory(month=5)
        >>> history.add_history(day=1, amount=50000, category="용돈", memo="정기")
        >>> history.add_history(day=2, amount=-20000, category="쇼핑", memo="옷")
        >>> history.calculate_total()
        30000
    """
    history = MonthlyHistory(month=5)
    history.add_history(day=1, amount=50000, category="용돈", memo="정기 용돈")
    history.add_history(day=2, amount=-20000, category="쇼핑", memo="티셔츠")
    history.add_history(day=3, amount=-5000, category="교통비", memo="버스카드 충전")

    total = history.calculate_total()

    assert total == 25000


def test_wrong_calculate_total():
    """
    MonthlyHistory.calculate_total의 잘 못 된 데이터 타입 삽입시 합산 기능 테스트.

    Example:
        >>> history = MonthlyHistory(month=3)
        >>> history.add_history(day=1, amount="사과", category="용돈", memo="정기")
        >>> history.calculate_total()
        계산할 수 없는 잘못된 데이터 타입이 포함되어 있습니다.
    """
    history = MonthlyHistory(month=4)
    history.add_history(day=1, amount="사과", category="용돈", memo="정기 용돈")

    total = history.calculate_total()

    assert total == "계산할 수 없는 잘못된 데이터 타입이 포함되어 있습니다."


def test_get_history_encapsulation():
    """
    get_history 호출 시 원본 리스트 캡슐화(보호) 테스트.

    Given: 거래 내역이 저장된 MonthlyHistory 객체 생성
    When: get_history()를 통해 반환받은 리스트를 외부에서 임의로 수정(clear)했을 때
    Then: 원본 객체 내부의 리스트(__use_history)는 영향을 받지 않고 보존되는지 확인합니다.

    Example:
        >>> history = MonthlyHistory(month=5)
        >>> history.add_history(day=10, amount=-4500, category="식비", memo="커피")
        >>> res = history.get_history()
        >>> res.clear()
        >>> len(history.get_history())
        1
    """
    history = MonthlyHistory(month=5)
    history.add_history(day=10, amount=-4500, category="식비", memo="커피")

    copied_history = history.get_history()
    copied_history.clear()

    assert len(history.get_history()) == 1


# --- 2. utils.py (_check_in_out) 테스트 ---
def test_check_in_out():
    """
    _check_in_out 함수의 양수/음수 판별 기능 테스트.

    Given: 양수(수입)와 음수(지출)가 섞여 있는 가상의 history 리스트 생성
    When: _check_in_out 함수에 리스트를 주입했을 때
    Then: 양수는 True, 음수는 False로 매핑된 불리언 리스트가 올바른 순서로 반환되는지 확인합니다.

    Example:
        >>> mock_data = [{"amount": 5000}, {"amount": -3000}]
        >>> _check_in_out(mock_data)
        [True, False]
    """
    mock_history = [
        {"amount": 10000},
        {"amount": -5000},
        {"amount": -1200}
    ]

    result = _check_in_out(mock_history)

    assert result == [True, False, False]


def test_wrong_check_in_out():
    """
    잘 못 된 데이터 삽입시 발생하는 오류 테스트

    Example:
        >>> wrong_data = [{"amount": 5000}, {"amount": "사과"}]
        >>> _check_in_out(wrong_data)
        데이터 타입을 확인해주세요.
    """
    wrong_data = [
        {"amount": 3000},
        {"amount": -4000},
        {"amount": "사과"}
    ]

    result = _check_in_out(wrong_data)

    assert result == "데이터 타입을 확인해주세요."


# --- 3. subclass.py (CreateAccountBook) 테스트 ---

def test_create_account_book_inheritance():
    """
    CreateAccountBook의 부모 클래스(MonthlyHistory) 기능 상속 및 초기화 테스트.

    Given: CreateAccountBook 객체 생성
    When: 부모의 메서드인 add_history를 사용해 데이터를 추가하고 계산할 때
    Then: 상속받은 변수와 메서드가 정상적으로 동작하는지 확인합니다.

    Example:
        >>> book = CreateAccountBook(month=6)
        >>> book.add_history(day=1, amount=-3000, category="문화", memo="영화")
        >>> book.month
        6
    """
    account_book = CreateAccountBook(month=6)
    account_book.add_history(day=1, amount=-3000, category="문화", memo="영화 영화")

    assert account_book.month == 6
    assert account_book.calculate_total() == -3000


def test_make_csv(tmp_path, monkeypatch):
    """
    CreateAccountBook.make_csv의 CSV 파일 생성 및 포맷팅 기능 테스트.

    Given: 수입과 지출 내역이 존재하는 CreateAccountBook 객체 생성
    When: make_csv() 메서드를 호출하여 파일로 내보낼 때 (tmp_path를 이용해 임시 디렉토리에 생성)
    Then: 지정된 경로에 CSV 파일이 생성되고, 수입/지출 칸이 규칙에 맞게 분리되어 저장되었는지 확인합니다.

    Example:
        >>> book = CreateAccountBook(month=7)
        >>> book.add_history(10, 50000, "기타", "보너스")
        >>> book.make_csv()  # 호출 시 '7월_가계부.csv' 파일 생성됨
    """
    monkeypatch.chdir(tmp_path)

    account_book = CreateAccountBook(month=7)
    account_book.add_history(day=10, amount=50000, category="기타", memo="보너스")
    account_book.add_history(day=11, amount=-15000, category="식비", memo="외식")

    account_book.make_csv()

    expected_file_name = "7월_가계부.csv"
    assert os.path.exists(expected_file_name)

    with open(expected_file_name, "r", encoding="utf-8-sig") as f:
        lines = f.read().splitlines()

    assert lines[0] == "날짜,수입,지출,카테고리,메모"
    assert lines[1] == "7월 10일,50000,0,기타,보너스"
    assert lines[2] == "7월 11일,0,15000,식비,외식"
