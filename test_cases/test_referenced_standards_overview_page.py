import time
import pytest
from test_cases import conftest
from test_cases.test_base import SUCCESS, YES_PROCEED, Test_Base
import allure

from test_cases.test_chapter_overview_page import (
    CANCEL,
    CHAPTER_TITLE,
    NEW_CODE_ELEMENT,
    OPEN_CHAPTER,
    SAVE_DRAFT,
    SAVE_FINAL,
    VALID_ORDINAL,
    VALIDATE_LOCATION,
)
from test_cases.test_view_project_page import VIEW_PROJECT
from uitility.baseclass import Baseclass

PROMULGATOR = conftest.json_obj["New Code Element"]["promulgator"]
SET_PROMU_ORDINAL = conftest.json_obj["Content Edit"]["set_promulgator_ordinal"]
RELOCATE_PROMU = conftest.json_obj["Relocate alert"]["relocate_promulgator"]

PROMU_FULL_NAME = conftest.json_obj["Content Edit"]["promulgator_full_name"]
PROMU_ACRONYM = conftest.json_obj["Content Edit"]["promulgator_acronym"]
PROMU_URL = conftest.json_obj["Content Edit"]["promulgator_url"]
PROMU_STREET_ADDRESS = conftest.json_obj["Content Edit"]["promulgator_street_address"]
PROMU_CITY = conftest.json_obj["Content Edit"]["promulgator_city"]
PROMU_STATE = conftest.json_obj["Content Edit"]["promulgator_state"]
PROMU_POSTAL_CODE = conftest.json_obj["Content Edit"]["promulgator_postal_code"]


@pytest.mark.Referenced_Standards
@pytest.mark.order(index=7)
@allure.epic("Referenced_Standards")
class Test_Referenced_Standards_Overview(Test_Base):

    @allure.feature("Referenced_Standards")
    @allure.title("Verify Open Referenced_Standards chapter status")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_verify_open_referenced_standards_chapter_status(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        status_overview_page = self.viewprojectpage.get_chapter_status(
            "CHAPTER 15 REFERENCED STANDARDS"
        )
        self.viewprojectpage.click_on_chapter("CHAPTER 15 REFERENCED STANDARDS")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        chap_status = self.chap_overview.get_chapter_status_toc()
        heading = self.chap_overview.get_chapter_heading()
        Baseclass.assert_equals(status_overview_page, chap_status)
        assert "CHAPTER 15 REFERENCED STANDARDS" in heading

    @allure.feature("Referenced_Standards")
    @allure.title("Verify Cancel Edited Referenced_Standards chapter content")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_cancel_edit_referenced_standards_chapter(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 15 REFERENCED STANDARDS")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        act_chap_name = self.chap_overview.get_chapter_heading()
        time.sleep(0.5)
        self.chap_overview.click_on_chapter()
        self.chap_overview.enter_text_in_textbox(CHAPTER_TITLE, " UPDATE")
        edited_text = self.chap_overview.get_edit_heading_text()
        self.chap_overview.click_edit_page_button(CANCEL)
        time.sleep(0.5)
        self.chap_overview.click_on_alert_button(YES_PROCEED)
        heading = self.chap_overview.get_chapter_heading()
        Baseclass.assert_equals(act_chap_name, heading)
        assert "UPDATE" in edited_text

    @allure.feature("Promulgator")
    @allure.title("Verify Cancel Edited Promulgator")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_cancel_edit_promulgator(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 15 REFERENCED STANDARDS")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        time.sleep(0.5)
        self.chap_overview.click_on_section_on_toc("ACCA")
        prom_name = self.ref_standards.get_promulgator_info("name")
        self.chap_overview.click_on_active_content()
        self.chap_overview.enter_text_in_textbox(PROMU_FULL_NAME, " UPDATE")
        self.chap_overview.click_edit_page_button(CANCEL)
        self.chap_overview.click_on_alert_button(YES_PROCEED)
        prom_name_2 = self.ref_standards.get_promulgator_info("name")
        Baseclass.assert_equals(prom_name, prom_name_2)

    @allure.feature("Referenced Standards")
    @allure.title("Verify Cancel Edited Referenced Standard")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_cancel_edit_referenced_standard(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 15 REFERENCED STANDARDS")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        time.sleep(0.5)
        self.chap_overview.click_on_section_on_toc("ACCA")
        ref_number = self.ref_standards.get_reference_standard_info("number", 0)
        self.chap_overview.click_on_active_content()
        self.chap_overview.enter_text_in_textbox("Number", " UPDATE")
        self.chap_overview.click_edit_page_button(CANCEL)
        self.chap_overview.click_on_alert_button(YES_PROCEED)
        ref_number_2 = self.ref_standards.get_reference_standard_info("number", 0)
        Baseclass.assert_equals(ref_number, ref_number_2)

    @allure.feature("Promulgator")
    @allure.title("Verify Add Promulgator")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency()
    def test_verify_add_promulgator(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 15 REFERENCED STANDARDS")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.header_footer.click_on_add_new()
        time.sleep(0.5)
        self.header_footer.click_on_model_list(NEW_CODE_ELEMENT)
        self.header_footer.click_on_code_element_button(PROMULGATOR)
        self.chap_overview.enter_text_in_textbox(PROMU_FULL_NAME, "Automation Testing")
        self.chap_overview.click_edit_page_button(SET_PROMU_ORDINAL)
        time.sleep(0.5)
        self.chap_overview.enter_new_ordinal_text("TEST")
        self.chap_overview.click_relocate_alt_button(VALIDATE_LOCATION)
        validate_msg = self.chap_overview.get_validate_message()
        self.chap_overview.click_relocate_alt_button(RELOCATE_PROMU)
        acronym = self.chap_overview.get_filled_text(PROMU_ACRONYM)
        self.chap_overview.enter_text_in_textbox(PROMU_URL, "https://www.iccsafe.org/")
        self.chap_overview.enter_text_in_textbox(
            PROMU_STREET_ADDRESS, "4051 Flossmoor Road"
        )
        self.chap_overview.enter_text_in_textbox(PROMU_CITY, "Country Club Hills")
        self.chap_overview.enter_text_in_textbox(PROMU_STATE, "IL")
        self.chap_overview.enter_text_in_textbox(PROMU_POSTAL_CODE, "60478")
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        draft_msg = self.viewprojectpage.get_alert_message()
        promu_status = self.chap_overview.get_section_indicator(acronym)

        promu_acronum = self.ref_standards.get_promulgator_acronym_text()
        promu_url = self.ref_standards.get_promulgaotr_url()
        promu_full_name = self.ref_standards.get_promulgator_info("name")
        promu_street_address = self.ref_standards.get_promulgator_info("street_address")
        promu_city = self.ref_standards.get_promulgator_info("city")
        promu_state = self.ref_standards.get_promulgator_info("state")
        promu_postal_code = self.ref_standards.get_promulgator_info("postal_code")

        Baseclass.assert_equals(VALID_ORDINAL, validate_msg)
        Baseclass.assert_equals("TEST", acronym)
        Baseclass.assert_equals(SUCCESS, draft_msg)
        Baseclass.assert_equals("Red", promu_status)

        Baseclass.assert_equals(acronym, promu_acronum)
        Baseclass.assert_equals("https://www.iccsafe.org/", promu_url)
        Baseclass.assert_equals("Automation Testing", promu_full_name)
        Baseclass.assert_equals("4051 Flossmoor Road", promu_street_address)
        Baseclass.assert_equals("Country Club Hills", promu_city)
        Baseclass.assert_equals("IL", promu_state)
        Baseclass.assert_equals("60478", promu_postal_code)

    @allure.feature("Referenced Standards")
    @allure.title("Verify Add Referenced Standard")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(depends=["test_verify_add_promulgator"], scope="class")
    def test_verify_add_referenced_standard(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 15 REFERENCED STANDARDS")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        time.sleep(0.5)
        self.chap_overview.click_on_section_on_toc("TEST")
        self.chap_overview.click_on_active_content()
        self.chap_overview.click_edit_page_button("Add New Referenced Standard")
        count = self.ref_standards.get_referenced_standard_count()
        self.chap_overview.enter_text_in_textbox("Number", "TEST-2024", clear=True)
        self.chap_overview.enter_text_in_textbox(
            "Title", "Automation Test standards", clear=True
        )
        self.ref_standards.enter_section_number(301.1)
        lablel = self.ref_standards.get_section_lable()
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        draft_msg = self.viewprojectpage.get_alert_message()
        draft_indicator = self.chap_overview.get_section_indicator("TEST")

        # Get Ref standard Information
        ref_number = self.ref_standards.get_reference_standard_info("number", 0)
        ref_title = self.ref_standards.get_reference_standard_info("title", 0)
        ref_sections = self.ref_standards.get_referenced_standard_sections(ref_title)
        # Save Final
        self.chap_overview.click_on_active_content()
        self.chap_overview.enter_text_in_textbox("Title", " Final")
        self.chap_overview.click_edit_page_button(SAVE_FINAL)
        final_msg = self.viewprojectpage.get_alert_message()
        final_indicator = self.chap_overview.get_section_indicator("TEST")
        final_ref_title = self.ref_standards.get_reference_standard_info("title", 0)

        Baseclass.assert_equals("1", count)
        assert "301.1" in lablel
        Baseclass.assert_equals(SUCCESS, draft_msg)
        Baseclass.assert_equals("TEST-2024", ref_number)
        Baseclass.assert_equals("Automation Test standards", ref_title)
        Baseclass.assert_equals(lablel, ref_sections)
        Baseclass.assert_equals("Red", draft_indicator)
        Baseclass.assert_equals(SUCCESS, final_msg)
        Baseclass.assert_equals(ref_title + " Final", final_ref_title)
        Baseclass.assert_equals("Green", final_indicator)

    @allure.feature("Referenced Standards")
    @allure.title("Verify Remove Section Referencing Standard")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(
        depends=["test_verify_add_referenced_standard"], scope="class"
    )
    def test_verify_remove_section_referencing_standard(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 15 REFERENCED STANDARDS")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        time.sleep(0.5)
        self.chap_overview.click_on_section_on_toc("TEST")
        ref_title = self.ref_standards.get_reference_standard_info("title", 0)
        self.chap_overview.click_on_active_content()
        lablel = self.ref_standards.get_section_lable()[0]
        self.ref_standards.click_close_section_lable(lablel)
        self.chap_overview.click_edit_page_button(SAVE_FINAL)
        final_msg = self.viewprojectpage.get_alert_message()
        ref_sections = self.ref_standards.get_referenced_standard_sections(ref_title)

        Baseclass.assert_true(len(ref_sections) == 0)
        Baseclass.assert_equals(SUCCESS, final_msg)
