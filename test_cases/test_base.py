import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from page_objects.add_edit_project_page import Add_Edit_Project_Page
from page_objects.appendix_overview_page import Appendix_Overview_Page
from page_objects.chapter_overview_page import Chapter_Overview_page
from page_objects.dashboard_page import Dashboard_Page
from page_objects.defination_management_page import Defination_Management
from page_objects.external_link_management_page import External_Link_Management
from page_objects.header_footer import Header_Footer
from page_objects.login_page import Login_Page
from page_objects.view_project_page import View_Project_Page
import test_cases.conftest as conftest
from uitility.baseclass import Baseclass
import allure

HOME_PAGE = conftest.json_obj["Page Titles"]["home_page"]
SUCCESS = conftest.json_obj["Alert"]["success"]
ERROR = conftest.json_obj["Alert"]["error"]
YES_PROCEED = conftest.json_obj["Alert"]["yes_proceed"]
ALT_CANCEL = conftest.json_obj["Alert"]["cancel"]


# @pytest.mark.usefixtures("test_base")
class Test_Base:

    driver: WebDriver

    @allure.title(
        "Fixture (Class Level): Setup WebDriver,Baseclass Objects and TearDown Delete all cookies"
    )
    @pytest.fixture(scope="class", autouse=True)
    def before_class(self, launch_browser):
        with allure.step("Asign objects"):
            Test_Base.driver = launch_browser
            Test_Base.baseclass = Baseclass(self.driver, conftest.webdriver_wait)
            Test_Base.loginpage = Login_Page(self.baseclass)
        with allure.step("Run Login Action before test class"):
            if self.__class__.__name__ != "Test_Login_Page":
                self.loginpage.login("ct-super-admin-test@iccsafe.org", "Password5")
                self.baseclass.wait_until_get_title(HOME_PAGE)
        with allure.step("Delete all cookies"):
            yield
            self.driver.delete_all_cookies()
            self.driver.refresh()

    @allure.title(
        "Fixture (Funcation Level): Navigate to Home page and Create Object of Page class"
    )
    @pytest.fixture(scope="function", autouse=True)
    def setup_class_objects(self):
        with allure.step("Navigate to Home page and create page class objects"):
            self.driver.get(conftest.url)

            if self.baseclass.is_alert_present():
                self.driver.switch_to.alert.accept()

            self.dashboardpage = Dashboard_Page(self.baseclass)
            self.viewprojectpage = View_Project_Page(self.baseclass)
            self.addproject_page = Add_Edit_Project_Page(self.baseclass)
            self.def_managemnat = Defination_Management(self.baseclass)
            self.link_managemant = External_Link_Management(self.baseclass)
            self.chap_overview = Chapter_Overview_page(self.baseclass)
            self.header_footer = Header_Footer(self.baseclass)
            self.appen_overview = Appendix_Overview_Page(self.baseclass)

    # @pytest.fixture(scope="class", autouse=True)
    # def setup_class(self):
    #     if self.__class__.__name__ != "Test_Login_Page":
    #         self.loginpage.login("ct-super-admin-test@iccsafe.org", "Password5")
    #         self.baseclass.wait_until_get_title("Correlation-Tool Book Dashboard")
