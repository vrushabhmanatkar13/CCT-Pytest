import datetime
import random
import string
import time
import allure
import pytest
from test_cases import conftest
from test_cases.test_base import Test_Base
from test_cases.test_dashboard_page import (
    CLOSE,
    DELETE,
    PROJECT_NAME,
    TITLE,
    VIEW_PROJECT,
    YES,
)
from uitility.baseclass import Baseclass

SELECT_BASE_BOOK = conftest.json_obj["Add Project"]["select_base_book"]
ADD_PROJECT = conftest.json_obj["Add Project"]["add_project"]
CANCEL = conftest.json_obj["Add Project"]["cancel"]
CLEAR_FROM = conftest.json_obj["Add Project"]["clear_from"]
SELECT = conftest.json_obj["Base Book"]["select"]

GROUP = conftest.json_obj["Base Book"]["group"]
BOOK_YEAR = conftest.json_obj["Base Book"]["book_year"]
PRINTING = conftest.json_obj["Base Book"]["printing"]
BOOK = conftest.json_obj["Base Book"]["book"]

PROJECT_TYPE = conftest.json_obj["Add Project"]["project_type"]
VERSION_TYPE = conftest.json_obj["Add Project"]["version_type"]
CATEGORY = conftest.json_obj["Add Project"]["category"]


@pytest.mark.Add_Project
@pytest.mark.order(index=2)
@allure.feature("Add Project")
@allure.tag("Add Project Page")
class Test_Add_Project_Page(Test_Base):

    @allure.title("Verify Cancel to Add project")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cancel_to_add_project(self):
        self.dashboardpage.click_add_project()
        self.addproject_page.click_on_button(CANCEL)
        text = self.dashboardpage.get_dashboard_page_text()
        Baseclass.assert_equals("Projects", text)

    @allure.title("Verify Add project button is enlabed")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_project_enalbed(self):
        self.dashboardpage.click_add_project()
        result = self.addproject_page.is_add_project_enalbed()
        Baseclass.assert_false(result)

    @allure.title("Verify Select Base Book")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_select_base_book(self):
        self.dashboardpage.click_add_project()
        self.addproject_page.wait_buttons_to_load()
        self.addproject_page.click_on_button(SELECT_BASE_BOOK)
        group = self.addproject_page.click_select_option(GROUP, "I-Codes")
        Baseclass.assert_equals("I-Codes", group)
        year = self.addproject_page.click_select_option(BOOK_YEAR, "2021")
        Baseclass.assert_equals("2021", year)
        printing = self.addproject_page.click_select_option(PRINTING, "DefaultPrinting")
        Baseclass.assert_equals("DefaultPrinting", printing)
        book = self.addproject_page.click_select_option(
            BOOK, "2021 International Fire Code"
        )
        Baseclass.assert_equals("2021 International Fire Code", book)
        self.addproject_page.click_on_button(SELECT)
        base_book = self.addproject_page.get_selected_basebook("Base Book:")
        assert book in base_book

    @allure.title("Verify Clear from button")
    @allure.severity(allure.severity_level.NORMAL)
    def test_clear_from_add_new_project(self):
        self.dashboardpage.click_add_project()
        number = str(random.randint(10, 99))
        self.addproject_page.fill_add_project_form(
            "TEST" + number,
            "Automation Testing",
            "Test" + number,
            "Level 0 - 1st Printing",
            "First Printing",
            "2021 I-Codes",
        )
        self.addproject_page.click_on_button(CLEAR_FROM)
        Baseclass.assert_false(
            self.addproject_page.get_filled_text("Project short code").strip()
        )

        Baseclass.assert_false(self.addproject_page.get_filled_text(PROJECT_NAME))
        Baseclass.assert_false(self.addproject_page.get_filled_text(TITLE))
        Baseclass.assert_false(self.addproject_page.get_selected_option(PROJECT_TYPE))
        Baseclass.assert_false(self.addproject_page.get_selected_option(VERSION_TYPE))
        Baseclass.assert_false(self.addproject_page.get_selected_option(CATEGORY))
        Baseclass.assert_true(self.addproject_page.get_error_message())

    @pytest.fixture(scope="function")
    def check_for_duplicate_project(self):
        if (
            self.dashboardpage.check_project_display(
                "2021 International Mechanical Code"
            )
            == "2021 International Mechanical Code"
        ):
            for tab, button in [
                ("ACTIVE PROJECTS", CLOSE),
                ("INACTIVE PROJECTS", DELETE),
            ]:
                self.dashboardpage.click_tabs(tab)
                self.dashboardpage.click_project_name(
                    "2021 International Mechanical Code"
                )
                self.dashboardpage.click_dashboard_button(button)
                self.dashboardpage.click_on_alert_button(YES)
                self.dashboardpage.wait_alert_dissappired()

    @allure.title("Verify Add new project")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures("check_for_duplicate_project")
    def test_add_new_project(self):
        self.dashboardpage.click_add_project()
        self.addproject_page.wait_buttons_to_load()
        self.addproject_page.click_on_button(SELECT_BASE_BOOK)
        self.addproject_page.click_select_option(GROUP, "I-Codes")
        self.addproject_page.click_select_option(BOOK_YEAR, "2021")
        self.addproject_page.click_select_option(PRINTING, "DefaultPrinting")
        book = self.addproject_page.click_select_option(
            BOOK, "2021 International Mechanical Code"
        )
        self.addproject_page.click_on_button(SELECT)
        base_book = (
            self.addproject_page.get_selected_basebook("Base Book: ")
            .replace("- " + book, "")
            .strip()
        )
        time.sleep(2)
        number = str(random.randint(2011, 2024))
        char = random.choice(string.ascii_uppercase)
        self.addproject_page.fill_add_project_form(
            "IMC" + char + number,
            "2021 International Mechanical Code",
            "2021 International Mechanical Code first printing",
            "Level 0 - 1st Printing",
            "First Printing",
            "Test Books",
        )
        time.sleep(4)
        self.addproject_page.click_on_button(ADD_PROJECT)
        current_date = datetime.datetime.now().strftime("%B %e, %Y %H:%M")
        time.sleep(2)
        self.dashboardpage.enter_text_title_textbox(
            "2021 International Mechanical Code first printing"
        )
        Baseclass.assert_equals(
            "2021 International Mechanical Code",
            self.dashboardpage.get_first_project_name(),
        )
        Baseclass.assert_equals(
            "2021 International Mechanical Code first printing",
            self.dashboardpage.get_first_title_name(),
        )
        Baseclass.assert_equals("Test Books", self.dashboardpage.get_first_category())
        Baseclass.assert_equals(base_book, self.dashboardpage.get_first_basebook_name())
        Baseclass.assert_equals(
            "Level 0 - 1st Printing", self.dashboardpage.get_first_project_type()
        )
        Baseclass.assert_equals(
            current_date, self.dashboardpage.get_first_project_modified_date()
        )
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        heading_name = self.viewprojectpage.get_project_heading_name()
        Baseclass.assert_equals("2021 International Mechanical Code", heading_name)
