from myServerPage import MyServerPage
from locators import Locators

driver_my_server = MyServerPage("your path")

driver_my_server.get_web_page("https://myserver.gg/es")

search_bar = driver_my_server.get_element(Locators.search_bar)

driver_my_server.click(search_bar)

driver_my_server.send_keys(search_bar, "music")

link = driver_my_server.get_element(Locators.link)

driver_my_server.click(link)

driver_my_server.back()

driver_my_server.quit()