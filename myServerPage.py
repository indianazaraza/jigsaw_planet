from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

class MyServerPage():
	"""Base class
	"""
	def __init__(self):
		"""Initialize an driver
		"""
		path = Service("/home/maca/chromedriver")
		chrome_options = Options()
		chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
		self.driver = Chrome(service=path, options=chrome_options)
		wait = WebDriverWait(self.driver, 5)


	def get_web_page(self, url):
		"""Get a web page given an url

		:param url: url of a web page
		:type value: string
		"""
		self.driver.get(url)


	def get_element(self, locator):
		"""Find an element on the actual page given a locator

		:param locator: attribute or path of the element to locate
		:type locator: tuple
		:rtype: webdriver	
		:return: an element of a web page 
		"""
		return self.driver.find_element(*locator)
		

	def send_keys(self, element, word):
		"""Given a word send keys to given an element

		:param element: an element of a web page
		:type value: webdriver
		:param word: a word
		:type value: str
		"""
		element.send_keys(word)
		
		
	def click(self, element):
		"""Clicks on the given element 

		:param element: an element of a web page
		:type value: webdriver
		"""
		element.click()


	def back(self):
		"""Go back once in history
		"""
		self.driver.back()


	def quit(self):
		"""Close the driver and page
		"""
		self.driver.quit()
