#server script
import urllib2
import socket
import RPi.GPIO as GPIO
from time import sleep
import os
import multiprocessing
import process1
import image

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#import threads
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("192.168.0.110",12345))   # Here change the address of Raspberry Pi
sock.listen(2)
(client,(ip,port))=sock.accept()
flag=0
while True:
	input_state = GPIO.input(18)
	gpsdata = client.recv(1204)
	file = open("file2","w")
	file.write(gpsdata)
	file.close()
	if input_state == False:
        print('Start')

        response=urllib2.urlopen("http://chillar.esy.es/make_call.php")
        response=urllib2.urlopen("http://chillar.esy.es/sms_plivo.php")

        if flag==0:
        	
        	newprocess=multiprocessing.Process(target=process1.main)      #Parallel process for burst check and others
        	newprocess.start()
        	newprocess1=multiprocessing.Process(target=image.takeimage)  # Take image two times per minute
        	newprocess1.start()
        	flag=1
	sleep(5)