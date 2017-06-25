import RPi.GPIO as GPIO
import time 

#set up pin 4, 17, 27 as an output
GPIO.setmode(gpio.BCM)
GPIO.setWARMINGS(False)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)   #setup variables for user input
led = GPIO.PWM(4,100)
led = GPIO.PWM(17,100)
led = GPIO.PWM(27,100)
led_choice = 0
count = 0

print("Enter your input number: ")
print("number 1 (Red):")
print("number 2 (Red, Yellow):")
print("number 3 (Red, Yellow, Green):")
led_choice = input("Make your Choice: ")

if led_choice == 1:

print "You choose the Red LED"
count = input("How many times you want it to blink?: ")
while count > 0:
GPIO.output(4,GPIO.HIGH)
time.sleep(1)
GPIO.output(4,GPIO.LOW)
time.sleep(1)
count = count - 1



if led_choice == 2:
print "You choose the Red and Yellow LED"
count = input("How many times you want it to blink?: ")
while count > 0:
GPIO.output(4,GPIO.HIGH)
time.sleep(1)
GPIO.output(4,GPIO.LOW)
time.sleep(1)
count = count - 1

while count > 0:
GPIO.output(17,GPIO.HIGH)
time.sleep(1)
GPIO.output(17,GPIO.LOW)
time.sleep(1)
count = count - 1




if led_choice == 3:
print "You choose the Red, Yellow,and Green LED"
count = input("How many times you want it to blink?: ")
while count > 0:
GPIO.output(4,GPIO.HIGH)
time.sleep(1)
GPIO.output(4,GPIO.LOW)
time.sleep(1)
count = count - 1

while count > 0:
GPIO.output(17,GPIO.HIGH)
time.sleep(1)
GPIO.output(17,GPIO.LOW)
time.sleep(1)
count = count - 1

while count > 0:
GPIO.output(27,GPIO.HIGH)
time.sleep(1)
GPIO.output(27,GPIO.LOW)
time.sleep(1)
count = count - 1

if led_choice > 3:
print "Your choice is ouside the range"
break

except KeyboardInterrupt
led.stop()
GPIO.cleanup()
