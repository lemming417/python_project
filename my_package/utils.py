def _check_in_out(history_list):
    """csv 파일 저장을 위해 지출과 수입을 분리하기 위해 사용합니다.

    :param history_list: 'amount' 키를 가진 거래 내역 딕셔너리들의 리스트
    :return: 금액이 0보다 크면 Ture, 0 이하면 False로 구성된 리스트

    >>> mock_history = [{'amount': 3000}, {'amount': -1500}]
    >>> _check_in_out(mock_history)
    [True, False]
    """
    result = []
    try:
        for item in history_list:
            if item['amount'] > 0:
                result.append(True)
            else:
                result.append(False)
        return result
    except TypeError:
        return "데이터 타입을 확인해주세요."
