from selenium.webdriver.common.by import By
import allure

from uitility.baseclass import Baseclass


class Header_Footer:

    def __init__(self, baseclass) -> None:
        self.baseclass: Baseclass = baseclass

    # footer
    __add_new_button = (By.CSS_SELECTOR, "div#footer>button")
    __footer_content_model_list = (
        By.CSS_SELECTOR,
        "div.chapter-footer-modal >div.v-list-item__content",
    )

    # Add new Code element
    __code_element_buttons = (By.XPATH, "//div[@class='v-overlay__content']//button")

    @allure.step("Click on Add New button")
    def click_on_add_new(self):
        self.baseclass.wait_loadder_dissappried()
        self.baseclass.click_javascript_executor(self.__add_new_button)

    @allure.step("Click om {text}")
    def click_on_model_list(self, text):
        for i in self.baseclass.wait_until_elements(self.__footer_content_model_list):
            if i.text == text:
                self.baseclass.click_javascript_executor_element(i)
                break
        self.baseclass.wait_loadder_dissappried()

    @allure.step("Click on {button_text}")
    def click_on_code_element_button(self, button_text):
        for i in self.baseclass.wait_until_elements(self.__code_element_buttons):
            if button_text in i.text:
                i.click()
                break
        self.baseclass.wait_loadder_dissappried()
