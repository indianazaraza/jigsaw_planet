from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class MyServerPage():
	"""Base class
	"""
	def __init__(self, driver_path):
		"""Initialize an driver

		:param driver_path: path to locate your webdriver
		:type driver_path: str
		"""
		path = Service(driver_path)
		chrome_options = Options()
		chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
		self.driver = Chrome(service=path, options=chrome_options)
		wait = WebDriverWait(self.driver, 5)


	def get_web_page(self, url):
		"""Get a web page given an url

		:param url: url of a web page
		:type url: string
		"""
		self.driver.get(url)
	

	def click_and_send_keys(self, locator, word):
		"""Given a word send keys to an element given a locator

		:param locator: attribute or path of the element to locate
		:type locator: tuple
		:param word: a word
		:type word: str
		"""
		element = self.driver.find_element(*locator)
		element.click()
		element.send_keys(word)
		
		
	def click(self, locator):
		"""Clicks on an element given a locator

		:param locator: attribute or path of the element to locate
		:type locator: tuple
		"""
		element = self.driver.find_element(*locator)
		element.click()


	def back(self):
		"""Go back once in history
		"""
		self.driver.back()


	def quit(self):
		"""Close the driver and page
		"""
		self.driver.quit()
