def _check_in_out(history_list):
    """csv 파일 저장을 위해 지출과 수입을 분리하기 위해 사용합니다."""
    result = []
    for item in history_list:
        if item['amount'] > 0:
            result.append(True)
        else:
            result.append(False)
    return result
