from .core import MonthlyHistory
from .utils import _check_in_out
import csv


class CreateAccountBook(MonthlyHistory):
    """CSV 내보내기 기능이 추가된 한 달 가계부 클래스"""

    def __init__(self, month: int):
        super().__init__(month)

    def in_out_check(self):
        return _check_in_out(super().get_history())

    def make_csv(self):
        """만들어진 객체를 조회하여 csv 파일을 만듭니다."""

        rows = ['날짜', '수입', '지출', "카테고리", "메모"]
        check_in_out = self.in_out_check()
        with open(f'{self.month}월_가계부.csv', 'w', newline='', encoding='utf-8-sig') as f:

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
