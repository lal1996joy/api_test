import pytest


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    print(msg)
    print(response)
    assert response == 250
    assert b"smtp.qq.com" in msg
    assert 0  # for debug


def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    assert 0  # for debug


if __name__ == '__main__':
    pytest.main(['-s', 'test_module.py'])
