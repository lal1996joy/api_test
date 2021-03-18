from testcase_UI.login_page import LoginPage


class Login(LoginPage):

    def test_login(self):
        self.get_name_element().value('admin')
        self.get_pwd_element().value('1q2w3eadmin')
        self.get_loginbutton_element().click()



if __name__ == '__main__':
    Login().test_login()
