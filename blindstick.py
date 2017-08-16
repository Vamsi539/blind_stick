import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(13,GPIO.OUT)
#Trigger

GPIO.setup(11,GPIO.IN)
#Echo

GPIO.setup(15,GPIO.OUT)

GPIO.output(15,False)

GPIO.output(13,False)

time.sleep(1)

while True:

	GPIO.output(13,True)

	time.sleep(0.00001)

	GPIO.output(13,False)

	while GPIO.input(11)==0:

		pulse_start=time.time()

	while GPIO.input(11)==1:

		pulse_stop=time.time()

	pulse_duration=pulse_stop-pulse_start

	distance=pulse_duration*17150

	distance=round(distance,2)

	print "Distance is:",distance,"cm"

	if(distance<=30):

		GPIO.output(15,True)

		time.sleep(1)

	else:

		GPIO.output(15,False)

		time.sleep(1)


