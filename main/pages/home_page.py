from main.base.base_page import BasePage
from main.pages.jigsaw_list_page import JigsawListPage
from main.ui.home import Home


class HomePage(BasePage):
    __driver = None

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    def search_jigsaw(self, category: str):
        self.type_word(self.by_xpath(Home.search_bar), category)
        self.click(self.by_xpath(Home.search_btn))
        return JigsawListPage(self.driver)

