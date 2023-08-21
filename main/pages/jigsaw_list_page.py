from main.base.base_page import BasePage
from main.ui.jigsaw_list import JigsawList


class JigsawListPage(BasePage):
    def __init__(self, driver):
        super(JigsawListPage, self).__init__(driver)

    def get_results(self):
        return self.get_text(self.by_xpath(JigsawList.results))

    def get_category(self):
        return self.get_text(self.by_xpath(JigsawList.category))

    def get_pages_links(self):
        pages_list = self.get_elements(self.by_xpath(JigsawList.pages_list))
        return [link.get_attribute("href") for link in pages_list]
