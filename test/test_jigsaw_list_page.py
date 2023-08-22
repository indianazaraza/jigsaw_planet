import pytest
from main.pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestJigsawListePage:

    def test_search_jigsaw_by_category(self):
        category = "simpsons"
        home_page = HomePage(self.driver)
        jigsaw_list_page = home_page.search_jigsaw(category)
        assert len(jigsaw_list_page.get_pages_links()) == 5
        assert "9098" in jigsaw_list_page.get_results()
        assert jigsaw_list_page.get_category() == category
