# /Users/Kaering/PycharmProjects/test
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

led = 7
print("start....")
GPIO.setup(led, GPIO.OUT)
# GPIO.setup(led, GPIO.IN)

try:
    while True:
        GPIO.output(led, 1)
        time.sleep(50)

        GPIO.output(led, 0)
        time.sleep(0.00001)
        # GPIO.output(TRIG, 0)
        # start = time.time()
        #
        # while GPIO.input(ECHO) == 0:
        #     start = time.time()
        #
        # while GPIO.input(ECHO) == 1:
        #     stop = time.time()
        #
        # distance = (stop - start) * 34000 / 2
        # print(distance)
except KeyboardInterrupt:
    GPIO.cleanup()