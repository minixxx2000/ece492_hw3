import RPi.GPIO as GPIO
import time

pin_num = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_num,GPIO.OUT)

pwm_led = GPIO.PWM(pin_num,500) #freq = 500
pwm_led.start(100)
try:
	while True:
		GPIO.output(pin_num, True)
		time.sleep(0.5)
		GPIO.output(pin_num, False)
		time.sleep(0.5)
		
finally:
	print("cleaning up")
	GPIO.cleanup()
