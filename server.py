 from http.server import SimpleHTTPRequesthandler,HTTPserver
 class MyHandler(SimpleHTTPRequesthandler):
        def do_GET(self)
        if self.path =='/':
            self.path = 'index.html'
            return super().do_GET()
            if__name __=="__main_":
        server = HTTPserver(('localhost',8000),MyHandler)
        printf("server on http://localhost:8000")
        server.server_forever()
    