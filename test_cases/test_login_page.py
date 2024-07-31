# from test_base import Test_Base
import pytest
from test_cases import conftest
from test_cases.test_base import Test_Base
from uitility.baseclass import Baseclass
import allure

HOME_PAGE = conftest.json_obj["Page Titles"]["home_page"]
RESET_PASSWORD_PAGE = conftest.json_obj["Page Titles"]["rest_password"]


@pytest.mark.Login
@pytest.mark.order(index=0)
@allure.feature("Login")
@allure.tag("Login Page")
class Test_Login_Page(Test_Base):

    @allure.title("Verify Login with Invalid email and password")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(
        ["email", "password"],
        [
            ("inavlid.user@iccsafe.org", "Password5"),
            ("ct-super-admin-test@iccsafe.org", "Pass123"),
        ],
    )
    def test_login_with_invalid_email_password(self, email, password):
        self.loginpage.login(email, password)
        text = self.loginpage.get_alert_text()
        Baseclass.assert_equals(
            text,
            "The email and password you entered did not match our records. Please double-check and try again.",
        )

    @allure.title("Verify Login with Empty email")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_with_empty_email(self):
        result = self.loginpage.login_empty_email("Password5")
        error = self.loginpage.get_message()

        Baseclass.assert_false(result)
        Baseclass.assert_equals(error, "Email is required")

    @allure.title("Verify Login with Empty password")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_with_empty_password(self):
        result = self.loginpage.login_empty_password("ct-super-admin-test@iccsafe.org")
        error = self.loginpage.get_message()
        Baseclass.assert_false(result)
        Baseclass.assert_equals(error, "Password is required")

    @allure.title("Verify Forgot password link")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_forgotpassword_link(self):
        current_window = self.baseclass.get_current_window_handel()
        self.loginpage.click_forgotpassword_link(current_window)
        Baseclass.assert_equals(RESET_PASSWORD_PAGE, self.driver.title)
        self.driver.close()
        self.baseclass.switch_to_parentwindow(current_window)

    @allure.title("Verify Login with valid email and password")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_with_valid_data(self):
        self.loginpage.login("ct-super-admin-test@iccsafe.org", "Password5")
        self.baseclass.wait_until_get_title(HOME_PAGE)
        Baseclass.assert_equals(self.driver.title, HOME_PAGE)
