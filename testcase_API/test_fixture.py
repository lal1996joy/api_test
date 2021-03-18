import pytest




def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert 0


if __name__ == '__main__':
    pytest.main(['test_fixture.py'])