import json
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import allure
from selenium.webdriver.common.by import By
import pytest_check as check


class Baseclass:
    def __init__(self, driver, wait) -> None:
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, wait, poll_frequency=0.1)

    # loadder Web element
    loader = (By.CSS_SELECTOR, "div.v-layout>div.v-progress-circular")

    def action_chain(self):
        action: ActionChains = ActionChains(self.driver)
        return action

    def findelement(self, locator):
        try:
            return self.driver.find_element(locator[0], locator[1])
        except Exception as e:
            print(f"{locator} is not prsent {e}")

    def findelements(self, locator):
        elements = self.driver.find_elements(locator[0], locator[1])
        if not elements:
            raise Exception
        else:
            return elements

    @allure.step("Get page title {title}")
    def wait_until_get_title(self, title):
        try:
            self.wait.until(EC.title_is(title))
        except Exception as e:
            print(f"Title: {title} : {str(e)}")

    def wait_until_url_change(self, url):
        self.wait.until(EC.url_changes(url))

    def wait_until(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception as e:
            print(f"Element: {locator} : {str(e)}")

    def wait_until_elements(self, locator):
        # try:
        return self.wait.until(EC.presence_of_all_elements_located(locator))
        # except Exception as e:
        #     # print(f"Element: {locator} : {str(e)}")
        #       return Exception()

    def click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception as e:
            print(f"Element: {locator} : {str(e)}")

    def send_keys(self, locator, text):
        try:
            element: WebElement = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"Element: {locator} : is not found")

    def get_text(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).text

        except Exception as e:
            print(f"Element: {locator} : {e.with_traceback}")

    def click_javascript_executor(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def click_javascript_executor_element(self, webelement):
        element = self.wait.until(EC.visibility_of(webelement))
        self.driver.execute_script("arguments[0].click();", element)

    def get_text_javascript_executor(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.execute_script("return arguments[0].textContent;", element)

    def get_text_javascript_executor_element(self, webelement):
        element = self.wait.until(EC.visibility_of(webelement))
        return self.driver.execute_script("return arguments[0].textContent;", element)

    def get_text_javascript_executor_textbox(self, locator) -> str:
        element = self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.execute_script("return arguments[0].value;", element)

    def send_keys_javascript_executor(self, element, text_to_send):
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", element, text_to_send
        )

    def wait_until_invisibility(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f"{locator} still visibal on screen",
        )

    def get_current_window_handel(self):
        return self.driver.current_window_handle

    def switch_to_window(self, parent_window):
        for i in self.driver.window_handles:
            if i != parent_window:
                self.driver.switch_to.window(i)

    def switch_to_parentwindow(self, handle):
        self.driver.switch_to.window(handle)

    def scroll_at_end(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element)

    def get_element_clickable(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        if element is False:
            return element

    def is_alert_present(self):
        try:
            WebDriverWait(self.driver, 1.0, 0.1).until(EC.alert_is_present())
            return True
        except Exception:
            return False

    # insted of hard assert we user "pytest_check" plugin for soft assert

    @staticmethod
    def assert_equals(expecated, actual):
        check.equal(
            expecated, actual, msg=f"Expecated: {expecated}, equal to Founded: {actual}"
        )
        # assert expecated == actual, print(
        #     f"Expecated: {expecated}, equal to Founded: {actual}"
        # )

    @staticmethod
    def assert_not_equals(expecated, actual):
        check.not_equal(
            expecated,
            actual,
            msg=f"Expecated: {expecated}, not equal to Founded: {actual}",
        )
        # assert expecated != actual, print(
        #     f"Expecated: {expecated}, not equal to Founded: {actual}"
        # )

    @staticmethod
    def assert_true(actual):
        check.is_true(actual, msg=f"Expecated: {actual}, but Founded: {False}")
        # assert actual, print(f"Expecated: {actual}, but Founded: {False}")

    @staticmethod
    def assert_false(actual):
        check.is_false(actual, msg=f"Expecated: {actual}, but Founded: {True}")
        # assert not actual, print(f"Expecated: {actual}, but Founded: {True}")

    # this method for wait untill loadder is display
    def wait_loadder_dissappried(self):
        try:
            self.wait_until_invisibility(self.loader)
        except:
            raise Exception("Loadder still showing on screen")
