class MonthlyHistory:
    """한 달 거래 내역을 관리하는 클래스

    :param month: 작성할 월

    :ivar month: int
    :ivar __use_history: list
    """
    def __init__(self, month: int):
        self.month = month
        self.__use_history = []

    def add_history(self, day, amount, category, memo):
        """거래 내역을 딕셔너리 형태로 저장합니다.

        :param day: 사용한 날짜 기록
        :param amount: 거래 내역
        :param category: 거래 분류
        :param memo: 간단한 설명
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
        """

        return sum(item['amount'] for item in self.__use_history)

    def get_history(self):
        """use_history에 직접적으로 접근하는 것을 막기 위해 사용합니다."""

        return self.__use_history.copy()
