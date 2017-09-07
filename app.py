# We need to import the jsonify object, it will let us
# output json, and it will take care of the right string
# data conversion, the headers for the response, etc
from flask import Flask, render_template
from sys import exit
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
app = Flask(__name__)
@app.route('/')
def index(): 
   GPIO.cleanup()
   return render_template('index.html')
   
@app.route('/speed1')
def speed1():
   GPIO.cleanup()
   GPIO.setup(17,GPIO.OUT)
   GPIO.output(17,GPIO.HIGH)
   print "switched to speed 1"
   return render_template('index.html')

@app.route('/speed2')
def speed2():
   GPIO.cleanup()
   GPIO.setup(27,GPIO.OUT)
   GPIO.output(27,GPIO.HIGH)
   print "switched to speed 2"
   return render_template('index.html')

@app.route('/s1')
def s1():
   GPIO.cleanup()
   GPIO.setup(22,GPIO.OUT)
   GPIO.output(22,GPIO.HIGH)
   print "socket on"
   return render_template('index.html',ic="checked")

@app.route('/s0')
def s0():
   GPIO.cleanup()
   GPIO.setup(22,GPIO.OUT)
   GPIO.output(22,GPIO.LOW)
   print "socket off"
   return render_template('index.html')



@app.route('/speed3')
def speed3():
   GPIO.cleanup()
   GPIO.setup(18,GPIO.OUT)
   GPIO.output(18,GPIO.HIGH)
   print "switched to speed 4"
   return render_template('index.html')

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("5000"),debug="True"
    )
    
