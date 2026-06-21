class MonthlyHistory:
    """한 달 거래 내역을 관리하는 클래스입니다.

    :ivar month: 가계부를 작성할 대상 월 (1 ~ 12).
    :ivar __use_history: list 거래 내역 딕셔너리를 저장하는 비공개 리스트

    >>> history = MonthlyHistory(month=5)
    >>> histroy.month
    5
    """
    def __init__(self, month: int):
        """MonthlyHistory 클래스의 생성자 입니다.

        :param month: 가계부를 기록할 월
        """
        self.month = month
        self.__use_history = []

    def add_history(self, day, amount, category, memo):
        """거래 내역을 딕셔너리 형태로 저장합니다.

        :param day: 거래가 발생한 날짜 (일).
        :param amount: 거래 금액 (양수는 수입, 음수는 지출).
        :param category: 거래 분류 (예: '식비', '교통비').
        :param memo: 거래에 대한 간단한 설명 또는 메모.

        >>> history = MonthlyHistory(month=5)
        >>> history.add_history(
            day=15, amount=-10000,
            category="식비", memo="점심값")
        >>> len(history.gethistory())
        1
        """
        history_item = {
            "month": self.month,
            "day": day,
            "amount": amount,
            "category": category,
            "description": memo
        }

        self.__use_history.append(history_item)

    def calculate_total(self):
        """한 달간 거래 내역을 합산하여 리턴하는 함수입니다.

        :return: 거래 내역의 총합

        >>> history = MonthlyHistory(month=5)
        >>> history.add_history(1, 50000, "용돈", "정기 용돈")
        >>> history.add_history(2, -20000, "쇼핑", "티셔츠")
        >>> history.calculate_total()
        30000
        """

        return sum(item['amount'] for item in self.__use_history)

    def get_history(self):
        """내부 거래 내역 리스트의 복사본을 반환합니다.

        use_history에 직접적으로 접근하는 것을 막기 위해 사용합니다.

        :return: 저장된 거래 내역 딕셔너리들이 담긴 리스트의 복사본.

        >>> history = MonthlyHistory(month=5)
        >>> history.add_history(10, -4500, "식비", "커피")
        >>> copied = history.get_history()
        >>> copied = copied.clear()
        >>> len(history.get_history())
        1
        """

        return self.__use_history.copy()
