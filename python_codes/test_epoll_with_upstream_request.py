#!/usr/bin/env python

import socket
import select
import argparse
import httplib

SERVER_HOST = 'localhost'

EOL1= b'\n\n'
EOL2 = b'\n\r\n'
SERVER_RESPONSE = b"""HTTP/1.1 200 OK\r\nDate: Mon, 1 Apr 2013 01:01:01
GMT\r\nContent-Type: text/plain\r\nContent-Length: 25\r\n\r\n
Hello from Epoll Server!"""

class Requester(object):
    #self.conn = httplib.HTTPConnection("www.python.org")
    #conn.request("GET", "/index.html")
    #r1 = conn.getresponse()
    #print r1.status, r1.reason #200 OK
    #data1 = r1.read()
    #conn.request("GET", "/parrot.spam")
    #r2 = conn.getresponse()
    #print r2.status, r2.reason #404 Not Found
    #data2 = r2.read()
    #conn.close()

    #def __init__(self):
    #    self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #    self.s.connect(('www.sina.com',80))
    #    self.s.send('''GET https://www.sina.com/ HTTP/1.1
    #    Host: www.sina.com
    #    Connection: keep-alive
    #    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    #    Upgrade-Insecure-Requests: 1
    #    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36
    #    Accept-Language: zh-CN,zh;q=0.8
    #    ''')
    #
    #def recv(self):
    #    buf = self.s.recv(1024)
    #    while len(buf):
    #        print buf
    #        buf = self.s.recv(1024)

    def __init__(self):
        # Set up a TCP/IP socket
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        # Connect as client to a selected server
        # on a specified port
        #self.s.connect(("www.wellho.net",80))
        self.s.connect(("www.baidu.com",80))

        # Protocol exchange - sends and receives
        #self.s.send("GET /robots.txt HTTP/1.0\n\n")
        self.s.send("GET / HTTP/1.0\n\n")

    def recv(self):
        resp = self.s.recv(1024)
        #print "recv"
        if resp == "": return "done" 
        #print resp;

    def close(self):
        # Close the connection when completed
        self.s.close()

class EpollServer(object):
    """ A cocket server using Epoll"""

    def __init__(self, host=SERVER_HOST, port=0):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((host, port))
        self.sock.listen(1)
        self.sock.setblocking(0)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        #print "Started Epoll Server"
        self.epoll = select.epoll()
        self.epoll.register(self.sock.fileno(), select.EPOLLIN)
        self.count_hup = 0

    def run(self):
        """Executes epoll server operation"""
        try:
            connections = {}; requests = {}; responses = {}; upstream_reqs = {};
            while True:
                events = self.epoll.poll(1)
                for fileno, event in events:
                    if fileno == self.sock.fileno():
                        connection, address = self.sock.accept()
                        connection.setblocking(0)
                        self.epoll.register(connection.fileno(), select.EPOLLIN)
                        connections[connection.fileno()] = connection
                        requests[connection.fileno()] = b''
                        responses[connection.fileno()] = SERVER_RESPONSE
                    #elif event & select.EPOLLIN:
                    #    requests[fileno] += connections[fileno].recv(1024)
                    #    if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                    #        self.epoll.modify(fileno, select.EPOLLOUT)
                    #        print('-'*40 + '\n' + responses[fileno].decode()[:-2])

                    elif event & select.EPOLLIN:
                        if fileno in upstream_reqs:
                            #print "fileno in upstream_reqs";
                            if upstream_reqs[fileno][0].recv() == "done":
                                #print "recv done"
                                self.epoll.unregister(fileno)
                                self.epoll.modify(upstream_reqs[fileno][1], select.EPOLLOUT);
                                #self.epoll.modify(fileno, select.EPOLLOUT)
                            #else: #wait for another buffer
                        else:
                            #print "reading cli requests"
                            requests[fileno] += connections[fileno].recv(1024)
                            if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                                req = Requester();
                                #print "Requester newed"
                                upstream_reqs[req.s.fileno()] = (req, fileno);
                                self.epoll.register(req.s.fileno(), select.EPOLLIN)
                                #print "epoll register for upstream request"

                    elif event & select.EPOLLOUT:
                        byteswritten = connections[fileno].send(responses[fileno])
                        responses[fileno] = responses[fileno][byteswritten:]
                        if len(responses[fileno]) == 0:
                            self.epoll.modify(fileno, 0)
                            connections[fileno].shutdown(socket.SHUT_RDWR)
                    elif event & select.EPOLLHUP:
                        self.count_hup += 1
                        #print str(self.count_hup) + " EPOLLHUP got"
                        self.epoll.unregister(fileno)
                        connections[fileno].close()
                        del connections[fileno]
        except BaseException as err:
            print "Error detected"
            print("Error: {0}".format(err))
        finally:
            self.epoll.unregister(self.sock.fileno())
            self.epoll.close()
            self.sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Socket Server Example with Epoll')
    parser.add_argument('--port', action="store", dest = "port", type = int, required = True)
    given_args = parser.parse_args()
    port = given_args.port
    server = EpollServer(host = SERVER_HOST, port = port)
    print "ready to run the server"
    while True:
        server.run()


