import smtplib
import pytest


@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.qq.com", 587, timeout=5)
