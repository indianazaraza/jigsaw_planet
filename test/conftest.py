import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):
    """Web controller configuration"""
    chrome_options: Options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    path: Service = Service("/home/maca/chromedriver")
    driver: Chrome = Chrome(service=path, options=chrome_options)
    request.cls.driver = driver
    driver.get("https://www.jigsawplanet.com/")
    yield driver
    driver.quit()
