from time import sleep
from datetime import datetime
import picamera

# This is for taking images regularly i.e., two images per minute

def takeimage():
	turn=0
	camera = picamera.PiCamera()
		while True:

			print "Taking regular images"
			time=datetime.now().strftime("date:%Y-%m-%dtime:%H:%M:%S")
			camera.capture('/home/pi/Desktop/Regular/image'+str(turn)+'_'+str(time)+'.jpg')

			try:

                ftp.login("u140749344", "nikhil")
                ftp.cwd("/public_html/SOS_images")
                f = open('/home/pi/Desktop/Regular/image'+str(turn)+'_'+str(time)+'.jpg', "rb")
                name= '/home/pi/Desktop/Regular/image'+str(turn)+'_'+str(time)+'.jpg'
                ftp.storbinary('STOR ' + name, f)
                f.close()
            except:
                traceback.print_exc()

			turn =turn+1
			print ('/home/pi/Desktop/Regular/image'+str(turn)+'_'+str(time)+'.jpg')
			sleep(30)
			time=datetime.now().strftime("date:%Y-%m-%dtime:%H:%M:%S")
			camera.capture('/home/pi/Desktop/Regular/image'+str(turn)+'_'+str(time)+'.jpg')
			try:

                ftp.login("u140749344", "nikhil")
                ftp.cwd("/public_html/SOS_images")
                f = open('/home/pi/Desktop/Regular/image'+str(turn)+'_'+str(time)+'.jpg', "rb")
                name= '/home/pi/Desktop/Regular/image'+str(turn)+'_'+str(time)+'.jpg'
                ftp.storbinary('STOR ' + name, f)
                f.close()
            except:
                traceback.print_exc()

			turn =turn+1
			print ('/home/pi/Desktop/Regular/image'+str(turn)+'_'+str(time)+'.jpg')
			sleep(30)
