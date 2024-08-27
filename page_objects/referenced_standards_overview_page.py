from uitility.baseclass import Baseclass
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.common.keys import Keys


class Referenced_Standards_Overview_Page:
    def __init__(self, baseclass) -> None:
        self.baseclass: Baseclass = baseclass
        self.action = self.baseclass.action_chain()

    # Content Page
    __ref_chapter_content_text = (
        By.XPATH,
        "//section[@class='chapter referenced_standards_chapter']//div",
    )
    # Promulgator
    __promulgator_acronym = (
        By.XPATH,
        "//div[@class='sectionLink selected']//p[@class='promulgator_acronym']",
    )
    __promulgator_url = (
        By.XPATH,
        "//div[@class='sectionLink selected']//p/a",
    )
    __promulgator_info = (
        By.XPATH,
        "//div[@class='sectionLink selected']//div[@class='promulgator_contact_info']/span",
    )

    # Referenced standards

    __referenced_standards_info = (
        By.XPATH,
        "//div[@class='sectionLink selected']//div[@class='referenced_standards']/div",
    )
    __referenced_standards_count = (By.XPATH, "//span[@aria-label='Badge']")

    __sections_referencing_standard = (
        By.XPATH,
        "//p[contains(text(),'Sections Referencing Standard')]/parent::div//input",
    )
    __section_lable = (By.XPATH, "//div[@class='v-chip__content']")

    @allure.step("Get Ref Chapter content")
    def get_ref_chapter_content_text(self):
        """To get Chapter content text"""
        return self.baseclass.get_text(self.__ref_chapter_content_text)

    @allure.step("Get Promulgator accronym")
    def get_promulgator_acronym_text(self):
        text = self.baseclass.get_text(self.__promulgator_acronym)
        with allure.step(text):
            return text

    @allure.step("Get Promulgator URL")
    def get_promulgaotr_url(self):
        text = self.baseclass.wait_until(self.__promulgator_url).get_attribute("href")
        with allure.step(text):
            return text

    @allure.step("Get Promulgator {field}")
    def get_promulgator_info(self, field):
        """To get promuglator info
        :param : name, specific_addressee, specific_location, street_address, city, state, postal_code, country
        :return : value of parameter
        """
        text = ""
        for i in self.baseclass.wait_until_elements(self.__promulgator_info):
            if field in i.get_attribute("class"):
                text = i.text
                break
        else:
            raise Exception(f"Promulgator {field} text is not showing")

        with allure.step(text):
            return text

    @allure.step("Get Referenced Standard {field}")
    def get_reference_standard_info(self, field, sr_number: int):
        """To get refrenece standard info
        :param : number, title, sections
        :return : value of parameter
        """
        text = ""
        ref_standard = self.baseclass.wait_until_elements(
            self.__referenced_standards_info
        )[sr_number].find_elements(By.TAG_NAME, "p")
        for i in ref_standard:
            if field in i.get_attribute("class"):
                text = i.text
                break
        else:
            raise Exception(f"{field} is not showing")
        with allure.step(text):
            return text

    @allure.step("Get Referenced Standard Sections")
    def get_referenced_standard_sections(self, title):
        sections = []
        for i in self.baseclass.wait_until_elements(self.__referenced_standards_info):
            if title in i.text:
                sections = [j.text for j in i.find_elements(By.TAG_NAME, "a")]
                break
        else:
            raise Exception(f"{title} sections are not showing")
        return sections

    @allure.step("Get Referenced Standard Count Bedge")
    def get_referenced_standard_count(self):
        text = self.baseclass.get_text(self.__referenced_standards_count)
        with allure.step(text):
            return text

    @allure.step("Enter {section_number}")
    def enter_section_number(self, section_number):
        self.action.click(
            self.baseclass.wait_until(self.__sections_referencing_standard)
        ).send_keys(section_number).send_keys(Keys.ENTER).perform()

    @allure.step("Get Section Lable")
    def get_section_lable(self):
        label = [
            i.text for i in self.baseclass.wait_until_elements(self.__section_lable)
        ]
        with allure.step(str(label)):
            return label

    @allure.step("Click on close section label")
    def click_close_section_lable(self, section_label):
        for i in self.baseclass.wait_until_elements(self.__section_lable):
            if i.text == section_label:
                i.find_element(By.TAG_NAME, "i").click()
                break
        else:
            raise Exception(f"{section_label} is not present in Reference standard")
