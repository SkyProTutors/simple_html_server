from unicodedata import category

from controller import PageController

ROUTES = {
    '/': PageController.main_page,
    '/hello': PageController.hello,
    '/error': PageController.error,
    '/top': PageController.top,
    '/example': PageController.example,
    '/main': PageController.main_page,
    '/contacts': PageController.contacts,
    '/category': PageController.category,
    '/catalog': PageController.catalog,
    404: PageController.error2
}