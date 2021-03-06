# -*- coding: utf-8 -*-
import socket
import os


def write_text_response(code, text):
    return '''HTTP/1.1 ''' + str(code) + '''\r\nContent-Type: text/html\r\nContent-Length: ''' + str(len(text)) \
           + '''\r\n\r\n''' + text + '''\r\n\r\n'''


def make_index_response(user_agent):
    return write_text_response('''200 OK''', '''Hello mister!\nYou are: ''' + user_agent)


def make_test_response(request):
    return write_text_response('''200 OK''', request)


def make_media_response(filename):
    listdir = os.listdir(os.path.join('..', 'files'))

    if filename == '':
        return write_text_response('''200 OK''', ' '.join(listdir))
    else:
        if filename not in listdir:
            return write_text_response('''404 Not found''', 'File not found')
        else:
            with open(os.path.join('..', 'files', filename), 'r') as current_file:
                return write_text_response('''200 OK''', current_file.read())


# form our http response for the request string
def get_response(request):
    request = request.decode()
    if not request.startswith('GET '):
        return write_text_response('''404 Not found''', 'Page not found').encode()

    uri = request[4:request.find(' ', 4)]

    if uri == '/':
        part = request[request.find('\r\nUser-Agent: ') + 14:]
        return make_index_response(part[:part.find('\r\n')]).encode()
    elif uri == '/test/':
        return make_test_response(request).encode()
    elif uri.startswith('/media/'):
        filename = uri[7:]
        return make_media_response(filename).encode()
    else:
        return write_text_response('''404 Not found''', 'Page not found').encode()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  # specify our server to listen host=localhost port=8000
server_socket.listen(0)  # enable our server to accept connections (0 unaccepted connections allowed before refusing)

print('Started')

while 1:
    try:
        (client_socket, address) = server_socket.accept()

        # get address and port for the client socket
        print('Got new client', client_socket.getsockname())

        request_string = client_socket.recv(2048)  # read data from the client (max amount to be received = 2048 bytes)
        client_socket.send(get_response(request_string))  # form and write our http response to the client socket
        client_socket.close()
    except KeyboardInterrupt:  # catch an exception raising when run.py is stopped from the console
        print('Stopped')
        server_socket.close()  # close server socket opened on our computer
        exit()
