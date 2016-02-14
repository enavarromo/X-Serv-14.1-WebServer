#!/usr/bin/python
import socket


# -------------- Port Set Up --------------
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#mySocket.bind(('localhost', 1234))  # Socket LoopBack
#mySocket.bind((socket.gethostname(), 1234))  # Socket LoopBack Host
mySocket.bind(('192.168.1.132', 1234))  # Socket wlan0 inet addr:192.168.1.132
mySocket.listen(2) # 5 TPC Cons cap

try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        # -------------- Plot Socket Info --------------
        print 'HTTP request received from: '+ str(address)
        print recvSocket.recv(1024)
        if address[0] == '127.0.0.1':
            print "Coming from Loopback"
            # -------------- HTTP to LoopBack --------------
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>Hello World!</h1>" +
                            "You came from LoopBack at IP: " +
                            str(address[0]) + 
                            " and Port: " + str(address[1]) +
                            "</body></html>\r\n")
        else:
            # -------------- HTTP to ext --------------
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>Hello World!</h1>" +
                            "You are at IP: " + str(address[0]) +
                            " and Port: " + str(address[1]) +
                            "</body></html>\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    mySocket.close()
    print("\nExiting Ok")
