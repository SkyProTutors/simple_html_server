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

        self.wfile.write(bytes("<html><head><title>boo</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))

        print(self.path)

        if self.path in self.routes:
            handler = self.routes[self.path]
            page_content = handler()
        else:
            #self.path = 404
            #handler = self.routes[self.path]
            page_content = self.routes[404]()

        self.wfile.write(bytes(page_content, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == '__main__':


    webServer = HTTPServer((hostName, serverPort), MyServer)

    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")