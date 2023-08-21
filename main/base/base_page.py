from selenium.webdriver.common.by import By


class BasePage:
    """Base class
    """
    __driver = None

    def __init__(self, driver):
        """Initialize a driver

        :param driver: path to locate your webdriver
        :type driver: str
        """
        self.driver = driver

    def get(self, url):
        """Get a web page given an url

        :param url: url of a web page
        :type url: string
        """
        self.driver.get(url)

    def type_word(self, locator: tuple, word: str):
        """Given a word send keys to an element given a locator
        :param locator: attribute or path of the element to locate
        :type locator: tuple
        :param word: a word
        :type word: str
        """
        self.driver.find_element(*locator).send_keys(word)

    def click(self, locator: tuple) -> None:
        """Clicks on an element given a locator

        :param locator: attribute or path of the element to locate
        :type locator: tuple
        """
        self.driver.find_element(*locator).click()

    def by_xpath(self, locator: str) -> tuple:
        return By.XPATH, locator

    def by_name(self, locator: str) -> tuple:
        return By.NAME, locator

    def get_text(self, locator: tuple):
        return self.driver.find_element(*locator).text

    def get_element(self, locator: tuple):
        return self.driver.find_element(*locator)

    def get_elements(self, locator: tuple) -> list:
        return self.driver.find_elements(*locator)
