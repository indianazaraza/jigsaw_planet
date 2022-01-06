from selenium.webdriver.common.by import By

class Locators():
	"""Class that contains all locators
	"""
	search_bar = (By.XPATH, "/html/body/div/main/div/div[2]/div[2]/div[1]/div[1]/div/div[3]/div/input")
	link = (By.XPATH, "/html/body/div/main/div/div[2]/div[2]/div[2]/div[4]/table/tbody/tr/td[3]/a")