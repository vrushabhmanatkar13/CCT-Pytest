import time
import pytest
import allure
from test_cases import conftest
from test_cases.test_base import SUCCESS, YES_PROCEED, Test_Base
from test_cases.test_chapter_overview_page import (
    CANCEL,
    CONTENT,
    FIG_ALT,
    FIG_NOTE_ABOVE,
    FIG_NOTE_BELOW,
    FIGURE,
    NEW_CODE_ELEMENT,
    OPEN_CHAPTER,
    SAVE_DRAFT,
    SAVE_FINAL,
    SECTION,
    TITLE,
)
from test_cases.test_dashboard_page import DELETE
from test_cases.test_view_project_page import VIEW_PROJECT
from uitility.baseclass import Baseclass

FM_CHAP_TITLE = conftest.json_obj["Content Edit"]["fm_chapter_title"]
FM_CHAP_CONTENT = conftest.json_obj["Content Edit"]["fm_chapter_content"]
NEW_FM_CHAPTER = conftest.json_obj["Footer_model"]["new_fm_chapter"]


@pytest.mark.sixth
@allure.epic("Fm Chapter Overview and Content")
@allure.tag("Fm Chapter Overview/Content page")
class Test_Fm_Chapter_Overview(Test_Base):

    @allure.feature("Frontmatter")
    @allure.title("Verify Cancel edit Fm Chapter")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_cancel_edit_fm_chapter(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("PREFACE")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        act_chap_name = self.chap_overview.get_chapter_heading()
        self.chap_overview.click_on_chapter()
        self.chap_overview.enter_text_in_textbox(FM_CHAP_TITLE, " UPDATE")
        self.chap_overview.enter_text_in_textbox(FM_CHAP_CONTENT, " update")
        self.chap_overview.click_edit_page_button(CANCEL)
        self.chap_overview.click_on_alert_button(YES_PROCEED)
        chap_name = self.chap_overview.get_chapter_heading()
        chap_content = self.chap_overview.get_fm_chapter_content_text()
        Baseclass.assert_equals(act_chap_name, chap_name)
        assert "update" not in chap_content

    @allure.feature("Frontmatter")
    @allure.title("Verify Edit Fm Chapter Title and Content")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_verify_edit_fm_chapter_title_content(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("PREFACE")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        # Save Draft

        self.chap_overview.click_on_chapter()
        time.sleep(1)
        self.chap_overview.edit_contant(FM_CHAP_TITLE, "TEST")
        self.chap_overview.edit_contant(FM_CHAP_CONTENT, "Test")
        time.sleep(1)
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        draft_msg = self.viewprojectpage.get_alert_message()
        self.baseclass.wait_loadder_dissappried()

        draft_chapter = self.chap_overview.get_chapter_heading()
        draft_content = self.chap_overview.get_fm_chapter_content_text()

        # Save final
        self.chap_overview.click_on_chapter()
        self.chap_overview.edit_contant(FM_CHAP_TITLE, "FINAL")
        self.chap_overview.edit_contant(FM_CHAP_CONTENT, "Final")
        time.sleep(1)
        self.chap_overview.click_edit_page_button(SAVE_FINAL)
        final_msg = self.viewprojectpage.get_alert_message()
        self.baseclass.wait_loadder_dissappried()
        final_chapter = self.chap_overview.get_chapter_heading()
        final_content = self.chap_overview.get_fm_chapter_content_text()

        Baseclass.assert_equals(SUCCESS, draft_msg)
        Baseclass.assert_equals("PREFACE TEST", draft_chapter)
        assert "Test" in draft_content

        Baseclass.assert_equals(SUCCESS, final_msg)
        Baseclass.assert_equals("PREFACE TEST FINAL", final_chapter)
        assert "Final" in final_content

    @allure.feature("Frontmatter")
    @allure.title("Verify Cancel Edit Fm Section")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_cancel_edit_fm_section(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("PREFACE")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.chap_overview.click_on_section_on_toc("Section Introduction")
        act_section_name = self.chap_overview.get_active_fm_heading_name()
        self.chap_overview.click_on_active_content()
        self.chap_overview.enter_text_in_textbox(TITLE, " UPDATE")
        self.chap_overview.enter_text_in_textbox(CONTENT, " update")
        self.chap_overview.click_edit_page_button(CANCEL)
        self.chap_overview.click_on_alert_button(YES_PROCEED)
        section_title = self.chap_overview.get_active_fm_heading_name()
        section_content = self.chap_overview.get_active_fm_section_text()
        Baseclass.assert_equals(act_section_name, section_title)
        assert "update" not in section_content

    @allure.feature("Frontmatter")
    @allure.title("Verify Edit Fm Section Title and Content")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_verify_edit_fm_section_title_content(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("PREFACE")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        # Save Draft

        self.chap_overview.click_on_section_on_toc("Section Introduction")
        self.chap_overview.click_on_active_content()
        time.sleep(1)
        self.chap_overview.edit_contant(TITLE, "TEST")
        self.chap_overview.edit_contant(CONTENT, "Test")
        time.sleep(1)
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        draft_msg = self.viewprojectpage.get_alert_message()
        self.baseclass.wait_loadder_dissappried()
        draft_section = self.chap_overview.get_active_fm_heading_name()
        draft_content = self.chap_overview.get_active_fm_section_text()
        draft_indicator = self.chap_overview.get_section_indicator(draft_section)

        # Save final
        self.chap_overview.click_on_active_content()
        self.chap_overview.edit_contant(TITLE, "FINAL")
        self.chap_overview.edit_contant(CONTENT, "Final")
        time.sleep(1)
        self.chap_overview.click_edit_page_button(SAVE_FINAL)
        final_msg = self.viewprojectpage.get_alert_message()
        self.baseclass.wait_loadder_dissappried()
        final_section = self.chap_overview.get_active_fm_heading_name()
        final_content = self.chap_overview.get_active_fm_section_text()
        final_indicator = self.chap_overview.get_section_indicator(final_section)

        Baseclass.assert_equals(SUCCESS, draft_msg)
        Baseclass.assert_equals("Introduction TEST", draft_section)
        assert "Test" in draft_content
        Baseclass.assert_equals("Red", draft_indicator)

        Baseclass.assert_equals(SUCCESS, final_msg)
        Baseclass.assert_equals("Introduction TEST FINAL", final_section)
        assert "Final" in final_content
        Baseclass.assert_equals("Green", final_indicator)

    @allure.feature("Frontmatter")
    @allure.title("Verify Add new Fm Chapter")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency()
    def test_verify_add_new_fm_chapter(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        time.sleep(1)
        self.header_footer.click_on_add_new()
        time.sleep(1)
        self.header_footer.click_on_model_list(NEW_FM_CHAPTER)
        self.chap_overview.enter_text_in_textbox(FM_CHAP_TITLE, "AUTOMATION FM")
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        draft_msg = self.viewprojectpage.get_alert_message()
        fm_chapters = self.viewprojectpage.get_all_fm_chapter_name()
        self.viewprojectpage.click_on_chapter("AUTOMATION FM")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        time.sleep(1)
        self.chap_overview.click_on_chapter()
        self.chap_overview.enter_text_in_textbox(FM_CHAP_TITLE, " FINAL")
        self.chap_overview.click_edit_page_button(SAVE_FINAL)
        final_msg = self.viewprojectpage.get_alert_message()
        fm_chapters_name = self.chap_overview.get_chapter_heading()
        self.viewprojectpage.click_pervios_breadcum()
        time.sleep(1)
        fm_chapters_final = self.viewprojectpage.get_all_fm_chapter_name()

        Baseclass.assert_equals(draft_msg, SUCCESS)
        assert "AUTOMATION FM" in fm_chapters
        Baseclass.assert_equals(final_msg, SUCCESS)
        Baseclass.assert_equals("AUTOMATION FM FINAL", fm_chapters_name)
        assert "AUTOMATION FM FINAL" in fm_chapters_final

    @allure.feature("Frontmatter")
    @allure.title("Verify Add new Fm Section")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(depends=["test_verify_add_new_fm_chapter"], scope="class")
    def test_verify_add_new_fm_section(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("AUTOMATION FM FINAL")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.header_footer.click_on_add_new()
        time.sleep(1)
        self.header_footer.click_on_model_list(NEW_CODE_ELEMENT)

        self.header_footer.click_on_code_element_button(SECTION)
        self.chap_overview.enter_text_in_textbox(TITLE, "Automation Fm Section")
        self.chap_overview.enter_text_in_textbox(
            CONTENT, "Automation Fm Section Content"
        )
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        draft_msg = self.viewprojectpage.get_alert_message()
        fm_section = self.chap_overview.get_active_fm_heading_name()
        fm_section_content = self.chap_overview.get_active_fm_section_text()
        draft_status = self.chap_overview.get_section_indicator(fm_section)
        fm_chap_status_draft = self.chap_overview.get_chapter_status_toc()
        self.chap_overview.click_on_active_content()
        self.chap_overview.click_edit_page_button(SAVE_FINAL)
        final_msg = self.viewprojectpage.get_alert_message()
        final_status = self.chap_overview.get_section_indicator(fm_section)
        fm_chap_status_final = self.chap_overview.get_chapter_status_toc()

        Baseclass.assert_equals(SUCCESS, draft_msg)
        Baseclass.assert_equals("Automation Fm Section", fm_section)
        assert "Automation Fm Section Content" in fm_section_content
        Baseclass.assert_equals("Red", draft_status)
        Baseclass.assert_equals("Codes Review", fm_chap_status_draft)
        Baseclass.assert_equals(SUCCESS, final_msg)
        Baseclass.assert_equals("Green", final_status)
        Baseclass.assert_equals("Codes Greenlight", fm_chap_status_final)

    @allure.feature("Frontmatter")
    @allure.title("Verify Add new Fm Figure")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(depends=["test_verify_add_new_fm_chapter"], scope="class")
    def test_verify_add_new_fm_figure(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("AUTOMATION FM FINAL")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.header_footer.click_on_add_new()
        time.sleep(1)
        self.header_footer.click_on_model_list(NEW_CODE_ELEMENT)
        self.header_footer.click_on_code_element_button(FIGURE)
        result = self.chap_overview.upload_figure("Test Data/JPG_Valid.jpeg")
        # fig_name = self.chap_overview.get_fig_file_name()                          # feature changed
        self.chap_overview.enter_text_in_textbox(FIG_NOTE_ABOVE, "Fig Above text")
        self.chap_overview.enter_text_in_textbox(FIG_NOTE_BELOW, "Fig Below text")
        self.chap_overview.enter_text_in_title_textbox("Automation Fm Figure")
        self.chap_overview.enter_text_in_textbox(FIG_ALT, "Fig Alt text")
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        draft_msg = self.viewprojectpage.get_alert_message()
        time.sleep(1)
        draft_status = self.chap_overview.get_section_indicator("Automation Fm Figure")
        draft_fm_chap_status = self.chap_overview.get_chapter_status_toc()
        alt_text = self.chap_overview.check_fig_showing_get_alt_text()
        above_text = self.chap_overview.get_fig_above_text()
        below_text = self.chap_overview.get_fig_below_text()
        fig_title = self.chap_overview.get_fig_title_text()
        self.chap_overview.click_active_fig()
        edit_fig_name = self.chap_overview.get_edit_heading_text()
        self.chap_overview.click_edit_page_button(SAVE_FINAL)
        final_msg = self.viewprojectpage.get_alert_message()
        time.sleep(1)
        final_status = self.chap_overview.get_section_indicator("Automation Fm Figure")
        final_fm_chap_status = self.chap_overview.get_chapter_status_toc()
        # Baseclass.assert_true(result)
        # assert "JPG_Valid.jpeg" in fig_name                                     # feature changed
        Baseclass.assert_equals(SUCCESS, draft_msg)
        Baseclass.assert_equals("Red", draft_status)
        Baseclass.assert_equals(alt_text, "Fig Alt text")
        Baseclass.assert_equals(above_text, "Fig Above text")
        Baseclass.assert_equals(below_text, "Fig Below text")
        Baseclass.assert_equals(fig_title, "Automation Fm Figure")
        assert "Automation Fm Figure" in edit_fig_name
        Baseclass.assert_equals(SUCCESS, final_msg)
        Baseclass.assert_equals("Green", final_status)
        Baseclass.assert_equals(draft_fm_chap_status, "Codes Review")
        Baseclass.assert_equals(final_fm_chap_status, "Codes Greenlight")

    @allure.feature("Frontmatter")
    @allure.title("Verify Cancel edit Fm Figure")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(depends=["test_verify_add_new_fm_figure"], scope="class")
    def test_verify_cancel_edit_fm_figure(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("AUTOMATION FM FINAL")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.chap_overview.click_on_section_on_toc("Automation Fm Figure")
        act_alt_text = self.chap_overview.check_fig_showing_get_alt_text()
        act_fig_title = self.chap_overview.get_fig_title_text()
        self.chap_overview.click_active_fig()
        self.chap_overview.enter_text_in_title_textbox("Edit")
        self.chap_overview.enter_text_in_textbox(FIG_ALT, "Edit alt")
        self.chap_overview.click_edit_page_button(CANCEL)
        self.chap_overview.click_on_alert_button(YES_PROCEED)
        time.sleep(2)
        alt_text = self.chap_overview.check_fig_showing_get_alt_text()
        fig_title = self.chap_overview.get_fig_title_text()
        Baseclass.assert_equals(act_alt_text, alt_text)
        Baseclass.assert_equals(act_fig_title, fig_title)

    @allure.feature("Frontmatter")
    @allure.title("Verify add Fm section with no title associated")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.dependency(
        depends=["test_verify_add_new_fm_section", "test_verify_add_new_fm_figure"],
        scope="class",
    )
    @pytest.mark.parametrize(
        ["Section", "No_title_name"],
        [
            ("Automation Fm Section", "SECTION_CONTENT"),
            ("Automation Fm Figure", "FIGURE_CONTENT"),
        ],
    )
    def test_verify_add_fm_section_with_no_title_associated(
        self, Section, No_title_name
    ):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("AUTOMATION FM FINAL")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.chap_overview.click_on_section_on_toc(Section)
        self.chap_overview.click_on_active_content()
        self.chap_overview.click_fm_no_title_checkbox()
        title_field = self.chap_overview.get_fm_title_field()
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        self.viewprojectpage.get_alert_message()
        self.baseclass.wait_loadder_dissappried()
        section_name = self.chap_overview.get_no_section_title_toc(No_title_name)
        fm_section = self.chap_overview.get_fm_hidden_title_name(No_title_name)
        Baseclass.assert_true(title_field)
        assert fm_section in section_name
        self.chap_overview.click_on_section_on_toc(No_title_name)
        self.chap_overview.click_fm_no_title_checkbox()
        self.chap_overview.enter_text_in_textbox(TITLE, Section)
        self.chap_overview.click_edit_page_button(SAVE_DRAFT)
        draft_msg = self.viewprojectpage.get_alert_message()
        self.baseclass.wait_loadder_dissappried()
        Baseclass.assert_equals(SUCCESS, draft_msg)

    @allure.feature("Frontmatter")
    @allure.title("Verify Delete Fm Figure")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(depends=["test_verify_add_new_fm_figure"], scope="class")
    def test_verify_delete_fm_figure(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("AUTOMATION FM FINAL")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        self.chap_overview.click_on_section_on_toc("Automation Fm Figure")
        self.chap_overview.click_active_fig()
        self.chap_overview.click_edit_page_button(DELETE)
        time.sleep(1)
        self.chap_overview.click_relocate_alt_button(DELETE)
        fig_name_result = self.chap_overview.check_section_deleted(
            "Automation Fm Figure"
        )
        fig_text_result = self.chap_overview.check_figure_text_strick_through()
        Baseclass.assert_true(fig_name_result)
        Baseclass.assert_true(fig_text_result)

    @allure.feature("Frontmatter")
    @allure.title("Verify Delete Fm Section")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(depends=["test_verify_add_new_fm_section"], scope="class")
    def test_verify_delete_fm_section(self):
        self.dashboardpage.click_project_name("2021 International Mechanical Code")
        self.dashboardpage.click_dashboard_button(VIEW_PROJECT)
        self.viewprojectpage.click_on_chapter("AUTOMATION FM FINAL")
        self.chap_overview.click_on_button(OPEN_CHAPTER)
        time.sleep(1)
        self.chap_overview.click_on_section_on_toc("Automation Fm Section")
        self.chap_overview.click_on_active_content()
        self.chap_overview.click_edit_page_button(DELETE)
        time.sleep(1)
        self.chap_overview.click_relocate_alt_button(DELETE)
        section_name_result = self.chap_overview.check_section_deleted(
            "Automation Fm Section"
        )
        section_text_result = self.chap_overview.check_fm_section_text_strick_through()
        Baseclass.assert_true(section_name_result)
        Baseclass.assert_true(section_text_result)
