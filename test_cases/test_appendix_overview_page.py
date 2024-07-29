import time
import pytest
import allure

from test_cases import conftest
from test_cases.test_base import SUCCESS, YES_PROCEED, Test_Base
from test_cases.test_chapter_overview_page import (
    CANCEL,
    FIG_ALT,
    FIG_NOTE_ABOVE,
    FIG_NOTE_BELOW,
    FIG_TITLE,
    FIGURE,
    NEW_CODE_ELEMENT,
    OPEN_CHAPTER,
    RELOCATE_FIG,
    RELOCATE_SECTION,
    SAVE_DRAFT,
    SAVE_FINAL,
    SECTION,
    SECTION_CONTENT,
    SECTION_ORDINAL,
    SECTION_TITLE,
    SET_SECTION_ORDINAL,
    VALIDATE_LOCATION,
)
from test_cases.test_dashboard_page import DELETE
from test_cases.test_view_project_page import VIEW_PROJECT
from uitility.baseclass import Baseclass

APPENDIX_TITLE = conftest.json_obj["Content Edit"]["appendix_title"]
APPENDIX_CONTENT = conftest.json_obj["Content Edit"]["appendix_content"]
APPENDIX_DELETE = conftest.json_obj["Content Edit"]["delete_appendix"]
SET_APPENDIX_ORDINAL = conftest.json_obj["Content Edit"]["set_appendix_ordinal"]
APPENDIX_ORDINAL = conftest.json_obj["Content Edit"]["appendix_ordinal"]

RELOCATE_APPENDIX = conftest.json_obj["Relocate alert"]["relocate_appendix"]

NEW_APPENDIX = conftest.json_obj["Footer_model"]["new_appendix"]


@pytest.mark.seventh
@allure.epic("Appendix Overview and Content")
@allure.tag("Appendix Overview/Content page")
class Test_Appendix_Overview(Test_Base):

    @allure.feature("Appendix")
    @allure.title("Verify Open Appendix content")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_verify_open_Appendix_content(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)

        status_overview_page = self.viewprojectpage.get_chapter_status(
            "APPENDIX B RECOMMENDED PERMIT FEE SCHEDULE"
        )
        self.viewprojectpage.click_on_chapter(
            "APPENDIX B RECOMMENDED PERMIT FEE SCHEDULE"
        )
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        chap_status = self.chap_overview.get_chapter_status_toc()
        heading = self.chap_overview.get_chapter_heading()
        Baseclass.assert_equals(status_overview_page, chap_status)
        assert "APPENDIX B RECOMMENDED PERMIT FEE SCHEDULE" in heading

    @allure.feature("Appendix")
    @allure.title("Verify Cancel Edited Appendix content")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_cancel_edit_chapter(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter(
            "APPENDIX B RECOMMENDED PERMIT FEE SCHEDULE"
        )
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        act_chap_name = self.chap_overview.get_chapter_heading()
        self.chap_overview.click_on_chapter()
        self.chap_overview.enter_text_in_textbox(APPENDIX_TITLE, " UPDATE")
        self.chap_overview.enter_text_in_textbox(APPENDIX_CONTENT, " update")
        edited_text = self.chap_overview.get_edit_heading_text()
        time.sleep(1)
        self.chap_overview.click_edit_page_button(CANCEL)
        self.chap_overview.click_on_alert_button(YES_PROCEED)
        heading = self.chap_overview.get_chapter_heading()
        content = self.appen_overview.get_appendix_content_text()
        Baseclass.assert_equals(act_chap_name, heading)
        assert "UPDATE" in edited_text
        assert "update" not in content

    @allure.feature("Appendix")
    @allure.title("Verify Edit Appendix Title and Content")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_verify_edit_appendix_title_content(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter(
            "APPENDIX B RECOMMENDED PERMIT FEE SCHEDULE"
        )
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        # Save Draft
        time.sleep(1)
        self.chap_overview.click_on_chapter()
        self.chap_overview.edit_contant(APPENDIX_TITLE, "TEST")
        self.chap_overview.edit_contant(APPENDIX_CONTENT, "Test content")
        time.sleep(1)
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        alert_draft = self.viewprojectpage.get_alert_message()
        Baseclass.assert_equals(SUCCESS, alert_draft)
        self.baseclass.wait_loadder_dissappried()
        edited_title = self.chap_overview.get_chapter_heading()
        edited_content = self.appen_overview.get_appendix_content_text()
        edited_appen_toc = self.chap_overview.get_chapter_name_toc()
        current_breadcum = self.viewprojectpage.get_current_breadcum()
        # Save Final
        self.chap_overview.click_on_chapter()
        self.chap_overview.edit_contant(APPENDIX_TITLE, "FINAL")
        self.chap_overview.edit_contant(APPENDIX_CONTENT, "final")
        time.sleep(1)
        self.chap_overview.click_edit_page_button(SAVE_FINAL)
        alert_final = self.viewprojectpage.get_alert_message()
        Baseclass.assert_equals(SUCCESS, alert_final)
        self.baseclass.wait_loadder_dissappried()
        final_title = self.chap_overview.get_chapter_heading()
        final_content = self.appen_overview.get_appendix_content_text()
        final_appen_toc = self.chap_overview.get_chapter_name_toc()
        final_breadcum = self.viewprojectpage.get_current_breadcum()

        Baseclass.assert_equals(
            "APPENDIX B RECOMMENDED PERMIT FEE SCHEDULE TEST", edited_title
        )
        assert "Test content" in edited_content
        assert "TEST" in edited_appen_toc
        Baseclass.assert_equals(
            "APPENDIX B RECOMMENDED PERMIT FEE SCHEDULE TEST", current_breadcum
        )

        Baseclass.assert_equals(
            "APPENDIX B RECOMMENDED PERMIT FEE SCHEDULE TEST FINAL", final_title
        )
        assert "Test content final" in final_content
        assert "FINAL" in final_appen_toc
        Baseclass.assert_equals(
            "APPENDIX B RECOMMENDED PERMIT FEE SCHEDULE TEST FINAL", final_breadcum
        )

    @allure.feature("Appendix")
    @allure.title("Verify Add new appendix")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency()
    def test_verify_add_new_appendix(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        appendix_ordinal = self.appen_overview.get_last_appendix_ordinal()
        self.header_footer.click_on_add_new()
        time.sleep(1)
        self.header_footer.click_on_model_list(NEW_APPENDIX)
        self.chap_overview.click_edit_page_button(SET_APPENDIX_ORDINAL)
        time.sleep(1)
        self.chap_overview.enter_new_ordinal_text(appendix_ordinal)
        self.chap_overview.click_relocate_alt_button(VALIDATE_LOCATION)
        validate_text = self.chap_overview.get_validate_message()
        self.chap_overview.click_relocate_alt_button(RELOCATE_APPENDIX)
        appendix_ordinal = self.chap_overview.get_filled_text(APPENDIX_ORDINAL)
        self.chap_overview.enter_text_in_textbox(APPENDIX_TITLE, "AUTOMATION APPENDIX")
        self.chap_overview.enter_text_in_textbox(
            APPENDIX_CONTENT, "Automation appendix content"
        )
        time.sleep(1)
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        msg = self.viewprojectpage.get_alert_message()
        appen_title = self.chap_overview.get_chapter_heading()
        appen_content = self.appen_overview.get_appendix_content_text()
        currnet_breadcum = self.viewprojectpage.get_current_breadcum()
        self.viewprojectpage.click_pervios_breadcum()
        title = " ".join(["APPENDIX", appendix_ordinal, "AUTOMATION APPENDIX"])
        appen_status = self.viewprojectpage.get_chapter_status(title)

        Baseclass.assert_equals("Valid Ordinal", validate_text)
        Baseclass.assert_equals(SUCCESS, msg)
        Baseclass.assert_equals(title, appen_title)
        assert "Automation appendix content" in appen_content
        Baseclass.assert_equals(title, currnet_breadcum)
        Baseclass.assert_equals("Codes Greenlight", appen_status)

    @allure.feature("Appendix")
    @allure.title("Verify Add new Appendix section")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(
        depends=["test_verify_add_new_appendix"],
        scope="class",
    )
    def test_verify_add_new_appendix_section(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("AUTOMATION APPENDIX")
        appen_ordinal = self.appen_overview.get_current_appendix_ordinal()

        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.header_footer.click_on_add_new()
        time.sleep(1)
        self.header_footer.click_on_model_list(NEW_CODE_ELEMENT)
        self.header_footer.click_on_code_element_button(SECTION)
        self.chap_overview.click_edit_page_button(SET_SECTION_ORDINAL)
        time.sleep(1)
        self.chap_overview.enter_new_ordinal_text(appen_ordinal + "101")
        self.chap_overview.click_relocate_alt_button(VALIDATE_LOCATION)
        validate_text = self.chap_overview.get_validate_message()
        self.chap_overview.click_relocate_alt_button(RELOCATE_SECTION)
        sec_ordinal = self.chap_overview.get_filled_text(SECTION_ORDINAL)
        self.chap_overview.enter_text_in_textbox(SECTION_TITLE, "AUTOMATION SECTION")
        time.sleep(1)
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        msg = self.viewprojectpage.get_alert_message()
        sec_title = self.chap_overview.get_active_heading_name()
        draft_chap_status = self.chap_overview.get_chapter_status_toc()
        section = " ".join(["SECTION", sec_ordinal, "AUTOMATION SECTION"])
        sec_status = self.chap_overview.get_section_indicator(section)
        self.chap_overview.click_on_active_content()
        time.sleep(1)
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

    @allure.feature("Appendix")
    @allure.title("Verify Add new Appendix sub-section")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(
        depends=["test_verify_add_new_appendix_section"], scope="class"
    )
    def test_verify_add_new_appendix_sub_section(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("AUTOMATION APPENDIX")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        section_number = self.chap_overview.get_section_number("AUTOMATION SECTION")
        self.header_footer.click_on_add_new()
        time.sleep(1)
        self.header_footer.click_on_model_list(NEW_CODE_ELEMENT)
        self.header_footer.click_on_code_element_button(SECTION)
        self.chap_overview.click_edit_page_button(SET_SECTION_ORDINAL)
        time.sleep(1)
        self.chap_overview.enter_new_ordinal_text(section_number + ".1")
        self.chap_overview.click_relocate_alt_button(VALIDATE_LOCATION)
        validate_text = self.chap_overview.get_validate_message()
        self.chap_overview.click_relocate_alt_button(RELOCATE_SECTION)
        subsec_ordinal = self.chap_overview.get_filled_text(SECTION_ORDINAL)
        self.chap_overview.select_section_label("BLANK")
        self.chap_overview.enter_text_in_textbox(
            SECTION_TITLE, "Automation sub section"
        )
        self.chap_overview.enter_text_in_textbox(
            SECTION_CONTENT, "Test data from automation for appendix"
        )
        time.sleep(1)
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        msg = self.viewprojectpage.get_alert_message()
        draft_chap_status = self.chap_overview.get_chapter_status_toc()

        subsec_title = self.chap_overview.get_active_heading_name()
        subsection = " ".join([subsec_ordinal, "Automation sub section"])
        self.chap_overview.click_on_section_on_toc("AUTOMATION SECTION")
        time.sleep(1)
        self.chap_overview.click_on_sub_section_on_toc(subsection)
        subsec_status = self.chap_overview.get_sub_section_indicator(subsection)
        self.chap_overview.click_on_active_content()
        time.sleep(1)
        currnet_breadcum = self.viewprojectpage.get_current_breadcum()
        self.chap_overview.click_edit_page_button(SAVE_FINAL)
        self.viewprojectpage.get_alert_message()
        time.sleep(1)
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

    @allure.feature("Appendix")
    @allure.title("Verify Add new Figure at Appendix")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(
        name="test_verify_add_figure_at_appendix",
        depends=[
            "test_verify_add_new_appendix_section",
            "test_verify_add_new_appendix_sub_section",
        ],
        scope="class",
    )
    @pytest.mark.parametrize(
        ["section_type", "fig_title", "fig_alt_text"],
        [
            ("Section", "Automation Appendix Section Figure", "Fig Alt section"),
            (
                "Sub-Section",
                "Automation Appendix Sub Section Figure",
                "Fig Alt sub section",
            ),
        ],
    )
    def test_verify_add_figure_at_appendix(self, section_type, fig_title, fig_alt_text):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("AUTOMATION APPENDIX")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        if section_type == "Section":
            section_number = self.chap_overview.get_section_number("AUTOMATION SECTION")
        else:
            self.chap_overview.click_on_section_on_toc("AUTOMATION SECTION")
            time.sleep(1)
            section_number = self.chap_overview.get_sub_section_number(
                "Automation sub section"
            )
        self.header_footer.click_on_add_new()
        time.sleep(1)
        self.header_footer.click_on_model_list(NEW_CODE_ELEMENT)
        self.header_footer.click_on_code_element_button(FIGURE)
        self.chap_overview.click_edit_page_button("Set Figure Ordinal")
        time.sleep(1)
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
        self.chap_overview.click_on_section_on_toc("AUTOMATION SECTION")
        time.sleep(1)
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
        time.sleep(1)
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
        Baseclass.assert_equals(draft_fm_chap_status, "Codes Review")
        Baseclass.assert_equals(final_fm_chap_status, "Codes Greenlight")

    @allure.feature("Appendix")
    @allure.title("Verify cancel edit Appendix figure")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(
        depends=["test_verify_add_figure_at_appendix"], scope="class"
    )
    @pytest.mark.parametrize(
        "fig_name",
        [
            "Automation Appendix Section Figure",
            "Automation Appendix Sub Section Figure",
        ],
    )
    def test_verify_cancel_edit_appendix_figure(self, fig_name):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("AUTOMATION APPENDIX")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        time.sleep(1)
        self.chap_overview.click_on_section_on_toc("AUTOMATION SECTION")
        self.chap_overview.click_on_sub_section_on_toc(fig_name)
        act_alt_text = self.chap_overview.check_fig_showing_get_alt_text()
        act_fig_title_text = self.chap_overview.get_fig_title_text()
        self.chap_overview.click_active_fig()
        self.chap_overview.enter_text_in_textbox(FIG_TITLE, "Edit")
        self.chap_overview.enter_text_in_textbox(FIG_ALT, "Edit alt")
        self.chap_overview.click_edit_page_button(CANCEL)
        self.chap_overview.click_on_alert_button(YES_PROCEED)
        time.sleep(1)
        alt_text = self.chap_overview.check_fig_showing_get_alt_text()
        fig_title_text = self.chap_overview.get_fig_title_text()
        Baseclass.assert_equals(act_alt_text, alt_text)
        Baseclass.assert_equals(act_fig_title_text, fig_title_text)

    @allure.feature("Appendix")
    @allure.title("Verify Delete figure at Appendix")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(
        depends=["test_verify_add_figure_at_appendix"], scope="class"
    )
    @pytest.mark.parametrize(
        "fig_name",
        [
            "Automation Appendix Section Figure",
            "Automation Appendix Sub Section Figure",
        ],
    )
    def test_verify_delete_figure_at_appendix(self, fig_name):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("AUTOMATION APPENDIX")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.chap_overview.click_on_section_on_toc("AUTOMATION SECTION")
        time.sleep(1)
        self.chap_overview.click_on_sub_section_on_toc(fig_name)
        self.chap_overview.click_active_fig()
        self.chap_overview.click_edit_page_button(DELETE)
        time.sleep(1)
        self.chap_overview.click_relocate_alt_button(DELETE)
        msg = self.viewprojectpage.get_alert_message()
        self.chap_overview.click_on_section_on_toc("AUTOMATION SECTION")
        result = self.chap_overview.check_subsection_deleted(fig_name)
        Baseclass.assert_equals(SUCCESS, msg)
        Baseclass.assert_true(result)

    @allure.feature("Appendix")
    @allure.title("Verify Delete Appendix sub-section")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(
        depends=["test_verify_add_new_appendix_sub_section"], scope="class"
    )
    def test_verify_delete_appendix_sub_section(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("AUTOMATION APPENDIX")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.chap_overview.click_on_section_on_toc("AUTOMATION SECTION")
        time.sleep(1)
        self.chap_overview.click_on_sub_section_on_toc("Automation sub section")
        self.chap_overview.click_on_active_content()
        self.chap_overview.click_edit_page_button(DELETE)
        time.sleep(1)
        self.chap_overview.click_on_delete_checkbox()
        self.chap_overview.click_relocate_alt_button(DELETE)
        alt_msg = self.viewprojectpage.get_alert_message()
        result = self.chap_overview.check_subsection_deleted("Automation sub section")
        Baseclass.assert_equals(SUCCESS, alt_msg)
        Baseclass.assert_true(result)

    @allure.feature("Appendix")
    @allure.title("Verify Delete Appendix section")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(
        depends=["test_verify_add_new_appendix_section"], scope="class"
    )
    def test_verify_delete_appendix_section(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("AUTOMATION APPENDIX")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        time.sleep(1)
        self.chap_overview.click_on_section_on_toc("AUTOMATION SECTION")
        self.chap_overview.click_on_active_content()
        self.chap_overview.click_edit_page_button(DELETE)
        time.sleep(1)
        self.chap_overview.click_on_delete_checkbox()
        self.chap_overview.click_relocate_alt_button(DELETE)
        alt_msg = self.viewprojectpage.get_alert_message()
        result = self.chap_overview.check_section_deleted("AUTOMATION SECTION")
        Baseclass.assert_equals(SUCCESS, alt_msg)
        Baseclass.assert_true(result)

    @allure.feature("Appendix")
    @allure.title("Verify Delete Appendix")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(depends=["test_verify_add_new_appendix"], scope="class")
    def test_verify_delete_appendix_chapter(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("AUTOMATION APPENDIX")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        time.sleep(1)
        self.chap_overview.click_on_chapter()
        self.chap_overview.click_edit_page_button(DELETE)
        self.chap_overview.click_on_delete_checkbox()
        self.chap_overview.click_relocate_alt_button(DELETE)
        alt_msg = self.viewprojectpage.get_alert_message()
        result = self.viewprojectpage.check_chapter_deleted("AUTOMATION APPENDIX")
        Baseclass.assert_equals(SUCCESS, alt_msg)
        Baseclass.assert_true(result)
