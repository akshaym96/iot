import urllib2
from time import sleep
from datetime import datetime
#import picamera
#location=[]
#n=0
def main():
        n=0
        # templon3=0
        # templat3=0
        while True:
                
                templon=0
                templat=0
                flag=0
                
                #while(True):
                fo = open("file2", "r+")
                str0 = fo.read(160)
                fo.close()
                location=[]
                location=str0.split()
                lon = location[0]
                print "recive"+lon
                lat = location[1]
                print lat

                file = open("temp_coord","r")
                str1 = file.read(160)
                file.close()
                location1=[]
                location1=str1.split()
                templon = location1[0]
                templat = location1[1]

                #file3=open("temp_read.txt","w")

                #file3.close()

                if templat==lat and templon==lon:
                        print "check"
                       
                        n=n+1
                        print n
                        if n==2:
                                  
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

                if n >=2:
                        print "entered if"
                        print n
                        if n==2 and flag==1:
                                print "Need to take images..."
                                #camera = picamera.PiCamera()
                                for var in range(0,5):
                                        time=datetime.now().strftime("date:%Y-%m-%dtime:%H:%M:%S")
                                        print ('/home/pi/Desktop/image'+str(var)+"_"+str(time)+'.jpg')
                                        #camera.capture('/home/pi/Desktop/image%d'+time+'.jpg'%var)
                                        #push image to server
                                        sleep(3)
                                #flag=1
                                flag=0
                             
                else:
                        time=datetime.now().strftime("date:%Y-%m-%dtime:%H:%M:%S")
                        response=urllib2.urlopen("http://chillar.esy.es/address.php?long="+lon+"&lati="+lat+"&tim="+time)
                        # print "hi"
                sleep(5)

# burst check for next coordinate change
# 30 seconds upload process and push image to server
# push button check