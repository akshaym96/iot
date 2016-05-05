import urllib2
from time import sleep
from datetime import datetime
import picamera
import ftplib
import traceback

def main():
        n=0
        
        camera = picamera.PiCamera()
        ftp = ftplib.FTP()
        ftp.connect("31.220.16.211", "21")
        print ftp.getwelcome()
        while True:
                
                templon=0
                templat=0
                flag=0
                
               
                fo = open("file2", "r+")
                str0 = fo.read(160)
                fo.close()
                location=[]
                location=str0.split()
                lon = location[0]
                print "Longitude is"+lon
                lat = location[1]
                print "Latitude is"+lat

                file = open("temp_coord","r")
                str1 = file.read(160)
                file.close()
                location1=[]
                location1=str1.split()
                templon = location1[0]
                templat = location1[1]

                if templat==lat and templon==lon:
                      
                       
                        n=n+1
                        #print n
                        if n==3:
                                  
                                  file3 = open("temp_read.txt","r")
                                  str2=file3.read(160)
                                  file3.close()
                                  temp=[]
                                  temp=str2.split()
                                  templon3=temp[0]
                                  templat3=temp[1]

                                  if lat!=templat3 and lon!=templon3:
                                        flag=1
                                        file3=open("temp_read.txt","w")
                                        file3.write(lon+" "+lat)
                                        file3.close()

                      
                else:
                        n=0

                file = open("temp_coord","w")
                file.write(lon+" "+lat)
                file.close()

                if n >=3:
                        #print "entered if"
                        #print n
                        if n==3 and flag==1:
                                print "Start taking images!!"
                                for var in range(0,5):

                                    time=datetime.now().strftime("date:%Y-%m-%dtime:%H:%M:%S")
                                    print ('/home/pi/Desktop/SOS/image'+str(var)+"_"+str(time)+'.jpg')
                                    camera.capture('/home/pi/Desktop/SOS/image'+str(var)+"_"+str(time)+'.jpg')


                                    try:
                                        ftp.login("u140749344", "nikhil")
                                        ftp.cwd("/public_html/SOS_images")
                                        f = open('/home/pi/Desktop/SOS/image'+str(var)+"_"+str(time)+'.jpg', "rb")
                                        name= '/home/pi/Desktop/SOS/image'+str(var)+"_"+str(time)+'.jpg'
                                        ftp.storbinary('STOR ' + name, f)
                                        f.close()
                                    except:
                                        traceback.print_exc()
                                       
                                        #push image to server
                                    sleep(3)
                                
                                flag=0
                             
                else:
                        time=datetime.now().strftime("date:%Y-%m-%dtime:%H:%M:%S")
                        response=urllib2.urlopen("http://chillar.esy.es/address.php?long="+lon+"&lati="+lat+"&tim="+time)
                        
                sleep(5)

