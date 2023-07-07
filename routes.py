from pages import PC

ROUTES = {
    '/': PC.index,
    '/hello': PC.hello,
    '/error': PC.error,
    '/top' : PC.top,
    '/example': PC.example,
    404: PC.error2
}