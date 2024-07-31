import time

import allure
from uitility.baseclass import Baseclass
from selenium.webdriver.common.by import By


class Dashboard_Page:
    def __init__(self, baseclass) -> None:
        self.baseclass: Baseclass = baseclass
        self.action = self.baseclass.action_chain()

    # locators of page title / header
    dashboard_title = (By.TAG_NAME, "h2")
    add_project_button = (By.XPATH, "//span[text()=' Add Project ']")

    # locators of Category field
    category_texbox = (By.CSS_SELECTOR, "div.v-autocomplete--single")
    category_options = (By.XPATH, "//div[@role='listbox']/div")
    clear_category = (By.XPATH, "//i[@aria-label='Clear Category']")
    selected_category = (By.CSS_SELECTOR, "span.v-autocomplete__selection-text")

    # locators of Title field
    title_textbox = (By.XPATH, "//div[@class='v-col-md-4 v-col-12']//input")
    clear_title = (By.XPATH, "//i[@aria-label='Clear Title']")

    # locators of tabs
    tabs = (By.CSS_SELECTOR, "div.v-sheet.v-theme--light")

    # locators of Table dashboard
    table_rows = (By.XPATH, "//tbody/tr")
    table_data = (By.XPATH, "//tbody/tr/td")
    # table_projct_name = (By.XPATH, "//tbody/tr/td[1]")
    # table_project_title = (By.XPATH, "//tbody/tr/td[2]")
    # table_project_category = (By.XPATH, "//tbody/tr/td[4]")
    # table_basebook = (By.XPATH, "//tbody/tr/td[3]")
    # table_project_type = (By.XPATH, "//tbody/tr/td[5]")
    # table_modified_date = (By.XPATH, "//tbody/tr/td[6]")

    __table_header = (By.XPATH, "//tr/th")
    __table_row_data = "//tbody/tr/td[{index}]"
    # locators of button below project row
    buttons = (
        By.XPATH,
        "//div[@id='dashboardButtons']/button//span[@class='v-btn__content']",
    )
    __version_count = (
        By.XPATH,
        "//div[@id='dashboardButtons']//span[@class='v-btn__append']",
    )

    # locators of Alert
    __alert_text = (By.CSS_SELECTOR, "div.v-card-title.text-h4.px-0")
    __alert_buttons = (By.CSS_SELECTOR, "div.v-card-actions>button")

    @allure.step("Get Dashboard text")
    def get_dashboard_page_text(self):
        return self.baseclass.get_text(self.dashboard_title)

    @allure.step("Click Add project")
    def click_add_project(self):
        self.baseclass.click(self.add_project_button)

    @allure.step("Click tab - {tab_name}")
    def click_tabs(self, tab_name):
        for tab in self.baseclass.wait_until_elements(self.tabs):
            if tab.text == tab_name:
                tab.click()
                break

    @allure.step("Select Category -{category_name}")
    def select_category(self, category_name):
        self.baseclass.wait_until_elements(self.table_rows)[0]
        self.baseclass.click(self.category_texbox)
        try:

            elements = self.baseclass.findelements(self.category_options)
        except:
            self.baseclass.driver.refresh()
            self.baseclass.wait_until_elements(self.table_rows)[0]
            self.baseclass.click(self.category_texbox)
            elements = self.baseclass.wait_until_elements(self.category_options)
        finally:
            self.action.move_to_element(elements[-1]).perform()
            for i in self.baseclass.wait_until_elements(self.category_options):
                if i.text == category_name:
                    i.click()
                    break
        return self.baseclass.wait_until_elements(self.table_rows)[0].is_displayed()

    @allure.step("Get Selected Category")
    def get_selected_category(self):
        time.sleep(2)
        text = self.baseclass.get_text_javascript_executor(self.selected_category)
        with allure.step(text):
            return text

    @allure.step("Get Selected Category is displayted")
    def get_selecated_category_displayed(self):
        # try:
        # self.baseclass.driver.find_element(
        #     self.selected_category[0], self.selected_category[1]
        # ).is_displayed()
        return self.baseclass.wait_until_invisibility(self.selected_category)

    # except Exception:
    #     return False

    @allure.step("Click Clear category")
    def click_clear_category(self):
        self.baseclass.click(self.clear_category)

    @allure.step("Get Project count")
    def get_project_count(self):
        count = len(self.baseclass.wait_until_elements(self.table_rows))
        with allure.step(count):
            return count

    @allure.step("Enter text in title textbox -{text}")
    def enter_text_title_textbox(self, text):
        self.baseclass.wait_until(self.table_rows)
        self.action.click_and_hold(
            self.baseclass.wait_until(self.title_textbox)
        ).send_keys(text).perform()

    @allure.step("Click clear title")
    def click_clear_title(self):
        self.baseclass.click(self.clear_title)

    @allure.step("Get data present in table ")
    def get_row_data_text(self, text):
        result = False
        for i in self.baseclass.wait_until_elements(self.table_data):
            if text in i.text:
                result = True
                break
        return result

    @allure.step("Get table row is invisibal")
    def project_row_is_displayed(self):
        return self.baseclass.wait_until_invisibility(self.table_rows)

    def get_row_data(self, text):
        header = self.baseclass.wait_until_elements(self.__table_header)
        index = None
        for i in header:
            if i.text == text:
                index = str(header.index(i) + 1)
                break
        return self.baseclass.wait_until_elements(
            (
                By.XPATH,
                self.__table_row_data.format(index=index),
            )
        )

    @allure.step("Get firt project name")
    def get_first_project_name(self):
        project_name = self.get_row_data("Project Name")[0].text
        with allure.step(project_name):
            return project_name

    @allure.step("Get last project name")
    def get_last_projcet_name(self):
        project_name = self.get_row_data("Project Name")[-1].text
        with allure.step(project_name):
            return project_name

    @allure.step("Get first category")
    def get_first_category(self):
        text = self.get_row_data("Category")[0].text
        with allure.step(text):
            return text.strip()

    @allure.step("Get first title name")
    def get_first_title_name(self):
        text = self.get_row_data("Title")[0].text
        with allure.step(text):
            return text

    @allure.step("Get first base book")
    def get_first_basebook_name(self):
        text = self.get_row_data("Base Book")[0].text
        with allure.step(text):
            return text

    @allure.step("Get first projcet type")
    def get_first_project_type(self):
        text = self.get_row_data("Project Type")[0].text
        with allure.step(text):
            return text

    @allure.step("Get first modified date")
    def get_first_project_modified_date(self):
        text = self.get_row_data("Last Modified")[0].text
        with allure.step(text):
            return text

    @allure.step("Click project row - {serial_no}")
    def click_project_row(self, serial_no: int):
        if serial_no == 1:
            serial_no = 0
        else:
            serial_no = serial_no - 1
        element = self.baseclass.wait_until_elements(self.table_rows)[serial_no]
        self.baseclass.click_javascript_executor_element(element)

    @allure.step("Click on project -{project_name}")
    def click_project_name(self, project_name):
        for i in self.get_row_data("Project Name"):
            if i.text == project_name:
                i.click()
                break
        else:
            raise Exception(f"{project_name} is not showing on Dashboard")

    @allure.step("Get Dashboard buttons text")
    def get_dashboard_button_text(self):
        text = [i.text for i in self.baseclass.wait_until_elements(self.buttons)]
        with allure.step(str(text)):
            return text

    @allure.step("Click on {text}")
    def click_dashboard_button(self, text):
        for i in self.baseclass.wait_until_elements(self.buttons):
            if i.text == text:
                i.click()
                break
        self.baseclass.wait_loadder_dissappried()

    @allure.step("Get Chapter version")
    def get_chapter_version_count(self):
        time.sleep(1.0)
        text = self.baseclass.get_text_javascript_executor(self.__version_count)
        with allure.step(text):
            return text

    @allure.step("Get {text} button is clickable")
    def get_button_clickable(self, text):
        result = None
        for i in self.baseclass.wait_until_elements(self.buttons):
            if i.text == text:
                result = self.baseclass.get_element_clickable(i)
                break
        return result

    @allure.step("Get alert heading")
    def get_alert_text(self) -> str:
        text = self.baseclass.get_text_javascript_executor(self.__alert_text)
        with allure.step(text):
            return text.strip()

    def wait_alert_dissappired(self):
        try:
            return self.baseclass.wait_until_invisibility(self.__alert_text)
        except:
            return False

    @allure.step("Click on {button_text}")
    def click_on_alert_button(self, button_text):
        for i in self.baseclass.wait_until_elements(self.__alert_buttons):
            if button_text in i.text:
                i.click()
                break

    @allure.step("Select Project is display on dashboard")
    def check_project_display(self, project_name):
        """To check project present on dashboard
        If not the retun first project name.
        """
        text = ""
        for i in self.get_row_data("Project Name"):
            if i.text == project_name:
                text = i.text
                break
        else:
            text = self.get_first_project_name()

        with allure.step(f"Selected Project {text}"):
            return text
