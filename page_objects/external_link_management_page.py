from uitility.baseclass import Baseclass
from selenium.webdriver.common.by import By
import allure


class External_Link_Management:

    def __init__(self, baseclass) -> None:
        self.baseclass: Baseclass = baseclass

    __page_title = (By.CSS_SELECTOR, "div.v-card-title")

    @allure.step("Get Page heading")
    def get_page_heading(self):
        text = self.baseclass.get_text(self.__page_title)
        with allure.step(text):
            return text
