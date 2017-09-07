# We need to import the jsonify object, it will let us
# output json, and it will take care of the right string
# data conversion, the headers for the response, etc
from flask import Flask, render_template
import os
import time
import RPi.GPIO as GPIO
import subprocess as sub
mc=1
ic=1
os.system("/usr/bin/midori -e Fullscreen &")
list=[5,17,16,5,19,11,6,7,3,67,8,28,6,6,7,5,2,10,6,12,14,5,11,3]
def buttonEventHandler(xn):

       global ic,mc
       if xn==23:
        if ic<list[mc-1]:
            ic=ic+1
        else: 
            mc=mc+1
            ic=1
            if mc>23:
             mc=1
        print "handling button event 23"
       elif xn==22:
          if ic==1:
             if mc==1:
               mc=1
               ic=1
             else:
              mc=mc-1
          else:
             ic=ic-1
          print "handling button event 22"
       elif xn==27:
            if mc>24:
             mc=1
             ic=1
            elif mc>0:
             mc=mc+1
             ic=1
            
            print "handling button event 27"
       elif xn==24:
            if mc==1:
             mc=1
             ic=1
            else:
             mc=mc-1
            print "handling button event 24 "

       elif xn==21:
             print "shutdown"
             os.system("sudo shutdowm now")
  # os.system("midori -e Fullscreen &")
       os.system("/usr/bin/midori -e Reload &")
       print "handling button event"
def main():
    # tell the GPIO module that we want to use 
    # the chip's pin numbering scheme
    GPIO.setmode(GPIO.BCM)
  
    # setup pin 23 as an input
    # and set up pins 24 and 25 as outputs
    GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_UP)


    # tell the GPIO library to look out for an 
    # event on pin 23 and deal with it by calling 
    # the buttonEventHandler function
    GPIO.add_event_detect(23,GPIO.FALLING,bouncetime=4000)
    GPIO.add_event_callback(23,buttonEventHandler)
    GPIO.add_event_detect(24,GPIO.FALLING,bouncetime=4000)
    GPIO.add_event_callback(24,buttonEventHandler)
    GPIO.add_event_detect(22,GPIO.FALLING,bouncetime=4000)
    GPIO.add_event_callback(22,buttonEventHandler)
    GPIO.add_event_detect(27,GPIO.FALLING,bouncetime=4000)
    GPIO.add_event_callback(27,buttonEventHandler)
app = Flask(__name__)
main()
@app.route('/')
def index():
   global ic,mc
  # os.system("midori -e Fullscreen &")
  # os.system("exit 1")
   user = {'nickname': 'Migudfdfl'} 
   return render_template('index.html',user=user,ic=ic,mc=mc)
   GPIO.cleanup()
 

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("5000"),debug="True"
    )
    
