import time
from uitility.baseclass import Baseclass
from selenium.webdriver.common.by import By
import allure


class Defination_Management:
    def __init__(self, baseclass) -> None:
        self.baseclass: Baseclass = baseclass
        self.action = self.baseclass.action_chain()

    __filter_textbox = (
        By.XPATH,
        "//div[@class='v-field__field']/input[@placeholder='Definitions...']",
    )
    __clear_defination = (By.CSS_SELECTOR, "i[aria-label='Clear Filter']")
    __definations = (
        By.XPATH,
        "//div[@role='listbox']//div[@class='v-list-item__content']",
    )
    __defination_title = (By.CSS_SELECTOR, "span.text-h5")
    __add_tag_textbox = (By.CSS_SELECTOR, "div.v-field__input>input")

    @allure.step("Click on {defination_name} ")
    def click_on_defiantion(self, defination_name):

        for i in self.baseclass.wait_until_elements(self.__definations):
            if i.text == defination_name:
                i.click()
                break
        else:
            self.baseclass.wait_until_elements(self.__definations)[0].click()
        return self.baseclass.get_text(self.__defination_title).replace(
            "Formal Usage of ", ""
        )

    @allure.step("Search Deination - {defination_name}")
    def search_defination(self, defination_name):
        time.sleep(1.0)
        for i in self.baseclass.wait_until_elements(self.__definations):
            if defination_name in i.text:
                pass
        else:
            defination_name = self.baseclass.wait_until_elements(self.__definations)[
                -1
            ].text
            with allure.step(f"Selected defination {defination_name}"):
                pass
        self.action.click(self.baseclass.wait_until(self.__filter_textbox)).send_keys(
            defination_name
        ).perform()
        return defination_name

    @allure.step("Check defination present")
    def check_defination_present(self, defination_name):

        texts = [i.text for i in self.baseclass.wait_until_elements(self.__definations)]
        if defination_name in texts:
            return True
        else:
            return False

    @allure.step("Get first defination")
    def get_first_defination(self):
        text = self.baseclass.wait_until_elements(self.__definations)[0].text
        with allure.step(text):
            return text

    @allure.step("Click on Clear defination")
    def click_clear_defination(self):
        self.baseclass.click(self.__clear_defination)
