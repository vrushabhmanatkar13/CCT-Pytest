from page_objects.dashboard_page import Dashboard_Page
from uitility.baseclass import Baseclass
from selenium.webdriver.common.by import By
import allure


class View_Project_Page:
    def __init__(self, baseclass) -> None:
        self.baseclass: Baseclass = baseclass
        self.action = self.baseclass.action_chain()

    # Commaon - Sucess Alert
    __sucess_alert = (By.CSS_SELECTOR, "div.vue3-snackbar-message-title")

    # locator of Heading project Name
    __project_name = (By.XPATH, "//div[@class='v-col-md-6 v-col-12']/h2")
    __active_breadcum = (By.CSS_SELECTOR, "a.v-breadcrumbs-item--link")
    __deactive_breadcum = (By.CSS_SELECTOR, "span.breadcrumbsMargin")
    __book_management_breadcum = (By.CSS_SELECTOR, "span.v-breadcrumbs-item--disabled")
    # Book Management buttons
    __book_management_buttons = (
        By.CSS_SELECTOR,
        "div.flex-column > button >span.v-btn__content",
    )
    __chapter_version = (
        By.XPATH,
        "//div[contains(@class,'flex-column')]//span[@class='v-btn__append']",
    )
    # Smart Index
    __sort_order_button = (
        By.XPATH,
        "//div[@aria-haspopup='dialog']//span[@class='v-btn__content']",
    )
    __chapter = (By.CSS_SELECTOR, "div.v-list-item-title.text-left.pr-1")
    __chapter_status = (By.CSS_SELECTOR, "div.v-list-item__append>small")
    __fm_chapter = (By.CSS_SELECTOR, "a.isFrontmatter>div.v-list-item__content")
    # Sort Order Alert
    __sort_order_text = (By.XPATH, "//div[text()='Sort Order']")
    __draggable_option = (By.CSS_SELECTOR, "li.list-group-item")
    __alert_buttons = (By.CSS_SELECTOR, "div.v-card-actions>button>span.v-btn__content")

    @allure.step("Get alert message")
    def get_alert_message(self):
        text = self.baseclass.get_text(self.__sucess_alert)
        self.baseclass.wait_loadder_dissappried()
        with allure.step(text):
            return text

    @allure.step("Get Project heading")
    def get_project_heading_name(self):
        text = self.baseclass.get_text(self.__project_name)
        with allure.step(text):
            return text

    @allure.step("Get Previos breadcum text")
    def get_previos_breadcum(self, number=1):
        if number == 1:
            text = self.baseclass.wait_until_elements(self.__active_breadcum)[0].text
            with allure.step(text):
                return text
        else:
            text = self.baseclass.wait_until_elements(self.__active_breadcum)[
                number - 1
            ].text
            with allure.step(text):
                return text

    @allure.step("Click on breadcum")
    def click_pervios_breadcum(self, text=None):
        if text == None:
            self.baseclass.click(self.__active_breadcum)
        else:
            for i in self.baseclass.wait_until_elements(self.__active_breadcum):
                if i.text == text:
                    i.click()
                    break
        self.baseclass.wait_loadder_dissappried()

    @allure.step("Get current breadcum")
    def get_current_breadcum(self):
        text = self.baseclass.get_text(self.__deactive_breadcum).strip()
        with allure.step(text):
            return text

    @allure.step("Get opened breadcum text")
    def get_book_managament_breadcum(self):
        text = self.baseclass.get_text(self.__book_management_breadcum).strip()
        with allure.step(text):
            return text

    @allure.step("Click on Book Management button - {button_name}")
    def click_on_book_management_button(self, button_name):
        for i in self.baseclass.wait_until_elements(self.__book_management_buttons):
            if i.text == button_name:
                self.baseclass.click_javascript_executor_element(i)
                break

    @allure.step("Get chapter version count")
    def get_chapter_version_count(self):
        text = self.baseclass.get_text(self.__chapter_version)
        with allure.step(text):
            return text

    @allure.step("Get {button_name} is clickable")
    def get_book_management_button_clickable(self, button_name):
        result = None
        for i in self.baseclass.wait_until_elements(self.__book_management_buttons):
            if i.text == button_name:
                result = self.baseclass.get_element_clickable(i)
                break
        return result

    @allure.step("Click sort order button")
    def click_sort_order_button(self):
        self.baseclass.click(self.__sort_order_button)

    @allure.step("Click on - {chapter_name}")
    def click_on_chapter(self, chapter_name):
        chapters = self.baseclass.wait_until_elements(self.__chapter)
        for i in chapters:
            self.action.scroll_to_element(i).perform()
            if chapter_name in i.text:
                self.baseclass.click_javascript_executor_element(i)
                break
        else:
            raise Exception(f"{chapter_name} is not persent on screen")
        self.baseclass.wait_loadder_dissappried()

    def get_last_cahpter_number(self):
        chapters = []
        for i in self.baseclass.wait_until_elements(self.__chapter):
            self.action.scroll_to_element(i).perform()
            text = self.baseclass.get_text_javascript_executor_element(i)
            if "CHAPTER" in text:
                chapters.append(i)
        return len(chapters)

    def get_cahpter_number(self, chapter_name):
        chapters = []
        number = None
        for i in self.baseclass.wait_until_elements(self.__chapter):
            if "CHAPTER" in i.text:
                chapters.append(i.text)
        for j in chapters:
            if chapter_name in j:
                number = str(chapters.index(j) + 1)
        return number

    @allure.step("Get Chapter status from smart index")
    def get_chapter_status(self, chapter_name):
        self.baseclass.wait_loadder_dissappried()
        chapters = self.baseclass.wait_until_elements(self.__chapter)
        status = ""
        for i in chapters:
            if chapter_name in i.text:
                status = self.baseclass.wait_until_elements(self.__chapter_status)[
                    chapters.index(i)
                ].text
                break
        with allure.step(status):
            return status

    @allure.step("Check chapter deleted")
    def check_chapter_deleted(self, chapter_name):
        for i in self.baseclass.wait_until_elements(self.__chapter):
            if chapter_name in i.text:
                return False
        else:
            return True

    @allure.step("Get all Fm chapter name")
    def get_all_fm_chapter_name(self):
        text = [i.text for i in self.baseclass.wait_until_elements(self.__fm_chapter)]
        with allure.step(str(text)):
            return text

    @allure.step("Get all Fm chapter name on Sort order popup")
    def get_fm_chapter_name_on_sortorder(self):
        self.baseclass.get_text(self.__sort_order_text)

        text = [
            i.text for i in self.baseclass.wait_until_elements(self.__draggable_option)
        ]
        with allure.step(str(text)):
            return text

    @allure.step("Drag {drag_text} drop to {drop_text}")
    def drag_drop_fm_chapter(self, drag_text, drop_text):
        source = None
        dest = None
        for i in self.baseclass.wait_until_elements(self.__draggable_option):
            if i.text == drag_text:
                source = i
            elif i.text == drop_text:
                dest = i
        self.action.drag_and_drop(source, dest).perform()

    @allure.step("Click on - {text}")
    def click_button_on_sort_order(self, text):
        for i in self.baseclass.wait_until_elements(self.__alert_buttons):
            if i.text == text:
                i.click()
                break
