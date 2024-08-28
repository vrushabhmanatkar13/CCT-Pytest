import test_cases.conftest as conftest


# Login
RESET_PASSWORD_PAGE = conftest.json_obj["Page Titles"]["rest_password"]

# Dashboard

HOME_PAGE = conftest.json_obj["Page Titles"]["home_page"]
SUCCESS = conftest.json_obj["Alert"]["success"]
ERROR = conftest.json_obj["Alert"]["error"]
YES_PROCEED = conftest.json_obj["Alert"]["yes_proceed"]
ALT_CANCEL = conftest.json_obj["Alert"]["cancel"]

VIEW_PROJECT = conftest.json_obj["Dashboard"]["view_project"]
PROJECT_DETAILS = conftest.json_obj["Dashboard"]["project_details"]
CHAPTER_VERSION = conftest.json_obj["Dashboard"]["chapter_version"]
DELETE = conftest.json_obj["Dashboard"]["delete"]
CLOSE = conftest.json_obj["Dashboard"]["close"]
RE_OPEN = conftest.json_obj["Dashboard"]["re-open"]
YES = conftest.json_obj["Dashboard"]["yes"]

PROJECT_NAME = conftest.json_obj["Add Project"]["project_name"]
TITLE = conftest.json_obj["Add Project"]["title"]


# Add Project

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

# Project View Page

DEF_MANAGEMENT = conftest.json_obj["Project View"]["def_management"]
EXT_LINK_MANAGEMENT = conftest.json_obj["Project View"]["ext_link_management"]
LOAD_PROPOSALS = conftest.json_obj["Project View"]["load_proposals"]
SHOW_CHAP_VERSION = conftest.json_obj["Project View"]["show_chap_version"]
SAVE_ORDER = conftest.json_obj["Project View"]["save_order"]


# Chapter Over view

OPEN_CHAPTER = conftest.json_obj["Chapter View"]["open_chapter"]
VALIDATE_LINKS = conftest.json_obj["Chapter View"]["validate_links"]
READY_REL_PUBS = conftest.json_obj["Chapter View"]["ready_rel_pubs"]
RETURN_TO_PUBS = conftest.json_obj["Chapter View"]["return_to_pubs"]
COMPLETE = conftest.json_obj["Chapter View"]["complete"]
CDP_ACCESS_SYN = conftest.json_obj["Chapter View"]["cdp_access_syn"]
NOTES = conftest.json_obj["Chapter View"]["notes"]

# Content Edit Page

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

SET_FIG_ORDINAL = conftest.json_obj["Content Edit"]["set_fig_ordinal"]
FIG_TITLE = conftest.json_obj["Content Edit"]["fig_title"]
FIG_NOTE_ABOVE = conftest.json_obj["Content Edit"]["fig_note_above"]
FIG_NOTE_BELOW = conftest.json_obj["Content Edit"]["fig_note_below"]
FIG_ALT = conftest.json_obj["Content Edit"]["fig_alt"]

# Footer

NEW_CHAPTER = conftest.json_obj["Footer_model"]["new_chapter"]
NEW_CODE_ELEMENT = conftest.json_obj["Footer_model"]["new_code_element"]

SECTION = conftest.json_obj["New Code Element"]["section"]
FIGURE = conftest.json_obj["New Code Element"]["figure"]
TABLE = conftest.json_obj["New Code Element"]["table"]

# Relocate Popup
VALIDATE_LOCATION = conftest.json_obj["Relocate alert"]["validate_location"]
RELOCATE_CHAPTER = conftest.json_obj["Relocate alert"]["relocate_chapter"]
RELOCATE_SECTION = conftest.json_obj["Relocate alert"]["relocate_section"]
RELOCATE_FIG = conftest.json_obj["Relocate alert"]["relocate_fig"]
VALID_ORDINAL = conftest.json_obj["Relocate alert"]["valid_ordinal_msg"]


# Appendix

APPENDIX_TITLE = conftest.json_obj["Content Edit"]["appendix_title"]
APPENDIX_CONTENT = conftest.json_obj["Content Edit"]["appendix_content"]
APPENDIX_DELETE = conftest.json_obj["Content Edit"]["delete_appendix"]
SET_APPENDIX_ORDINAL = conftest.json_obj["Content Edit"]["set_appendix_ordinal"]
APPENDIX_ORDINAL = conftest.json_obj["Content Edit"]["appendix_ordinal"]
RELOCATE_APPENDIX = conftest.json_obj["Relocate alert"]["relocate_appendix"]
NEW_APPENDIX = conftest.json_obj["Footer_model"]["new_appendix"]


# Fm Chapter

FM_CHAP_TITLE = conftest.json_obj["Content Edit"]["fm_chapter_title"]
FM_CHAP_CONTENT = conftest.json_obj["Content Edit"]["fm_chapter_content"]
NEW_FM_CHAPTER = conftest.json_obj["Footer_model"]["new_fm_chapter"]
