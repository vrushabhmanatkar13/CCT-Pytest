import time

import pytest
from test_cases import conftest
from test_cases.test_base import Test_Base
from uitility.baseclass import Baseclass
import allure

VIEW_PROJECT = conftest.json_obj["Dashboard"]["view_project"]
PROJECT_DETAILS = conftest.json_obj["Dashboard"]["project_details"]
CHAPTER_VERSION = conftest.json_obj["Dashboard"]["chapter_version"]
DELETE = conftest.json_obj["Dashboard"]["delete"]
CLOSE = conftest.json_obj["Dashboard"]["close"]
RE_OPEN = conftest.json_obj["Dashboard"]["re-open"]
YES = conftest.json_obj["Dashboard"]["yes"]

PROJECT_NAME = conftest.json_obj["Add Project"]["project_name"]
TITLE = conftest.json_obj["Add Project"]["title"]


@pytest.mark.Dashboard
@pytest.mark.order(index=1)
@allure.feature("Dashboard")
@allure.tag("Dahsboard Page")
class Test_Dashboard_Page(Test_Base):

    @allure.title("Verify chnage tabs")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        ["tab_name", "url"],
        [
            ("INACTIVE PROJECTS", "inactive"),
            ("CONTENT FINAL", "blueline"),
        ],
    )
    def test_change_tabs(self, tab_name, url):
        project_name_1 = self.dashboardpage.get_first_project_name()
        self.dashboardpage.click_tabs(tab_name)
        time.sleep(0.5)
        project_name_2 = self.dashboardpage.get_first_project_name()
        current_url = self.driver.current_url
        Baseclass.assert_equals(conftest.url + "projects/" + url, current_url)
        Baseclass.assert_not_equals(project_name_1, project_name_2)

    @allure.title("Verify select category")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "tab_name",
        ["ACTIVE PROJECTS", "INACTIVE PROJECTS", "CONTENT FINAL"],
    )
    def test_select_category(self, tab_name):
        self.dashboardpage.click_tabs(tab_name)
        category_name = self.dashboardpage.get_first_category()
        result = self.dashboardpage.select_category(category_name)
        text = self.dashboardpage.get_selected_category()
        Baseclass.assert_equals(text, category_name)
        Baseclass.assert_true(result)

    @allure.title("Verify clear category")
    @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.parametrize(
    #     "tab_name",
    #     ["ACTIVE PROJECTS", "INACTIVE PROJECTS", "CONTENT FINAL"],
    # )
    def test_clear_category(self):
        # self.dashboardpage.click_tabs(tab_name)
        category_name = self.dashboardpage.get_first_category()
        self.dashboardpage.select_category(category_name)
        time.sleep(0.5)
        category_project = self.dashboardpage.get_project_count()
        self.dashboardpage.click_clear_category()
        result = self.dashboardpage.get_selecated_category_displayed()
        project_count = self.dashboardpage.get_project_count()
        Baseclass.assert_true(result)
        Baseclass.assert_not_equals(category_project, project_count)

    @allure.title("Verify search title")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        ("tab_name", "title"),
        [
            ("ACTIVE PROJECTS", "IEBC2021 First Printing"),
            ("INACTIVE PROJECTS", "2021 IECC"),
            ("CONTENT FINAL", "2021 International Fire Code"),
        ],
    )
    def test_search_text_title_textbox(self, tab_name, title):
        self.dashboardpage.click_tabs(tab_name)
        self.dashboardpage.enter_text_title_textbox(title)
        result = self.dashboardpage.get_row_data_text(title)
        Baseclass.assert_true(result)

    @allure.title("Verify clear title")
    @allure.severity(allure.severity_level.NORMAL)
    def test_clear_title_textbox(self):
        project_name = self.dashboardpage.get_first_project_name()
        self.dashboardpage.enter_text_title_textbox(project_name)
        result_count = self.dashboardpage.get_project_count()
        time.sleep(0.5)
        self.dashboardpage.click_clear_title()
        project__count = self.dashboardpage.get_project_count()
        Baseclass.assert_not_equals(project__count, result_count)

    @allure.title("Verify project buttons")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        ["tab_name", "button_name"],
        [
            (
                "ACTIVE PROJECTS",
                [VIEW_PROJECT, PROJECT_DETAILS, CHAPTER_VERSION, CLOSE],
            ),
            (
                "INACTIVE PROJECTS",
                [VIEW_PROJECT, RE_OPEN, CHAPTER_VERSION, DELETE],
            ),
            (
                "CONTENT FINAL",
                [VIEW_PROJECT, PROJECT_DETAILS, CHAPTER_VERSION, RE_OPEN],
            ),
        ],
    )
    def test_get_dashboard_button_text(self, tab_name, button_name):
        self.dashboardpage.click_tabs(tab_name)
        self.dashboardpage.click_project_row(1)
        texts = self.dashboardpage.get_dashboard_button_text()
        Baseclass.assert_equals(button_name, texts)

    @allure.title("Verify view project button")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(
        "tab_name",
        ["ACTIVE PROJECTS", "INACTIVE PROJECTS", "CONTENT FINAL"],
    )
    def test_view_project(self, tab_name):
        self.dashboardpage.click_tabs(tab_name)
        project_name_1 = self.dashboardpage.get_first_project_name()
        self.dashboardpage.click_project_name(project_name_1)
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        project_name_2 = self.viewprojectpage.get_project_heading_name()
        Baseclass.assert_equals(project_name_2, project_name_1)

    @allure.title("Verify project details button")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(
        "tab_name",
        ["ACTIVE PROJECTS", "CONTENT FINAL"],
    )
    def test_project_details(self, tab_name):
        self.dashboardpage.click_tabs(tab_name)
        project_name_1 = self.dashboardpage.get_first_project_name()
        title_name_1 = self.dashboardpage.get_first_title_name()
        self.dashboardpage.click_project_name(project_name_1)
        self.dashboardpage.click_dashboard_button(PROJECT_DETAILS)
        time.sleep(4)
        project_name_2 = self.addproject_page.get_filled_text(PROJECT_NAME)
        title_name_2 = self.addproject_page.get_filled_text(TITLE)
        Baseclass.assert_equals(project_name_2, project_name_1)
        Baseclass.assert_equals(title_name_2, title_name_1)

    @allure.title("Verify add project button")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_project_button(self):
        self.dashboardpage.click_add_project()
        text = self.addproject_page.get_page_title()
        self.addproject_page.click_close_icon()
        Baseclass.assert_equals("Add Project", text)

    @allure.title("Verify remove project")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(
        ("tab_name", "alert_text"),
        [("ACTIVE PROJECTS", CLOSE), ("INACTIVE PROJECTS", DELETE)],
    )
    def test_remove_project(self, tab_name, alert_text):
        self.dashboardpage.click_tabs(tab_name)
        project_name = self.dashboardpage.check_project_display(
            "2021 International Mechanical Code"
        )
        self.dashboardpage.enter_text_title_textbox(project_name)
        self.dashboardpage.click_project_name(project_name)
        self.dashboardpage.click_dashboard_button(alert_text)
        act_alert_text = self.dashboardpage.get_alert_text()
        self.dashboardpage.click_on_alert_button(YES)
        self.dashboardpage.wait_alert_dissappired()
        Baseclass.assert_equals(alert_text + " Project?", act_alert_text)
        Baseclass.assert_true(self.dashboardpage.project_row_is_displayed())
