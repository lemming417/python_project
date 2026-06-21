from .core import MonthlyHistory
from .utils import _check_in_out
import csv


class CreateAccountBook(MonthlyHistory):
    """CSV 내보내기 기능이 추가된 한 달 가계부 클래스입니다.
    MonthlyHistory 클래스를 상속받습니다.

    >>> book = CreateAccountBook(month=6)
    >>> isinstance(book, MonthlyHistory)
    True
    """

    def __init__(self, month: int):
        """CreateAccountBook 클래스의 생성자 입니다. 부모 클래스의 생성자를 호출합니다.

        :param month: 가계부를 기록할 월.
        """
        super().__init__(month)

    def in_out_check(self):
        """현재까지 기록된 거래 내역들이 수입인지 지출인지 판별합니다.

        :return: 각 거래 내역의 양수/음수 여부가 매핑된 불리언 리스트.
        >>> book = CreateAccountBook(month=6)
        >>> book.add_history(1, 10000, "수입", "알바")
        >>> book.add_history(2, -5000, "지출", "책")
        [True, False]
        """
        return _check_in_out(super().get_history())

    def make_csv(self):
        """현재 가계부 객체에 저장된 데이터를 기반으로 'N월_가계부.csv' 파일을 생성합니다.

        수입과 지출을 별도의 열로 분리하여 저장하고
        지출 금액은 음수 기호를 제거하여 절대값으로 기록합니다.
        한글이 깨지지 않도록 'utf-8-sig' 인코딩을 사용합니다.

        >>> book = CreateAccountBook(month=7)
        >>> book.add_history(10, 50000, "기타", "보너스")
        >>> book.make_csv()  # 로컬 디렉터리에 '7월_가계부.csv' 파일이 생성됨
        """

        rows = ['날짜', '수입', '지출', "카테고리", "메모"]
        check_in_out = self.in_out_check()
        with open(
                f'{self.month}월_가계부.csv', 'w', newline='', encoding='utf-8-sig'
                ) as f:

            writer = csv.writer(f)
            writer.writerow(rows)

            for item in self.get_history():
                data = list(item.values())
                if check_in_out.pop():
                    data[2] = abs(data[2])
                    data.insert(2, 0)
                    writer.writerow(
                        [f'{data[0]}월 {data[1]}일',
                         data[2], data[3], data[4], data[5]]
                        )
                else:
                    data.insert(3, 0)
                    writer.writerow(
                        [f'{data[0]}월 {data[1]}일',
                         data[2], data[3], data[4], data[5]]
                        )
