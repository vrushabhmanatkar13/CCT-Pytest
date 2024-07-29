from multiprocessing import set_forkserver_preload
import os
from re import T
import time
from tkinter import E
from selenium.webdriver.common.keys import Keys

from uitility.baseclass import Baseclass
from selenium.webdriver.common.by import By
import allure


class Chapter_Overview_page:
    def __init__(self, baseclass) -> None:
        self.baseclass: Baseclass = baseclass
        self.action = self.baseclass.action_chain()

    # Header
    __chapter_status = (By.CSS_SELECTOR, "div.text-md-right>small.pTB-Status")

    __all_buttons = (
        By.CSS_SELECTOR,
        "div.flex-column.max-w-270.px-4>button>span.v-btn__content",
    )

    # Smart Index
    __chapter_status_toc = (By.CSS_SELECTOR, "div.v-list-item__append>small")
    __chapter_name_toc = (By.CSS_SELECTOR, "a>div>div.v-list-item-title")
    __section_name_toc = (
        By.XPATH,
        "//div[contains(@class,'itemHeight')]/div[@class='v-list-item__content']",
    )
    __sub_section_name_toc = (
        By.XPATH,
        "//div[@role='group']//div[@class='v-list-item__content']",
    )

    # indicator
    __section_green_indicator = (
        By.XPATH,
        "//div[contains(@class,'itemHeight')]//span/i",
    )
    __sub_section_green_indicator = (
        By.XPATH,
        "//div[@role='group']//span/i",
    )

    # Content Page
    __chapter_heading = (By.XPATH, "//h1[@class='chapter']/span")
    __chapter_content_text = (By.XPATH, "//section[@class='chapter']")

    # Active Content page
    __active_content = (By.XPATH, "//div[@class='sectionLink selected']")
    __active_section_heading = (
        By.XPATH,
        "//div[@class='sectionLink selected']//h1/span",
    )
    __active_section_text = (By.XPATH, "//div[@class='sectionLink selected']//p")

    # __active_defination = (By.XPATH, "//div[@class='sectionLink selected']//h1/span")

    __active_fig = (By.XPATH, "//div[@class='sectionLink selected']//figure/img")
    __active_fig_above_text = (
        By.XPATH,
        "//div[@class='sectionLink selected']//figcaption/div[1]",
    )
    __active_fig_below_text = (
        By.XPATH,
        "//div[@class='sectionLink selected']//figcaption/div[2]",
    )
    __active_fig_title_text = (
        By.XPATH,
        "//div[@class='sectionLink selected']//figcaption/p",
    )
    __deleated_figure = (
        By.XPATH,
        "//figure[@data-deleted='true' and @class='figure' ]",
    )

    # Frontmatter Cahapter
    __fm_chapter_content_text = (By.CSS_SELECTOR, "section >header")
    __fm_active_section_heading = (
        By.XPATH,
        "//div[@class='sectionLink selected']//h2/span",
    )
    __fm_active_section_text = (
        By.XPATH,
        "//div[@class='sectionLink selected']//section",
    )
    __fm_deleted_section = (By.XPATH, "//section[@data-deleted='true']")

    # Edit content
    __edit_heading = (By.XPATH, "//div[contains(@class,'v-col v-col-')]/h2")
    __textboxs = (
        "//p[contains(text(),'{text}')]/parent::div//div[@contenteditable='true']"
    )
    __title_textbox = (
        By.XPATH,
        "//p[text()=' Title: ']/parent::div//div[@contenteditable='true']",
    )
    __checkbox_label_no_title = (
        By.XPATH,
        "//label[@class='v-label v-label--clickable']",
    )

    __get_text_textboxs = "//p[contains(text(),'{text}')]/parent::div/div"
    __edit_page_buttons = (
        By.XPATH,
        "//div[@class='v-col v-col-12 py-0']//span[@class='v-btn__content']",
    )
    __label_options = (
        By.XPATH,
        "//div[@class='v-overlay-container']//div[@class='v-list-item__content']",
    )
    __fig_upload = (
        By.XPATH,
        "//input[@type='file']",
    )
    __uploaded_fig = (By.XPATH, "//img[@class='v-img__img v-img__img--cover']")
    __fig_name = (By.XPATH, "//div[@class='v-chip__content']")

    # conformation Alert (Are you sure?)
    __alert_buttons = (By.XPATH, "//div[@class='swal2-actions']/button")

    # Relocate Alert
    __relocate_alert_buttons = (By.XPATH, "//div[@class='v-overlay__content']//button")
    __current_ordinal = (
        By.XPATH,
        "(//div[@class='v-overlay__content']//div[@class='v-card-text well'])[1]",
    )
    __new_ordinal = (By.XPATH, "(//div[@class='v-overlay__content']//input)[1]")

    __alert_text = (By.CSS_SELECTOR, "div.v-card-actions.px-0>div>div.v-alert__content")

    # Delete Alert
    __checkbox = (By.XPATH, "//label[@class='v-label v-label--clickable']")

    @allure.step("Click on {button_text}")
    def click_on_alert_button(self, button_text):
        for i in self.baseclass.wait_until_elements(self.__alert_buttons):
            if button_text in i.text:
                i.click()
                break

        self.baseclass.wait_loadder_dissappried()

    @allure.step("Edit content of {textbox_name}")
    def edit_contant(self, textbox_name, content_text):
        self.baseclass.wait_loadder_dissappried()
        textbox = (By.XPATH, self.__textboxs.format(text=textbox_name))
        if content_text in self.baseclass.get_text_javascript_executor(textbox):
            text = self.baseclass.get_text(textbox).replace(content_text, "").strip()
            final_text = text.rsplit(" ", 1)[0].strip()
            # pyperclip.copy(final_text)
            self.baseclass.click(textbox)
            self.baseclass.send_keys(textbox, final_text)
            # self.baseclass.send_keys(textbox, pyperclip.paste())
        time.sleep(2)
        self.baseclass.click(textbox)
        self.action.send_keys(Keys.PAGE_DOWN).send_keys(" " + content_text).perform()

    @allure.step("Enter text in {textbox_name}")
    def enter_text_in_textbox(self, textbox_name, text):
        self.baseclass.wait_loadder_dissappried()
        textbox = (By.XPATH, self.__textboxs.format(text=textbox_name))
        self.action.click(self.baseclass.wait_until(textbox)).send_keys(text).perform()

    @allure.step("Enter Text in Title")
    def enter_text_in_title_textbox(self, text):
        self.baseclass.wait_loadder_dissappried()
        self.baseclass.wait_until(self.__title_textbox).clear()
        self.action.click(self.baseclass.wait_until(self.__title_textbox)).send_keys(
            text
        ).perform()

    @allure.step("Click no title checkbox")
    def click_fm_no_title_checkbox(self):
        self.baseclass.click(self.__checkbox_label_no_title)

    @allure.step("Get Title text field")
    def get_fm_title_field(self):
        result = self.baseclass.wait_until_invisibility(self.__title_textbox)
        with allure.step(result):
            return result

    @allure.step("Get filled text in {textbox_name}")
    def get_filled_text(self, textbox_name):
        textbox = (By.XPATH, self.__get_text_textboxs.format(text=textbox_name))
        text = self.baseclass.get_text_javascript_executor(textbox)
        with allure.step(text):
            return text

    @allure.step("Select Section label- {label_text}")
    def select_section_label(self, label_text):
        element = (By.XPATH, self.__get_text_textboxs.format(text="Section Label"))
        self.baseclass.click(element)
        time.sleep(1)
        options = self.baseclass.wait_until_elements(self.__label_options)
        self.action.move_to_element(options[0]).perform()
        for i in options:
            if i.text == label_text:
                self.action.move_to_element(i).click().perform()
                break
        else:
            raise Exception(f"{label_text} is not present in Section Label")

    @allure.step("Click on {button_text}")
    def click_edit_page_button(self, button_text):
        for i in self.baseclass.wait_until_elements(self.__edit_page_buttons):
            if button_text in i.text:
                self.baseclass.click_javascript_executor_element(i)
                break
        else:
            raise Exception(f"{button_text} is not showing on screen")

    @allure.step("Get Edit heading Text")
    def get_edit_heading_text(self):
        text = self.baseclass.get_text(self.__edit_heading).replace("Edit ", "")
        with allure.step(text):
            return text

    @allure.step("Get Chapter status from toolbar")
    def get_chapter_status(self):
        text = self.baseclass.get_text(self.__chapter_status)
        with allure.step(text):
            return text

    @allure.step("Click on - {text}")
    def click_on_button(self, text):
        for i in self.baseclass.wait_until_elements(self.__all_buttons):
            if i.text == text:
                self.baseclass.click_javascript_executor_element(i)
                break
        else:
            raise Exception(f"Button: {text} Not found")
        self.baseclass.wait_loadder_dissappried()

    @allure.step("Get chapter status from TOC")
    def get_chapter_status_toc(self):
        text = self.baseclass.get_text(self.__chapter_status_toc)
        with allure.step(text):
            return text

    @allure.step("Get Chapter Name from TOC")
    def get_chapter_name_toc(self):
        text = self.baseclass.get_text(self.__chapter_name_toc)
        with allure.step(text):
            return text

    @allure.step("Click on {section_name} from TOC")
    def click_on_section_on_toc(self, section_name):
        self.baseclass.wait_loadder_dissappried()
        for i in self.baseclass.wait_until_elements(self.__section_name_toc):
            if section_name in i.text:
                self.baseclass.click(i)
                break
        else:
            raise Exception(f"{section_name} is not present on toc")

    def get_section_number(self, section_name):
        sections = self.baseclass.wait_until_elements(self.__section_name_toc)
        number = None
        for i in sections:
            if section_name in i.text:
                number = i.find_element(By.XPATH, "//div/span/span[2]").text
                break
        return number

    @allure.step("Click on sub {sub_section_name} from TOC")
    def click_on_sub_section_on_toc(self, sub_section_name):
        for i in self.baseclass.wait_until_elements(self.__sub_section_name_toc):
            if sub_section_name in i.text:
                self.baseclass.click_javascript_executor_element(i)
                break
        else:
            raise Exception(f"{sub_section_name} is not present on toc")

    def get_sub_section_number(self, sub_section_name):
        number = None
        sections = self.baseclass.wait_until_elements(self.__sub_section_name_toc)
        for i in sections:

            if sub_section_name in self.baseclass.get_text_javascript_executor_element(
                i
            ):
                number = i.text.split()[0]
                break
        return number

    @allure.step("Get Active Content heading")
    def get_active_heading_name(self):
        text = " ".join(
            i.text
            for i in self.baseclass.wait_until_elements(self.__active_section_heading)
        )
        with allure.step(text):
            return text

    @allure.step("Get Active Fm Content heading")
    def get_active_fm_heading_name(self):
        text = " ".join(
            i.text
            for i in self.baseclass.wait_until_elements(
                self.__fm_active_section_heading
            )
        )
        with allure.step(text):
            return text

    @allure.step("Check Sub Section Deleted")
    def check_subsection_deleted(self, subsection_name):
        try:
            result = None
            for i in self.baseclass.wait_until_elements(self.__sub_section_name_toc):
                if subsection_name in i.text:
                    result = False
                    break
            else:
                result = True
            return result
        except:
            return True

    @allure.step("Check Section Deleted")
    def check_section_deleted(self, section_name):
        try:
            result = None
            for i in self.baseclass.wait_until_elements(self.__section_name_toc):
                if section_name in i.text:
                    result = False
            else:
                result = True
            return result
        except:
            return True

    @allure.step("Get Chapter heading")
    def get_chapter_heading(self):
        """To get Chapter Name on content page"""
        text = " ".join(
            i.text for i in self.baseclass.wait_until_elements(self.__chapter_heading)
        )
        with allure.step(text):
            return text

    @allure.step("Click on Chapter")
    def click_on_chapter(self):
        """To Click on Chapter"""
        element = self.baseclass.wait_until_elements(self.__chapter_heading)
        self.baseclass.click(element[0])
        self.baseclass.wait_loadder_dissappried()

    @allure.step("Click on Active content")
    def click_on_active_content(self):
        """To Click on Active content"""
        self.baseclass.click(self.__active_content)
        self.baseclass.wait_loadder_dissappried()

    @allure.step("Get Chapter Content text")
    def get_chapter_content_text(self):
        """To get Chapter content text"""
        return self.baseclass.get_text(self.__chapter_content_text)

    @allure.step("Get Fm Chapter Content text")
    def get_fm_chapter_content_text(self):
        """To get Fm chapter content text"""
        return self.baseclass.get_text(self.__fm_chapter_content_text)

    @allure.step("Get Active Section Content text")
    def get_active_section_text(self):
        return self.baseclass.get_text(self.__active_section_text)

    @allure.step("Get Active Fm Section Content text")
    def get_active_fm_section_text(self):
        return self.baseclass.get_text(self.__fm_active_section_text)

    @allure.step("Check fm Section text strick through")
    def check_fm_section_text_strick_through(self):
        text = self.baseclass.wait_until(
            self.__fm_deleted_section
        ).value_of_css_property("text-decoration")
        if "line-through" in text:
            return True
        else:
            return False

    @allure.step("Get Section indicator")
    def get_section_indicator(self, section_name):
        self.baseclass.wait_loadder_dissappried()
        section = self.baseclass.wait_until_elements(self.__section_name_toc)
        att_value = ""
        for i in section:
            if section_name in i.text:
                att_value = self.baseclass.wait_until_elements(
                    self.__section_green_indicator
                )[section.index(i)].get_attribute("class")
                break
        if "greenlight text-greenlight" in att_value:
            return "Green"
        elif "in-progress text-in-progress" in att_value:
            return "Red"
        with allure.step(att_value):
            pass

    @allure.step("Get Sub-Section indicator")
    def get_sub_section_indicator(self, subsection_name):
        self.baseclass.wait_loadder_dissappried()
        sub_section = self.baseclass.wait_until_elements(self.__sub_section_name_toc)
        att_value = ""
        for i in sub_section:
            if subsection_name in i.text:
                att_value = self.baseclass.wait_until_elements(
                    self.__sub_section_green_indicator
                )[sub_section.index(i)].get_attribute("class")
                break
        if "greenlight text-greenlight" in att_value:
            return "Green"
        elif "in-progress text-in-progress" in att_value:
            return "Red"

    @allure.step("Get Section name from toc")
    def get_no_section_title_toc(self, section_name):
        section = self.baseclass.wait_until_elements(self.__section_name_toc)
        for i in section:
            if section_name in i.text:
                return i.text
        else:
            raise Exception(f"{section_name} is not showing on toc")

    @allure.step("Get hidden fm section name")
    def get_fm_hidden_title_name(self, section_type):
        if section_type == "SECTION_CONTENT":
            return self.baseclass.get_text_javascript_executor(
                self.__fm_active_section_heading
            )
        elif section_type == "FIGURE_CONTENT":
            return self.baseclass.get_text_javascript_executor(
                self.__active_fig_title_text
            )
        elif section_type == "TABLE_CONTENT":
            pass

    @allure.step("Get current ordinal")
    def get_current_ordinal(self):
        text = self.baseclass.get_text_javascript_executor(self.__current_ordinal)
        with allure.step(text):
            return text

    @allure.step("Enter new ordinal {text}")
    def enter_new_ordinal_text(self, text):
        self.action.click(self.baseclass.wait_until(self.__new_ordinal)).send_keys(
            text
        ).perform()

    @allure.step("click on {button_text}")
    def click_relocate_alt_button(self, button_text):
        for i in self.baseclass.wait_until_elements(self.__relocate_alert_buttons):
            if button_text in i.text:
                if i.is_enabled():
                    i.click()
                    break
        else:
            raise Exception(f"{button_text} is not enabled or showing")

    @allure.step("Get validate ordinal message")
    def get_validate_message(self):
        text = self.baseclass.get_text(self.__alert_text)
        with allure.step(text):
            return text

    @allure.step("click on Delete conformation Checkbox")
    def click_on_delete_checkbox(self):
        self.baseclass.click(self.__checkbox)

    @allure.step("Upload Figure")
    def upload_figure(self, file_path):
        element = self.baseclass.wait_until(self.__fig_upload)
        element.send_keys(os.path.abspath(file_path))
        # image = self.baseclass.wait_until(self.__uploaded_fig)
        # return image.is_displayed()

    @allure.step("Get uploaded fig name")
    def get_fig_file_name(self):
        text = self.baseclass.get_text(self.__fig_name)
        with allure.step(text):
            return text

    @allure.step("Click on Active Fig")
    def click_active_fig(self):
        self.baseclass.click(self.__active_fig)

    @allure.step("Check Fig is display and get Fig alt text")
    def check_fig_showing_get_alt_text(self):
        fig = self.baseclass.wait_until(self.__active_fig)
        if fig.is_displayed():
            return fig.get_attribute("alt")
        else:
            raise Exception("Fig is not showing")

    @allure.step("Get Fig Above text")
    def get_fig_above_text(self):
        text = self.baseclass.get_text(self.__active_fig_above_text)
        with allure.step(text):
            return text

    @allure.step("Get Fig Below text")
    def get_fig_below_text(self):
        text = self.baseclass.get_text(self.__active_fig_below_text)
        with allure.step(text):
            return text

    @allure.step("Get Fig Title")
    def get_fig_title_text(self):
        text = " ".join(
            [
                i.text
                for i in self.baseclass.wait_until_elements(
                    self.__active_fig_title_text
                )
            ]
        )
        with allure.step(text):
            return text

    @allure.step("Check Figure text strick through")
    def check_figure_text_strick_through(self):
        text = self.baseclass.wait_until(self.__deleated_figure).value_of_css_property(
            "text-decoration"
        )
        if "line-through" in text:
            return True
        else:
            return False
