from myServerPage import MyServerPage
from locators import Locators

driver_my_server = MyServerPage("your path")

driver_my_server.get_web_page("https://myserver.gg/es")

driver_my_server.click_and_send_keys(Locators.search_bar, "music")

driver_my_server.click(Locators.link)

driver_my_server.back()

driver_my_server.quit()