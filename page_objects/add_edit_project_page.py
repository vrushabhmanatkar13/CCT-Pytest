import time
from test_cases import conftest as cf
from uitility.baseclass import Baseclass
from selenium.webdriver.common.by import By
import allure

SELECT_BASE_BOOK = cf.json_obj["Add Project"]["select_base_book"]
ADD_PROJECT = cf.json_obj["Add Project"]["add_project"]


class Add_Edit_Project_Page:
    def __init__(self, baseclass) -> None:
        self.baseclass: Baseclass = baseclass
        self.action = self.baseclass.action_chain()

    __buttons = (By.XPATH, "//span[@class='v-btn__content']")
    __buttons_loading = (By.CSS_SELECTOR, "button.v-btn--loading")
    # locator of edit project page
    __page_title = (By.XPATH, "//div[@class='v-toolbar-title__placeholder']")
    __close_icon = (By.CSS_SELECTOR, "i.mdi-close")
    __selected_base_book = (
        By.XPATH,
        "//div[@class='v-card-text px-0 pt-0 opacity-6']/span",
    )

    __short_code = (By.XPATH, "//input[@placeholder='Project short code']")
    __project_name_textbox = (By.XPATH, "//input[@placeholder='Project Name']")
    __project_title_textbox = (By.XPATH, "//input[@placeholder='Title']")
    __project_type = (By.XPATH, "//input[@placeholder='Select a project type']")
    __version_type = (By.XPATH, "//input[@placeholder='Select a version type']")
    __category = (By.XPATH, "//input[@placeholder='Select a category']")

    __all_textboxs = "//input[@placeholder='{text}']"
    __error_messages = (By.XPATH, "//div[@class='v-messages__message']")
    # locators of Select base book alert
    __group_comboboxs = "//label[text()='{text}']/following-sibling::div"
    __group_options = (By.XPATH, "//div[@role='listbox']/div")

    @allure.step("Get page header")
    def get_page_title(self):
        text = self.baseclass.get_text(self.__page_title)
        with allure.step(text):
            return text

    @allure.step("Click on {button_text}")
    def click_on_button(self, button_text):
        for i in self.baseclass.findelements(self.__buttons):
            if i.text == button_text:
                i.click()
                break
        else:
            raise Exception(f"{button_text} is not present on page")

    def wait_buttons_to_load(self):
        self.baseclass.wait_until_invisibility(self.__buttons_loading)

    @allure.step("Click close")
    def click_close_icon(self):
        self.baseclass.click(self.__close_icon)

    @allure.step("Get add project button enabled")
    def is_add_project_enalbed(self):
        result = None
        for i in self.baseclass.findelements(self.__buttons):
            if i.text == ADD_PROJECT:
                result = i.is_enabled()
                break
        return result

    # @allure.step("Get basebook text")
    def get_basebook_button_text(self):
        time.sleep(2)
        text = ""
        for i in self.baseclass.wait_until_elements(self.__buttons):
            if i.text == SELECT_BASE_BOOK:
                text = i.text
        return text

    def select_options(self, text):
        elements = self.baseclass.wait_until_elements(self.__group_options)

        for i in elements:
            if i.text == text:
                self.action.click(i).perform()
                break
        else:
            self.action.move_to_element(elements[-1]).perform()
            for i in self.baseclass.wait_until_elements(self.__group_options):
                if i.text == text:
                    self.action.click(i).perform()
                    break

    @allure.step("Select option - {text} of {option}")
    def click_select_option(self, text, option):

        self.baseclass.click((By.XPATH, self.__group_comboboxs.format(text=text)))
        self.select_options(option)
        return self.baseclass.get_text_javascript_executor(
            (By.XPATH, self.__group_comboboxs.format(text=text))
        )

    @allure.step("Get selected base book")
    def get_selected_basebook(self, replace_text):
        text = (
            self.baseclass.get_text(self.__selected_base_book)
            .replace(replace_text, "")
            .strip()
        )
        with allure.step(text):
            return text

    @allure.step("Fill Add project form")
    def fill_add_project_form(
        self, short_code, project_name, title, project_type, version_type, category
    ):
        self.action.click(self.baseclass.wait_until(self.__short_code)).send_keys(
            short_code
        ).perform()
        self.action.click(
            self.baseclass.wait_until(self.__project_name_textbox)
        ).send_keys(project_name).perform()
        self.action.click(
            self.baseclass.wait_until(self.__project_title_textbox)
        ).send_keys(title).perform()
        self.action.click(self.baseclass.wait_until(self.__project_type)).perform()
        self.select_options(project_type)
        self.action.click(self.baseclass.wait_until(self.__version_type)).perform()
        self.select_options(version_type)
        self.action.click(self.baseclass.wait_until(self.__category)).perform()
        self.select_options(category)

    @allure.step("Get filled text in textbox ")
    def get_filled_text(self, text) -> str:
        filled_text = self.baseclass.get_text_javascript_executor_textbox(
            (By.XPATH, self.__all_textboxs.format(text=text))
        ).strip()
        with allure.step(filled_text):
            return filled_text

    @allure.step("Get Selected option ")
    def get_selected_option(self, text):
        selected_text = self.baseclass.get_text_javascript_executor(
            (By.XPATH, self.__group_comboboxs.format(text=text))
        )
        with allure.step(selected_text):
            return selected_text

    @allure.step("Get Error Message")
    def get_error_message(self):
        text = [
            i.text for i in self.baseclass.wait_until_elements(self.__error_messages)
        ]
        with allure.step(str(text)):
            return text
