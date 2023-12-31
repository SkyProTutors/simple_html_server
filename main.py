import urllib
from http.server import BaseHTTPRequestHandler, HTTPServer
from routes import ROUTES

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        self.routes = ROUTES
        super().__init__(*args, **kwargs)




    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        print(self.path)
        if self.path in self.routes:
            handler = self.routes[self.path]
            page_content = handler()
        else:
            #self.path = 404
            #handler = self.routes[self.path]
            self.path = "/error"
            page_content = self.routes[404]()

        if self.path in ("/error", "/top", "/hello"):
            self.wfile.write(bytes("<html><head><title>boo</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes(page_content, "utf-8"))    # page content was created by handler() / self.routes
            self.wfile.write(bytes("</body></html>", "utf-8"))
        else:
            self.wfile.write(bytes(page_content, "utf-8"))


    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            decoded_message = urllib.parse.unquote(post_data)
            print("Получили с клиента вот такое: \n", decoded_message, "\n")
        except:
            self.send_error(404, "{}".format("hren-znaet-chto exception"))
            # print(sys.exc_info())


if __name__ == '__main__':


    webServer = HTTPServer((hostName, serverPort), MyServer)

    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
