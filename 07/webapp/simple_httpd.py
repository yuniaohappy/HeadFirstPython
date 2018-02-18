from http.server import HTTPServer,CGIHTTPRequestHandler
#指定一个端口号
port = 8080
#创建一个HTTP服务器
httpd = HTTPServer(('',port),CGIHTTPRequestHandler)
#显示一个友好的消息提示
print("Starting simple_httpd on port: " + str(httpd.server_port))
#启动服务器
httpd.serve_forever()
