from uitility.baseclass import Baseclass
from selenium.webdriver.common.by import By
import allure


class Appendix_Overview_Page:
    def __init__(self, baseclass) -> None:
        self.baseclass: Baseclass = baseclass
        self.action = self.baseclass.action_chain()

    __appendix_content_text = (By.XPATH, "//section[@class='appendix']")
    __chapter = (By.CSS_SELECTOR, "div.v-list-item-title.text-left.pr-1")

    @allure.step("Get Appendix Content text")
    def get_appendix_content_text(self):
        """To get Appendix content text"""
        return self.baseclass.get_text(self.__appendix_content_text)

    def get_last_appendix_ordinal(self):
        ordinal = ""
        for i in self.baseclass.wait_until_elements(self.__chapter):
            self.action.scroll_to_element(i).perform()
            text = self.baseclass.get_text_javascript_executor_element(i)
            if "APPENDIX" in text:
                ordinal = i.find_element(By.CSS_SELECTOR, "span>span:nth-child(2)").text
        return chr(ord(ordinal) + 1)

    def get_current_appendix_ordinal(self):
        ordinal = ""
        for i in self.baseclass.wait_until_elements(self.__chapter):
            text = self.baseclass.get_text_javascript_executor_element(i)
            if "APPENDIX" in text:
                ordinal = i.find_element(By.CSS_SELECTOR, "span>span:nth-child(2)").text
        return ordinal
