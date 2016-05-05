from time import sleep
from datetime import datetime
import picamera

def takeimage():
	turn=0
		while True:
			camera = picamera.PiCamera()
			time=datetime.now().strftime("date:%Y-%m-%dtime:%H:%M:%S")
			camera.capture('/home/pi/Desktop/image%d'+time+'.jpg'%turn)
			turn =turn+1
			print ('/home/pi/Desktop/image'+str(turn)+"_"+str(time)+'.jpg')
			sleep(30)
			time=datetime.now().strftime("date:%Y-%m-%dtime:%H:%M:%S")
			camera.capture('/home/pi/Desktop/image%d'+time+'.jpg'%turn)
			turn =turn+1
			print ('/home/pi/Desktop/image'+str(turn)+"_"+str(time)+'.jpg')
			sleep(30)
