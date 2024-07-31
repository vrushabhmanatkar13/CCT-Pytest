import time
import pytest
from test_cases import conftest
from test_cases.test_base import SUCCESS, Test_Base
from uitility.baseclass import Baseclass
import allure

VIEW_PROJECT = conftest.json_obj["Dashboard"]["view_project"]
CHAPTER_VERSION = conftest.json_obj["Dashboard"]["chapter_version"]
DEF_MANAGEMENT = conftest.json_obj["Project View"]["def_management"]
EXT_LINK_MANAGEMENT = conftest.json_obj["Project View"]["ext_link_management"]
LOAD_PROPOSALS = conftest.json_obj["Project View"]["load_proposals"]
SHOW_CHAP_VERSION = conftest.json_obj["Project View"]["show_chap_version"]
SAVE_ORDER = conftest.json_obj["Project View"]["save_order"]


@pytest.mark.View_Project
@pytest.mark.order(index=3)
@allure.tag("Project View Page")
@allure.epic("Project Overview")
class Test_View_Project_Page(Test_Base):

    @allure.feature("Defination Managemant")
    @allure.title("Verify Defination Management")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_verify_defination_managemant(self):
        project_name = self.dashboardpage.check_project_display(
            "2021 International Mechanical Code"
        )
        self.dashboardpage.click_project_name(project_name)
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_book_management_button(DEF_MANAGEMENT)
        previos_breadcum = self.viewprojectpage.get_previos_breadcum()
        current_breadcum = self.viewprojectpage.get_book_managament_breadcum()
        opened_defination = self.def_managemnat.click_on_defiantion(
            "ABRASIVE MATERIALS"
        )
        def_breadcum = self.viewprojectpage.get_book_managament_breadcum()
        Baseclass.assert_equals(project_name, previos_breadcum)
        Baseclass.assert_equals(DEF_MANAGEMENT, current_breadcum)
        Baseclass.assert_equals(def_breadcum, opened_defination)
        Baseclass.assert_equals(opened_defination, def_breadcum)

    @allure.feature("Defination Managemant")
    @allure.title("Verify Search and clear defination")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_search_clear_defination(self):
        project_name = self.dashboardpage.check_project_display(
            "2021 International Mechanical Code"
        )
        self.dashboardpage.click_project_name(project_name)
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)

        self.viewprojectpage.click_on_book_management_button(DEF_MANAGEMENT)
        defination = self.def_managemnat.search_defination("PIPING")
        result = self.def_managemnat.check_defination_present(defination)
        defination_1 = self.def_managemnat.get_first_defination()
        self.def_managemnat.click_clear_defination()
        defination_2 = self.def_managemnat.get_first_defination()
        Baseclass.assert_true(result)
        Baseclass.assert_not_equals(defination_1, defination_2)

    @allure.feature("External Links Management")
    @allure.title("Verify External Links Management")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_verify_external_link_management(self):
        project_name = self.dashboardpage.check_project_display(
            "2021 International Mechanical Code"
        )
        self.dashboardpage.click_project_name(project_name)
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)

        self.viewprojectpage.click_on_book_management_button(EXT_LINK_MANAGEMENT)
        current_breadcum = self.viewprojectpage.get_book_managament_breadcum()
        heading = self.link_managemant.get_page_heading()
        Baseclass.assert_equals(EXT_LINK_MANAGEMENT, current_breadcum)
        Baseclass.assert_equals(EXT_LINK_MANAGEMENT, heading)

    @allure.feature("Cahpter Versions")
    @allure.title("Verify chapter version count and it clickable")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_chapter_version_clickable_count(self):
        project_name = self.dashboardpage.check_project_display(
            "2021 International Mechanical Code"
        )
        self.dashboardpage.click_project_name(project_name)
        dashboard_version = self.dashboardpage.get_chapter_version_count()
        dashboard_clickable = self.dashboardpage.get_button_clickable(CHAPTER_VERSION)
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        time.sleep(4)
        viewpage_version = self.viewprojectpage.get_chapter_version_count()
        viewpage_clickable = self.viewprojectpage.get_book_management_button_clickable(
            SHOW_CHAP_VERSION
        )
        Baseclass.assert_false(dashboard_clickable)
        Baseclass.assert_equals(dashboard_version, viewpage_version)
        Baseclass.assert_false(viewpage_clickable)

    @allure.feature("Smart Index")
    @allure.title("Verify open chapter, Fm chapter, Appendix and Index")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(
        "chapter_name",
        [
            "PREFACE",
            "CHAPTER 2 DEFINITIONS",
            "INDEX",
        ],
    )
    def test_verify_chapter_status(self, chapter_name):
        project_name = self.dashboardpage.check_project_display(
            "2021 International Mechanical Code"
        )
        self.dashboardpage.click_project_name(project_name)
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)

        status_1 = self.viewprojectpage.get_chapter_status(chapter_name)
        self.viewprojectpage.click_on_chapter(chapter_name)
        time.sleep(2)
        breadcum = self.viewprojectpage.get_current_breadcum()
        status_2 = self.chap_overview.get_chapter_status()
        Baseclass.assert_equals(status_1, status_2)
        assert breadcum in chapter_name

    @allure.feature("Sort Order")
    @allure.title("Verify Fm_chapter name on sort order popup")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_Fm_chapter_names(self):
        project_name = self.dashboardpage.check_project_display(
            "2021 International Mechanical Code"
        )
        self.dashboardpage.click_project_name(project_name)
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)

        fm_chap_smt_index = self.viewprojectpage.get_all_fm_chapter_name()
        self.viewprojectpage.click_sort_order_button()
        fm_chap_popup = self.viewprojectpage.get_fm_chapter_name_on_sortorder()
        Baseclass.assert_equals(fm_chap_smt_index, fm_chap_popup)

    @allure.feature("Sort Order")
    @allure.title("Verify change sequence of Fm chapter")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_verify_change_sequence_of_Fm_chapter(self):
        project_name = self.dashboardpage.check_project_display(
            "2021 International Mechanical Code"
        )
        self.dashboardpage.click_project_name(project_name)
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.get_project_heading_name()
        self.viewprojectpage.click_sort_order_button()
        time.sleep(2)
        self.viewprojectpage.drag_drop_fm_chapter("COPYRIGHT", "PREFACE")
        fm_chap_popup = self.viewprojectpage.get_fm_chapter_name_on_sortorder()
        self.viewprojectpage.click_button_on_sort_order(SAVE_ORDER)
        alert_msg = self.viewprojectpage.get_alert_message()
        fm_chap_smt_index = self.viewprojectpage.get_all_fm_chapter_name()
        Baseclass.assert_equals(fm_chap_smt_index, fm_chap_popup)
        Baseclass.assert_equals(SUCCESS, alert_msg)
