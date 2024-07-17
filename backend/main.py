from http.server import BaseHTTPRequestHandler, HTTPServer
from cgi import FieldStorage
from json import dumps
from mimetypes import guess_type
from os import path

dir_path = path.dirname(path.realpath(__file__))
port = 8000

def evaluate_image_to_number(image):
    # TODO: 完成这个函数，将前端传来的image图片文件上的数字/算式识别并返回给前端
    # 下面是样例代码，会把image保存到本地input.png文件中并固定返回1
    with open(dir_path + '/input.png', 'wb') as file:
        file.write(image.read())
    return 1

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        file_path = dir_path + '/public' + ('/index.html' if self.path == '/' else self.path)
        with open(file_path, 'rb') as file:
            self.send_response(200)
            self.send_header('Content-Type', guess_type(file_path)[0])
            self.end_headers()
            self.wfile.write(file.read())
    def do_POST(self):
        if self.path == '/api':
            form = FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )
            image = form['image'].file
            number = evaluate_image_to_number(image)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(dumps({'output': number}).encode('utf-8'))

if __name__ == '__main__':
    httpd = HTTPServer(('localhost', port), RequestHandler)
    print('Server running on port: ', port)
    httpd.serve_forever()
