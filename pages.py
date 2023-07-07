from pages_view import PagesView


class PC:
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
        return PagesView.order()

    @staticmethod
    def example():
        return PagesView.example()
