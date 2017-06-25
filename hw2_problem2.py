# Hw2_problem_2
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import time

def liteon(pin,tiim):
		 GPIO.output(pin,GPIO.HIGH)
		 time.sleep(tiim)
def liteoff(pin,tiim):
		 GPIO.output(pin,GPIO.LOW)
		 time.sleep(tiim)
		 return
		 
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

for i in range(0,5):
		liteon(4,2)
		liteoff(4,0.1)
		liteon(17,2)
		liteoff(17,0.1)
		liteon(18,2)
		liteoff(18,0.1)
		liteon(27,2)
		liteoff(27,0.1)  # if the user do not want an extra blink between the end of start and begin of reverse, you can change a 
						 # longer time, and delete the first two lines.
		
		liteon(27,2)
		liteoff(27,0.1)
		liteon(18,2)
		liteoff(18,0.1)
		liteon(17,2)
		liteoff(17,0.1)
		liteon(4,2)
		liteoff(4,0.1)
print ('Finish')
		
GPIO.cleanup()
