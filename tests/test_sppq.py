from sppq import printt, cl, bigtext, percent, pbar, pbarupdate, color2rgb, get_decimal_color, send_webhook


def test_printt():
    assert printt('test', speed=0, newLine=False) == ''


def test_cl():
    assert cl() is None


def test_bigtext():
    assert isinstance(bigtext('test'), str)


def test_percent():
    assert percent(50, 100) == 50.0


def test_pbar():
    bar = pbar(100)
    assert bar.total == 100


def test_pbarupdate():
    bar = pbar(100)
    pbarupdate(bar)
    assert bar.n == 1


def test_color2rgb():
    assert color2rgb('red') == (255, 0, 0)


def test_get_decimal_color():
    assert get_decimal_color('red') == 16711680


def test_send_webhook():
    # Тест с невалидным URL должен вернуть False
    assert send_webhook('') is False


if __name__ == '__main__':
    printt('test complete')
