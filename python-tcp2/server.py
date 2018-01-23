import sys
import socket 
import os

TCP_IP = "127.0.0.1"
TCP_PORT = 5008
FILE_NAME = 'masako.jpg'

print "TCP target IP:", TCP_IP
print "TCP target port:", TCP_PORT
print "Image:", FILE_NAME


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((TCP_IP,TCP_PORT))
sock.listen(10)

while True :
    data,addr = sock.accept()
    newpath = r'file-upload/' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    fileUpload = open(newpath+FILE_NAME,"wb")
    sData = data.recv(1024)
    while sData:
        fileUpload.write(sData)
        sData = data.recv(1024)
    print "Upload Completed"
sock.close()
