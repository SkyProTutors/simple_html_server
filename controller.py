from pages_view import PagesView


class PageController:
    @staticmethod
    def index():
        return PagesView.index()

    @staticmethod
    def hello():
        return PagesView.hello()

    @staticmethod
    def error():
        return PagesView.error()

    @staticmethod
    def top():
        return PagesView.top()

    @staticmethod
    def error2():
        return PagesView.error2()

    @staticmethod
    def example():
        return PagesView.example()

    @staticmethod
    def main_page():
        return PagesView.main_page()

    @staticmethod
    def catalog():
        return PagesView.catalog()

    @staticmethod
    def category():
        return PagesView.category()

    @staticmethod
    def contacts():
        return PagesView.contacts()