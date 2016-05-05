#server script
import socket
from time import sleep
import os
import multiprocessing
import process1
#import threads
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("192.168.0.110",12345))
sock.listen(2)
(client,(ip,port))=sock.accept()
flag=0
while True:
	gpsdata = client.recv(1204)
	#print gpsdata
	file = open("file2","w")
	file.write(gpsdata)
	file.close()
	#os.system("python process.py")
	if flag==0:
		newprocess=multiprocessing.Process(target=process1.main)      #Parallel process for burst check and others
		newprocess.start()
		#newprocess1=multiprocessing.Process(target=image.takeimage)  # Take image two times per minute
		#newprocess1.start()
		flag=1
	sleep(5)