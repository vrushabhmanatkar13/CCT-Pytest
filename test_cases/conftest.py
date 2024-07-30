import datetime
import os
import platform

from filelock import FileLock
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from pytest_metadata.plugin import metadata_key
from pytest_html import extras
from uitility.read_config import get_josn_data, read_config
import allure


# print(sys.path)
# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# sys.path.insert(0, parent_dir)
# sys.path.remove('D:\\python program\\ICC-Shop\\test case')
# updated_dir = os.path.join(parent_dir, 'test_case')``


_config = read_config("./Confuguration/config.ini")
zoom_level = _config.get("options", "level")
window_size = _config.get("options", "window_size")

implicit = float(_config.get("wait", "implicit"))
webdriver_wait = float(_config.get("wait", "webdriver_wait"))

_title = _config.get("Project Details", "report_title")
_project_name = _config.get("Project Details", "project_name")
_reporator = _config.get("Project Details", "reporter")

_report_dir = os.path.join(os.getcwd(), "Report")
_screnshot_dir = os.path.join(os.getcwd(), "Screenshot")
_enviroment_dir = os.path.join(os.getcwd(), "allure-results", "environment.properties")

json_obj = get_josn_data("./Test Data/buttons_text.json")


def pytest_addoption(parser):
    """To set command line argument for selecting browser and headless"""

    parser.addoption("--headless", action="store_true", default=False)
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--clean-allure", action="store_true", default=False)
    parser.addoption("--env", action="store", default="dev")


def pytest_configure(config):
    # Set file name as current date and enviroment varibles for html report
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    os.makedirs(_report_dir, exist_ok=True)
    html_report = os.path.join(_report_dir, f"test_report_{timestamp}.html")
    config.option.htmlpath = html_report
    browser_name = config.getoption("--browser")
    env = config.getoption("--env")
    global url
    url = _config.get("enviroment", env)
    config.stash[metadata_key]["Browser"] = browser_name
    config.stash[metadata_key]["URL"] = url

    # Set Enviroment Variables for Allure Report

    env = read_config(_enviroment_dir)
    if _project_name not in env:
        env.add_section(_project_name)
    env.set(_project_name, "Platfrom", platform.platform())
    env.set(_project_name, "Python", platform.python_version())
    env.set(_project_name, "pytest", pytest.__version__)
    env.set(_project_name, "Browser", browser_name)
    env.set(_project_name, "Url", url)
    with open(_enviroment_dir, "w") as configfile:
        env.write(configfile)
        configfile.close()


def pytest_html_report_title(report):
    report.title = _title


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"Project Name : {_project_name}"])
    prefix.extend([f"Reporter : {_reporator}"])


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report: pytest.TestReport = outcome.get_result()

    extra = getattr(report, "extra", [])
    if report.when == "call":

        xfail = hasattr(report, "wasxfail")
        if report.failed or xfail:
            os.makedirs(_screnshot_dir, exist_ok=True)
            image = _screnshot_dir + "/" + report.nodeid.split("::")[-1] + ".png"
            driver.get_screenshot_as_file(image)
            html = (
                '<div><img src="%s" alt="screenshot" style="width:204px;height:128px;" '
                'onclick="window.open(this.src)" align="right"/></div>' % image
            )
            extra.append(extras.html(html))
            allure.attach(
                driver.get_screenshot_as_png(), image, allure.attachment_type.PNG
            )
        report.extras = extra


def pytest_sessionfinish(session):
    import subprocess

    subprocess.run(
        ["allure", "generate", "--clean", "allure-results", "-o", "allure-report"]
    )


@pytest.fixture(
    scope="session", autouse=True
)  # Autouse true will run first then autouse false
def Setup_log_config_file(request):
    allure_results_dir = "allure-results"
    environment_file = "environment.properties"
    lock_file = "allure-results.lock"
    if request.config.getoption("--clean-allure"):
        with FileLock(lock_file):  # only one process can delete the files at a time
            if os.path.exists(allure_results_dir):
                for file_name in os.listdir(allure_results_dir):
                    file_path = os.path.join(allure_results_dir, file_name)
                    if os.path.isfile(file_path) and file_name != environment_file:
                        os.remove(file_path)


@allure.title("Fixture (Package Level): Setup Launch Browser and Teardown Quit Browser")
@pytest.fixture(scope="package", autouse=True)
def launch_browser(request):
    """
    To launch browser and initlize driver,
    Apply implicit wait, Maximize window
    :return: Webdriver
    """
    with allure.step("Launch Browser"):
        global driver
        browser: str = request.config.getoption("--browser")

        if browser.lower() == "chrome":
            driver = chrome_options(request, zoom_level, window_size)
        elif browser.lower() == "firefox":
            driver = firefox_options(request, zoom_level)

        else:
            raise Exception("Browser is not selected")
        # Maximize window
        driver.maximize_window()
        # Implicit wait
        driver.implicitly_wait(implicit)
        driver.get(url)

    # request.cls.driver = driver  # it create class level variable at run time
    with allure.step("Quite Driver"):
        yield driver
        driver.quit()


# @pytest.fixture(scope="class", autouse=True)
# def test_base(request, launch_browser):
#     request.cls.driver = launch_browser
#     request.cls.driver.get(config.get("enviroment", "dev"))
#     print(request.cls.driver.title, "---------------------class")

#     return launch_browser


# def before_class():
#     return launch_browser()


def chrome_options(request, zoom_level, window_size) -> WebDriver:
    """
    This funcation for set chrome desire capabilites.
    :param zoom_level: window zoom level
    :return: chrome driver
    """
    headless = request.config.getoption("--headless")
    options = webdriver.ChromeOptions()
    options.accept_insecure_certs = True
    options.add_argument(f"--force-device-scale-factor={zoom_level}")
    options.add_argument(f"--window-size={window_size}")
    # options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_argument("--incognito")
    # options.add_argument("--ignore-certificate-errors")
    if headless:
        options.add_argument("headless")

    driver = webdriver.Chrome(service=Service(), options=options)
    return driver


def firefox_options(request, zoom_level) -> WebDriver:
    """
    This funcation for set firefox desire capabilites.
    :param zoom_level: window zoom level
    :return: firefox driver
    """
    headless = request.config.getoption("--headless")
    options = webdriver.FirefoxOptions()
    options.accept_insecure_certs = True
    options.set_preference("layout.css.devPixelsPerPx", zoom_level)
    if headless:
        options.add_argument("-headless")
    driver = webdriver.Firefox(service=Service(), options=options)
    return driver
