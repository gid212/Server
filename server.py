import os
import http.server
import socketserver
from http import HTTPStatus
from urllib.parse import urlparse, parse_qs
# import socket
# import sys

# define host and port
# host = '64.227.27.104'
# port = 8080
# password = 'Hello321Hello'


# # create socket on server side using TCP/IP protocol
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # bind the socket with the server and the port number
# sock.bind((host, port))
# print ("Binding successful")

# # get input for user name
# name = input('Enter name: ')

# # define max number of connections to socket
# sock.listen(1)

# # wait until client accepts connection
# conn, addr = sock.accept()
# print("CONNECTION FROM:", str(addr))

# # retrieve the client name(in binary) and decode to string
# client = (conn.recv(1024)).decode()
# print(client + ' has connected.')
# # send server side user's name in binary string
# conn.send(name.encode())

# while True:
#     message = input('Me : ')
#     conn.send(message.encode())
#     message = conn.recv(1024)
#     message = message.decode()
#     print(client, ':', message)

# sock.close()

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        msg = query_components["msg"] 
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'who is joe %s' % (msg)
        self.wfile.write(msg.encode("utf-8"))


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
