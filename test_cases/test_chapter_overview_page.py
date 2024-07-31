import time
from test_cases import conftest
from test_cases.test_base import SUCCESS, YES_PROCEED, Test_Base
import pytest
import allure
from test_cases.test_dashboard_page import DELETE, VIEW_PROJECT
from uitility.baseclass import Baseclass

OPEN_CHAPTER = conftest.json_obj["Chapter View"]["open_chapter"]
VALIDATE_LINKS = conftest.json_obj["Chapter View"]["validate_links"]
READY_REL_PUBS = conftest.json_obj["Chapter View"]["ready_rel_pubs"]
RETURN_TO_PUBS = conftest.json_obj["Chapter View"]["return_to_pubs"]
COMPLETE = conftest.json_obj["Chapter View"]["complete"]
CDP_ACCESS_SYN = conftest.json_obj["Chapter View"]["cdp_access_syn"]
NOTES = conftest.json_obj["Chapter View"]["notes"]


SET_CHAP_ORDINAL = conftest.json_obj["Content Edit"]["set_chap_ordinal"]
SET_SECTION_ORDINAL = conftest.json_obj["Content Edit"]["set_section_ordinal"]

SAVE_DRAFT = conftest.json_obj["Content Edit"]["save_draft"]
SAVE_FINAL = conftest.json_obj["Content Edit"]["save_final"]
DELETE_CHAPTER = conftest.json_obj["Content Edit"]["delete_chapter"]
DELETE_SECTION = conftest.json_obj["Content Edit"]["delete_section"]

CANCEL = conftest.json_obj["Content Edit"]["cancel"]
TITLE = conftest.json_obj["Content Edit"]["title"]
CONTENT = conftest.json_obj["Content Edit"]["content"]

CHAPTER_LABEL = conftest.json_obj["Content Edit"]["chapter_label"]
CHAPTER_ORDINAL = conftest.json_obj["Content Edit"]["chapter_ordinal"]
CHAPTER_TITLE = conftest.json_obj["Content Edit"]["chapter_title"]
CHAPTER_CONTENT = conftest.json_obj["Content Edit"]["chapter_content"]

SECTION_ORDINAL = conftest.json_obj["Content Edit"]["section_ordinal"]
SECTION_TITLE = conftest.json_obj["Content Edit"]["section_title"]
SECTION_CONTENT = conftest.json_obj["Content Edit"]["section_content"]


FIG_TITLE = conftest.json_obj["Content Edit"]["fig_title"]
FIG_NOTE_ABOVE = conftest.json_obj["Content Edit"]["fig_note_above"]
FIG_NOTE_BELOW = conftest.json_obj["Content Edit"]["fig_note_below"]
FIG_ALT = conftest.json_obj["Content Edit"]["fig_alt"]

NEW_CHAPTER = conftest.json_obj["Footer_model"]["new_chapter"]
NEW_CODE_ELEMENT = conftest.json_obj["Footer_model"]["new_code_element"]


VALIDATE_LOCATION = conftest.json_obj["Relocate alert"]["validate_location"]
RELOCATE_CHAPTER = conftest.json_obj["Relocate alert"]["relocate_chapter"]
RELOCATE_SECTION = conftest.json_obj["Relocate alert"]["relocate_section"]
RELOCATE_FIG = conftest.json_obj["Relocate alert"]["relocate_fig"]

SECTION = conftest.json_obj["New Code Element"]["section"]
FIGURE = conftest.json_obj["New Code Element"]["figure"]
TABLE = conftest.json_obj["New Code Element"]["table"]
DEFINATION = conftest.json_obj["New Code Element"]["defination"]
REF_STD = conftest.json_obj["New Code Element"]["ref_std"]
EQUATION = conftest.json_obj["New Code Element"]["equation"]


@pytest.mark.Chapter
@pytest.mark.order(index=4)
@allure.epic("Chapter Overview and Content")
@allure.tag("Chapter Overview/Content page")
class Test_Chapter_Overview(Test_Base):

    @allure.feature("Chapter")
    @allure.title("Verify Open Chapter content")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_verify_open_chapter_content(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)

        status_overview_page = self.viewprojectpage.get_chapter_status(
            "CHAPTER 4 VENTILATION"
        )
        self.viewprojectpage.click_on_chapter("CHAPTER 4 VENTILATION")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        chap_status = self.chap_overview.get_chapter_status_toc()
        heading = self.chap_overview.get_chapter_heading()

        Baseclass.assert_equals(status_overview_page, chap_status)
        assert "CHAPTER 4 VENTILATION" in heading

    @allure.feature("Chapter")
    @allure.title("Verify Cancel Edited Chapter content")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_cancel_edit_chapter(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 4 VENTILATION")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        act_chap_name = self.chap_overview.get_chapter_heading()
        time.sleep(0.5)
        self.chap_overview.click_on_chapter()
        self.chap_overview.enter_text_in_textbox(CHAPTER_TITLE, " UPDATE")
        edited_text = self.chap_overview.get_edit_heading_text()
        self.chap_overview.click_edit_page_button(CANCEL)
        time.sleep(1.0)
        self.chap_overview.click_on_alert_button(YES_PROCEED)
        heading = self.chap_overview.get_chapter_heading()
        Baseclass.assert_equals(act_chap_name, heading)
        assert "UPDATE" in edited_text

    @allure.feature("Chapter")
    @allure.title("Verify Edit Chapter Title and Content")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_verify_edit_chapter_title_content(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 4 VENTILATION")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        # Save Draft
        time.sleep(1.0)
        self.chap_overview.click_on_chapter()
        self.chap_overview.edit_contant(CHAPTER_TITLE, "TEST")
        self.chap_overview.edit_contant(CHAPTER_CONTENT, "Test content")
        time.sleep(1.0)
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        alert_draft = self.viewprojectpage.get_alert_message()
        Baseclass.assert_equals(SUCCESS, alert_draft)
        self.baseclass.wait_loadder_dissappried()
        edited_title = self.chap_overview.get_chapter_heading()
        edited_content = self.chap_overview.get_chapter_content_text()
        edited_chapter_toc = self.chap_overview.get_chapter_name_toc()
        current_breadcum = self.viewprojectpage.get_current_breadcum()
        # Save Final
        self.chap_overview.click_on_chapter()
        self.chap_overview.edit_contant(CHAPTER_TITLE, "FINAL")
        self.chap_overview.edit_contant(CHAPTER_CONTENT, "final")
        time.sleep(1.0)
        self.chap_overview.click_edit_page_button(SAVE_FINAL)
        alert_final = self.viewprojectpage.get_alert_message()
        Baseclass.assert_equals(SUCCESS, alert_final)
        self.baseclass.wait_loadder_dissappried()
        final_title = self.chap_overview.get_chapter_heading()
        final_content = self.chap_overview.get_chapter_content_text()
        final_chapter_toc = self.chap_overview.get_chapter_name_toc()
        final_breadcum = self.viewprojectpage.get_current_breadcum()

        Baseclass.assert_equals("CHAPTER 4 VENTILATION TEST", edited_title)
        assert "Test content" in edited_content
        assert "TEST" in edited_chapter_toc
        Baseclass.assert_equals("CHAPTER 4 VENTILATION TEST", current_breadcum)

        Baseclass.assert_equals("CHAPTER 4 VENTILATION TEST FINAL", final_title)
        assert "Test content final" in final_content
        assert "FINAL" in final_chapter_toc
        Baseclass.assert_equals("CHAPTER 4 VENTILATION TEST FINAL", final_breadcum)

    @allure.feature("Chapter")
    @allure.title("Verify Add new chapter")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency()
    def test_verify_add_new_chapter(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        chapter_number = self.viewprojectpage.get_last_cahpter_number()
        self.header_footer.click_on_add_new()
        time.sleep(1.0)
        self.header_footer.click_on_model_list(NEW_CHAPTER)
        self.chap_overview.click_edit_page_button(SET_CHAP_ORDINAL)
        time.sleep(1.0)
        self.chap_overview.enter_new_ordinal_text(chapter_number + 1)
        self.chap_overview.click_relocate_alt_button(VALIDATE_LOCATION)
        validate_text = self.chap_overview.get_validate_message()
        self.chap_overview.click_relocate_alt_button(RELOCATE_CHAPTER)
        chap_ordinal = self.chap_overview.get_filled_text(CHAPTER_ORDINAL)
        self.chap_overview.enter_text_in_textbox(CHAPTER_TITLE, "AUTOMATION TEST")
        self.chap_overview.enter_text_in_textbox(
            CHAPTER_CONTENT, "Automation chapter content"
        )
        time.sleep(1.0)
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        msg = self.viewprojectpage.get_alert_message()
        chap_title = self.chap_overview.get_chapter_heading()
        chap_content = self.chap_overview.get_chapter_content_text()
        currnet_breadcum = self.viewprojectpage.get_current_breadcum()
        self.viewprojectpage.click_pervios_breadcum()
        title = " ".join(["CHAPTER", chap_ordinal, "AUTOMATION TEST"])
        chap_status = self.viewprojectpage.get_chapter_status(title)

        Baseclass.assert_equals("Valid Ordinal", validate_text)
        Baseclass.assert_equals(SUCCESS, msg)
        Baseclass.assert_equals(title, chap_title)
        assert "Automation chapter content" in chap_content
        Baseclass.assert_equals(title, currnet_breadcum)
        Baseclass.assert_equals("Codes Greenlight", chap_status)

    @allure.feature("Section")
    @allure.title("Verify Add new section")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(
        depends=["test_verify_add_new_chapter"],
        scope="class",
    )
    def test_verify_add_new_section(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 16 AUTOMATION TEST")
        chapter_number = self.viewprojectpage.get_cahpter_number(
            "CHAPTER 16 AUTOMATION TEST"
        )

        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.header_footer.click_on_add_new()
        time.sleep(1.0)
        self.header_footer.click_on_model_list(NEW_CODE_ELEMENT)
        self.header_footer.click_on_code_element_button(SECTION)
        self.chap_overview.click_edit_page_button(SET_SECTION_ORDINAL)
        time.sleep(1.0)
        self.chap_overview.enter_new_ordinal_text(chapter_number + "01")
        self.chap_overview.click_relocate_alt_button(VALIDATE_LOCATION)
        validate_text = self.chap_overview.get_validate_message()
        self.chap_overview.click_relocate_alt_button(RELOCATE_SECTION)
        sec_ordinal = self.chap_overview.get_filled_text(SECTION_ORDINAL)
        self.chap_overview.enter_text_in_textbox(SECTION_TITLE, "SECTION DATA")
        time.sleep(1.0)
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        msg = self.viewprojectpage.get_alert_message()
        sec_title = self.chap_overview.get_active_heading_name()
        draft_chap_status = self.chap_overview.get_chapter_status_toc()
        section = " ".join(["SECTION", sec_ordinal, "SECTION DATA"])
        sec_status = self.chap_overview.get_section_indicator(section)
        self.chap_overview.click_on_active_content()
        time.sleep(1.0)
        currnet_breadcum = self.viewprojectpage.get_current_breadcum()
        self.chap_overview.click_edit_page_button(SAVE_FINAL)
        final_msg = self.viewprojectpage.get_alert_message()
        sec_status_final = self.chap_overview.get_section_indicator(section)
        final_chap_status = self.chap_overview.get_chapter_status_toc()

        Baseclass.assert_equals("Valid Ordinal", validate_text)
        Baseclass.assert_equals(SUCCESS, msg)
        Baseclass.assert_equals(section, sec_title)
        Baseclass.assert_equals(section, currnet_breadcum)
        Baseclass.assert_equals("Red", sec_status)
        Baseclass.assert_equals(SUCCESS, final_msg)
        Baseclass.assert_equals("Green", sec_status_final)
        Baseclass.assert_equals("Codes Review", draft_chap_status)
        Baseclass.assert_equals("Codes Greenlight", final_chap_status)

    @allure.feature("Sub-Section")
    @allure.title("Verify Add new sub-section")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(depends=["test_verify_add_new_section"], scope="class")
    def test_verify_add_new_sub_section(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 16 AUTOMATION TEST")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        time.sleep(0.5)
        section_number = self.chap_overview.get_section_number(
            "SECTION 1601 SECTION DATA"
        )
        self.header_footer.click_on_add_new()
        time.sleep(1.0)
        self.header_footer.click_on_model_list(NEW_CODE_ELEMENT)
        self.header_footer.click_on_code_element_button(SECTION)
        self.chap_overview.click_edit_page_button(SET_SECTION_ORDINAL)
        time.sleep(1.0)
        self.chap_overview.enter_new_ordinal_text(section_number + ".1")
        self.chap_overview.click_relocate_alt_button(VALIDATE_LOCATION)
        validate_text = self.chap_overview.get_validate_message()
        self.chap_overview.click_relocate_alt_button(RELOCATE_SECTION)
        subsec_ordinal = self.chap_overview.get_filled_text(SECTION_ORDINAL)
        self.chap_overview.select_section_label("BLANK")
        self.chap_overview.enter_text_in_textbox(SECTION_TITLE, "Sub Section Data")
        self.chap_overview.enter_text_in_textbox(
            SECTION_CONTENT, "Test data from automation"
        )
        time.sleep(1.0)
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        msg = self.viewprojectpage.get_alert_message()
        draft_chap_status = self.chap_overview.get_chapter_status_toc()

        subsec_title = self.chap_overview.get_active_heading_name()
        subsection = " ".join([subsec_ordinal, "Sub Section Data"])
        self.chap_overview.click_on_section_on_toc("SECTION 1601")
        time.sleep(1.0)
        self.chap_overview.click_on_sub_section_on_toc(subsection)
        subsec_status = self.chap_overview.get_sub_section_indicator(subsection)
        self.chap_overview.click_on_active_content()
        time.sleep(1.0)
        currnet_breadcum = self.viewprojectpage.get_current_breadcum()
        self.chap_overview.click_edit_page_button(SAVE_FINAL)
        self.viewprojectpage.get_alert_message()
        time.sleep(1.0)
        sec_status_final = self.chap_overview.get_sub_section_indicator(subsection)
        final_chap_status = self.chap_overview.get_chapter_status_toc()

        Baseclass.assert_equals("Valid Ordinal", validate_text)
        Baseclass.assert_equals(SUCCESS, msg)
        Baseclass.assert_equals(subsection, subsec_title)
        Baseclass.assert_equals(subsection, currnet_breadcum)
        Baseclass.assert_equals("Red", subsec_status)
        Baseclass.assert_equals("Green", sec_status_final)
        Baseclass.assert_equals("Codes Review", draft_chap_status)
        Baseclass.assert_equals("Codes Greenlight", final_chap_status)

    @allure.feature("Figure")
    @allure.title("Verify Add new Figure at section")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(
        name="test_verify_add_figure_at_section",
        depends=["test_verify_add_new_section", "test_verify_add_new_sub_section"],
        scope="class",
    )
    @pytest.mark.parametrize(
        ["section_type", "fig_title", "fig_alt_text"],
        [
            ("Section", "Automation Section Figure", "Fig Alt text"),
            (
                "Sub-Section",
                "Automation Sub Section Figure",
                "Fig Alt text sub section",
            ),
        ],
    )
    def test_verify_add_figure_at_section(self, section_type, fig_title, fig_alt_text):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 16 AUTOMATION TEST")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        if section_type == "Section":
            section_number = self.chap_overview.get_section_number(
                "SECTION 1601 SECTION DATA"
            )
        else:

            self.chap_overview.click_on_section_on_toc("SECTION 1601 SECTION DATA")
            time.sleep(1.0)
            section_number = self.chap_overview.get_sub_section_number(
                "1601.1 Sub Section Data"
            )
        self.header_footer.click_on_add_new()
        time.sleep(1.0)
        self.header_footer.click_on_model_list(NEW_CODE_ELEMENT)
        self.header_footer.click_on_code_element_button(FIGURE)
        self.chap_overview.click_edit_page_button("Set Figure Ordinal")
        time.sleep(1.0)
        self.chap_overview.enter_new_ordinal_text(section_number)
        self.chap_overview.click_relocate_alt_button(VALIDATE_LOCATION)
        validate_text = self.chap_overview.get_validate_message()
        self.chap_overview.click_relocate_alt_button(RELOCATE_FIG)

        # fig_name = self.chap_overview.get_fig_file_name()                         # feature is changed
        self.chap_overview.enter_text_in_textbox(FIG_NOTE_ABOVE, "Fig Above text")
        self.chap_overview.enter_text_in_textbox(FIG_NOTE_BELOW, "Fig Below text")
        self.chap_overview.enter_text_in_textbox(FIG_TITLE, fig_title)
        self.chap_overview.enter_text_in_textbox(FIG_ALT, fig_alt_text)
        result = self.chap_overview.upload_figure("Test Data/JPG_Valid.jpeg")
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        draft_msg = self.viewprojectpage.get_alert_message()
        self.chap_overview.click_on_section_on_toc("SECTION 1601 SECTION DATA")
        time.sleep(1.0)
        self.chap_overview.click_on_sub_section_on_toc(fig_title)
        draft_status = self.chap_overview.get_sub_section_indicator(fig_title)
        draft_fm_chap_status = self.chap_overview.get_chapter_status_toc()
        alt_text = self.chap_overview.check_fig_showing_get_alt_text()
        above_text = self.chap_overview.get_fig_above_text()
        below_text = self.chap_overview.get_fig_below_text()
        fig_title_text = self.chap_overview.get_fig_title_text()
        self.chap_overview.click_active_fig()
        edit_fig_name = self.chap_overview.get_edit_heading_text()
        self.chap_overview.click_edit_page_button(SAVE_FINAL)
        final_msg = self.viewprojectpage.get_alert_message()
        time.sleep(1.0)
        final_status = self.chap_overview.get_sub_section_indicator(fig_title)
        final_fm_chap_status = self.chap_overview.get_chapter_status_toc()

        Baseclass.assert_equals("Valid Ordinal", validate_text)
        # Baseclass.assert_true(result)
        # assert "JPG_Valid.jpeg" in fig_name                               # this feature is changed
        Baseclass.assert_equals(SUCCESS, draft_msg)
        Baseclass.assert_equals("Red", draft_status)
        Baseclass.assert_equals(alt_text, fig_alt_text)
        Baseclass.assert_equals(above_text, "Fig Above text")
        Baseclass.assert_equals(below_text, "Fig Below text")
        Baseclass.assert_equals(
            fig_title_text, "FIGURE " + section_number + " " + fig_title
        )
        assert fig_title in edit_fig_name
        Baseclass.assert_equals(SUCCESS, final_msg)
        Baseclass.assert_equals("Green", final_status)
        Baseclass.assert_equals("Codes Review", draft_fm_chap_status)
        Baseclass.assert_equals("Codes Greenlight", final_fm_chap_status)

    @allure.feature("Figure")
    @allure.title("Verify cancel edit figure")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(
        depends=["test_verify_add_figure_at_section"], scope="class"
    )
    @pytest.mark.parametrize(
        "fig_name", ["Automation Section Figure", "Automation Sub Section Figure"]
    )
    def test_verify_cancel_edit_figure(self, fig_name):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 16 AUTOMATION TEST")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.chap_overview.click_on_section_on_toc("SECTION 1601 SECTION DATA")
        time.sleep(1.0)
        self.chap_overview.click_on_sub_section_on_toc(fig_name)
        act_alt_text = self.chap_overview.check_fig_showing_get_alt_text()
        act_fig_title_text = self.chap_overview.get_fig_title_text()
        self.chap_overview.click_active_fig()
        self.chap_overview.enter_text_in_textbox(FIG_TITLE, "Edit")
        self.chap_overview.enter_text_in_textbox(FIG_ALT, "Edit alt")
        self.chap_overview.click_edit_page_button(CANCEL)
        self.chap_overview.click_on_alert_button(YES_PROCEED)
        time.sleep(1.0)
        alt_text = self.chap_overview.check_fig_showing_get_alt_text()
        fig_title_text = self.chap_overview.get_fig_title_text()
        Baseclass.assert_equals(act_alt_text, alt_text)
        Baseclass.assert_equals(act_fig_title_text, fig_title_text)

    @allure.feature("Figure")
    @allure.title("Verify Delete figure at section")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(
        depends=["test_verify_add_figure_at_section"], scope="class"
    )
    @pytest.mark.parametrize(
        "fig_name", ["Automation Section Figure", "Automation Sub Section Figure"]
    )
    def test_verify_delete_figure_at_section(self, fig_name):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 16 AUTOMATION TEST")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.chap_overview.click_on_section_on_toc("SECTION 1601 SECTION DATA")
        time.sleep(1.0)
        self.chap_overview.click_on_sub_section_on_toc(fig_name)
        self.chap_overview.click_active_fig()
        self.chap_overview.click_edit_page_button(DELETE)
        time.sleep(1.0)
        self.chap_overview.click_relocate_alt_button(DELETE)
        msg = self.viewprojectpage.get_alert_message()
        self.chap_overview.click_on_section_on_toc("SECTION 1601 SECTION DATA")
        result = self.chap_overview.check_subsection_deleted(fig_name)
        Baseclass.assert_equals(SUCCESS, msg)
        Baseclass.assert_true(result)

    @allure.feature("Sub-Section")
    @allure.title("Verify Delete sub-section")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(depends=["test_verify_add_new_sub_section"], scope="class")
    def test_verify_delete_new_sub_section(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 16 AUTOMATION TEST")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.chap_overview.click_on_section_on_toc("SECTION 1601 SECTION DATA")
        time.sleep(1.0)
        self.chap_overview.click_on_sub_section_on_toc("1601.1 Sub Section Data")
        self.chap_overview.click_on_active_content()
        self.chap_overview.click_edit_page_button(DELETE_SECTION)
        time.sleep(1.0)
        self.chap_overview.click_on_delete_checkbox()
        self.chap_overview.click_relocate_alt_button(DELETE)
        alt_msg = self.viewprojectpage.get_alert_message()
        result = self.chap_overview.check_subsection_deleted("1601.1 Sub Section Data")
        Baseclass.assert_equals(SUCCESS, alt_msg)
        Baseclass.assert_true(result)

    @allure.feature("Section")
    @allure.title("Verify Delete section")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(depends=["test_verify_add_new_section"], scope="class")
    def test_verify_delete_new_section(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 16 AUTOMATION TEST")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        time.sleep(1.0)
        self.chap_overview.click_on_section_on_toc("SECTION 1601 SECTION DATA")
        self.chap_overview.click_on_active_content()
        self.chap_overview.click_edit_page_button(DELETE_SECTION)
        time.sleep(1.0)
        self.chap_overview.click_on_delete_checkbox()
        self.chap_overview.click_relocate_alt_button(DELETE)
        alt_msg = self.viewprojectpage.get_alert_message()
        result = self.chap_overview.check_section_deleted("SECTION 1601 SECTION DATA")
        Baseclass.assert_equals(SUCCESS, alt_msg)
        Baseclass.assert_true(result)

    @allure.feature("Chapter")
    @allure.title("Verify Delete chapter")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(depends=["test_verify_add_new_chapter"], scope="class")
    def test_verify_delete_new_chapter(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 16 AUTOMATION TEST")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        time.sleep(2)
        self.chap_overview.click_on_chapter()
        self.chap_overview.click_edit_page_button(DELETE_CHAPTER)
        self.chap_overview.click_on_delete_checkbox()
        self.chap_overview.click_relocate_alt_button(DELETE)
        alt_msg = self.viewprojectpage.get_alert_message()
        result = self.viewprojectpage.check_chapter_deleted(
            "CHAPTER 16 AUTOMATION TEST"
        )
        Baseclass.assert_equals(SUCCESS, alt_msg)
        Baseclass.assert_true(result)

    @allure.feature("Section")
    @allure.title("Verify Open Section content")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_open_section_content(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 4 VENTILATION")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.chap_overview.click_on_section_on_toc("SECTION 401 GENERAL")
        active_section = self.chap_overview.get_active_heading_name()
        assert "SECTION 401 GENERAL" in active_section

    @allure.feature("Section")
    @allure.title("Verify Cancel Edited Section content")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_cancel_edit_section(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 4 VENTILATION")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.chap_overview.click_on_section_on_toc("SECTION 401 GENERAL")
        act_section_name = self.chap_overview.get_active_heading_name()
        self.chap_overview.click_on_active_content()
        self.chap_overview.enter_text_in_textbox(SECTION_TITLE, " UPDATE")
        edited_text = self.chap_overview.get_edit_heading_text()
        self.chap_overview.click_edit_page_button(CANCEL)
        self.chap_overview.click_on_alert_button(YES_PROCEED)
        heading = self.chap_overview.get_active_heading_name()
        Baseclass.assert_equals(act_section_name, heading)
        assert "UPDATE" in edited_text

    @allure.feature("Section")
    @allure.title("Verify Edit Section Title")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_verify_edit_section_title(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 4 VENTILATION")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        # Save Draft
        time.sleep(1.0)
        self.chap_overview.click_on_section_on_toc("SECTION 401 GENERAL")
        self.chap_overview.click_on_active_content()
        self.chap_overview.edit_contant(SECTION_TITLE, "TEST")
        time.sleep(1.0)
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        alert_draft = self.viewprojectpage.get_alert_message()
        Baseclass.assert_equals(SUCCESS, alert_draft)
        self.baseclass.wait_loadder_dissappried()
        edited_title = self.chap_overview.get_active_heading_name()
        draft_indicator = self.chap_overview.get_section_indicator(edited_title)

        # Save Final
        self.chap_overview.click_on_active_content()
        current_breadcum = self.viewprojectpage.get_current_breadcum()
        self.chap_overview.edit_contant(SECTION_TITLE, "FINAL")
        time.sleep(1.0)
        self.chap_overview.click_edit_page_button(SAVE_FINAL)
        alert_final = self.viewprojectpage.get_alert_message()
        Baseclass.assert_equals(SUCCESS, alert_final)
        self.baseclass.wait_loadder_dissappried()
        final_title = self.chap_overview.get_active_heading_name()
        final_indicator = self.chap_overview.get_section_indicator(final_title)

        Baseclass.assert_equals("SECTION 401 GENERAL TEST", current_breadcum)
        Baseclass.assert_equals("SECTION 401 GENERAL TEST", edited_title)
        Baseclass.assert_equals("Red", draft_indicator)

        Baseclass.assert_equals("SECTION 401 GENERAL TEST FINAL", final_title)
        Baseclass.assert_equals("Green", final_indicator)

    @allure.feature("Sub-Section")
    @allure.title("Verify Open Sub-Section content")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_open_sub_section_content(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 4 VENTILATION")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.chap_overview.click_on_section_on_toc("SECTION 401 GENERAL")
        time.sleep(1.0)
        self.chap_overview.click_on_sub_section_on_toc("401.1 Scope.")
        active_section = self.chap_overview.get_active_heading_name()
        assert "401.1 Scope." in active_section

    @allure.feature("Sub-Section")
    @allure.title("Verify Cancel Edited Sub-Section content")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_cancel_edit_subsection(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 4 VENTILATION")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.chap_overview.click_on_section_on_toc("SECTION 401 GENERAL")
        time.sleep(1.0)
        self.chap_overview.click_on_sub_section_on_toc("401.1 Scope.")
        act_section_name = self.chap_overview.get_active_heading_name()
        self.chap_overview.click_on_active_content()
        self.chap_overview.enter_text_in_textbox(SECTION_TITLE, " Update")
        edited_text = self.chap_overview.get_edit_heading_text()
        self.chap_overview.click_edit_page_button(CANCEL)
        self.chap_overview.click_on_alert_button(YES_PROCEED)
        heading = self.chap_overview.get_active_heading_name()
        Baseclass.assert_equals(act_section_name, heading)
        assert "Update" in edited_text

    @allure.feature("Sub-Section")
    @allure.title("Verify Edit Sub-Section Title and Content")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_verify_edit_subsection_title_content(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("CHAPTER 4 VENTILATION")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        # Save Draft
        time.sleep(1.0)
        self.chap_overview.click_on_section_on_toc("SECTION 401 GENERAL")
        time.sleep(1.0)
        self.chap_overview.click_on_sub_section_on_toc("401.1 Scope.")
        self.chap_overview.click_on_active_content()
        self.chap_overview.edit_contant(SECTION_TITLE, "Test")
        self.chap_overview.edit_contant(SECTION_CONTENT, "Test content")
        time.sleep(1.0)
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        alert_draft = self.viewprojectpage.get_alert_message()
        Baseclass.assert_equals(SUCCESS, alert_draft)
        self.baseclass.wait_loadder_dissappried()
        edited_title = self.chap_overview.get_active_heading_name()
        edited_content = self.chap_overview.get_active_section_text()
        time.sleep(1.0)
        draft_indicator = self.chap_overview.get_sub_section_indicator(edited_title)

        # Save Final
        self.chap_overview.click_on_active_content()
        current_breadcum = self.viewprojectpage.get_current_breadcum()
        self.chap_overview.edit_contant(SECTION_TITLE, "Final")
        self.chap_overview.edit_contant(SECTION_CONTENT, "Final")
        time.sleep(1.0)
        self.chap_overview.click_edit_page_button(SAVE_FINAL)
        alert_final = self.viewprojectpage.get_alert_message()
        Baseclass.assert_equals(SUCCESS, alert_final)
        self.baseclass.wait_loadder_dissappried()
        final_title = self.chap_overview.get_active_heading_name()
        final_content = self.chap_overview.get_active_section_text()
        final_indicator = self.chap_overview.get_sub_section_indicator(final_title)

        Baseclass.assert_equals("401.1 Scope. Test", current_breadcum)
        Baseclass.assert_equals("401.1 Scope. Test", edited_title)
        assert "Test" in edited_content
        Baseclass.assert_equals("Red", draft_indicator)

        Baseclass.assert_equals("401.1 Scope. Test Final", final_title)
        assert "Final" in final_content
        Baseclass.assert_equals("Green", final_indicator)
