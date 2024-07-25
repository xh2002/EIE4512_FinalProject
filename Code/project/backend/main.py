from http.server import BaseHTTPRequestHandler, HTTPServer
from cgi import FieldStorage
from json import dumps
from mimetypes import guess_type
from os import path
import subprocess

dir_path = path.dirname(path.realpath(__file__))
port = 8000

def evaluate(input):
    # TODO: 完成这个函数，将前端传来的input图片识别并返回output图片
    # 下面是样例代码，会把input图片保存到本地input.png文件中并直接把文件再返回回去
    file_path = dir_path + '/input.png'
    with open(file_path, 'wb') as file:
        file.write(input.read())
    subprocess.run(['python', path.join(dir_path, 'pre_process.py')])
    subprocess.run(['python', path.join(dir_path, 'CNN_recognition.py')]) 
    file_path = dir_path + '/output.jpg'   
    with open(file_path, 'rb') as file:
        return file.read()

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        file_path = dir_path + '/public' + ('/index.html' if self.path == '/' else self.path)
        with open(file_path, 'rb') as file:
            self.send_response(200)
            self.send_header('Content-Type', guess_type(file_path)[0])
            self.end_headers()
            self.wfile.write(file.read())
    def do_POST(self):
        if self.path == '/api/evaluate':
            form = FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )
            input = form['input'].file
            output = evaluate(input)
            self.send_response(200)
            self.send_header('Content-Type', 'image/png')
            self.end_headers()
            self.wfile.write(output)

if __name__ == '__main__':
    httpd = HTTPServer(('localhost', port), RequestHandler)
    print('Server running on port: ', port)
    httpd.serve_forever()
