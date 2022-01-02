#client
import socket 
s = socket.socket()
ip ='localhost'
port = 9999
s.connect((ip, port))
print('connected ! Welcome...')

while True:
    print(s.recv(1024).decode())
    msg = input("your message>>>>")
    s.send(msg.encode())