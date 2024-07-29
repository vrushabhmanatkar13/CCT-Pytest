import time
from selenium.webdriver.common.by import By
from uitility.baseclass import Baseclass
import allure


class Login_Page:
    def __init__(self, baseclass) -> None:
        self.baseclass: Baseclass = baseclass
        self.action = self.baseclass.action_chain()

    logo = (By.TAG_NAME, "h1")
    email_textbox = (By.CSS_SELECTOR, "input[name='email']")
    password_textbox = (By.CSS_SELECTOR, "input[name='password']")
    login_button = (By.XPATH, "//button[@type='submit']")
    forgot_password = (By.XPATH, "//a[text()=' Forgot Your Password? ']")

    alert = (By.XPATH, "//div[@class='v-alert__content']")
    message = (By.XPATH, "//div[@class='v-messages']/div")

    @allure.step("Enter email- {email}, password- {password} and click on Login")
    def login(self, email, password):

        self.action.click(self.baseclass.wait_until(self.email_textbox)).send_keys(
            email
        ).perform()
        self.action.click(self.baseclass.wait_until(self.password_textbox)).send_keys(
            password
        ).perform()

        self.baseclass.click_javascript_executor(self.login_button)

    # @allure.step("click forgotpassword link")
    # def click_forgot_password(self):
    #     self.baseclass.click(self.forgot_password)

    @allure.step("Get Alert text")
    def get_alert_text(self):
        text = self.baseclass.wait_until(self.alert).text
        with allure.step(text):
            return text

    @allure.step("Enter password - {password}")
    def login_empty_email(self, password):
        self.action.click(self.baseclass.wait_until(self.email_textbox)).perform()
        self.action.click(self.baseclass.wait_until(self.password_textbox)).send_keys(
            password
        ).perform()
        return self.baseclass.wait_until(self.login_button).is_enabled()

    @allure.step("Enter email - {email}")
    def login_empty_password(self, email):
        self.action.click(self.baseclass.wait_until(self.email_textbox)).send_keys(
            email
        ).perform()
        self.action.click(self.baseclass.wait_until(self.password_textbox)).perform()
        time.sleep(1)
        self.baseclass.click(self.logo)
        return self.baseclass.wait_until(self.login_button).is_enabled()

    @allure.step("Get error message")
    def get_message(self):
        text = self.baseclass.get_text_javascript_executor(self.message)
        with allure.step(text):
            return text

    @allure.step("click forgotpassword link")
    def click_forgotpassword_link(self, window_handel):
        self.baseclass.click(self.forgot_password)
        self.baseclass.switch_to_window(window_handel)
