from jinja2 import Template
from model import Order

class PagesView:

    @staticmethod
    def read_file(filename):
        with open(filename, 'r') as f:
            text = f.read()
        return text

    @staticmethod
    def render(filename, **var):
        filecontent = PagesView.read_file(filename)
        res = Template(filecontent).render(**var)
        return res

    @staticmethod
    def index():
        info = "index"
        res = PagesView.render('templates/uni.html', info=info, pic="https://picsum.photos/300/300")
        return res

    @staticmethod
    def top():
        order_ = Order.top()[:2]
        res = PagesView.render('templates/order.html', orders_top=order_)
        return res

    @staticmethod
    def hello():
        res = PagesView.render('templates/uni.html', info="Hello", pic="https://picsum.photos/300/300")
        return res

    @staticmethod
    def error():
        res = PagesView.render('templates/uni.html', info="Error", pic="https://picsum.photos/300/300")
        return res

    @staticmethod
    def error2():
        res = PagesView.render('templates/uni.html', info="FAIL", pic="")
        return res

    @staticmethod
    def example():
        res = PagesView.render('templates/example.html', info="FAIL", pic="")
        return res