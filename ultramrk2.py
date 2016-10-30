# -*- coding: utf-8 -*-
#Libraries
import RPi.GPIO as GPIO
import time
import pygame

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO_TRIGGER1 = 14
GPIO_ECHO1 = 15

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)

#pygame statup
pygame.init()
pygame.mixer.init()
alert = pygame.mixer.Sound("bell.wav")


def distance():
        # set Trigger to HIGH
        GPIO.output(GPIO_TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
                StartTime = time.time()

        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
                StopTime = time.time()

        # time difference between start and arrival for both sensors
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance0 = (TimeElapsed * 34300) / 2

        time.sleep(0.25)

        ###### Second sensor

        # set TRIGGER1 to HIGH
        GPIO.output(GPIO_TRIGGER1, True)

        # set Trigger1 after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER1, False)

        StartTime1 = time.time()
        StopTime1 = time.time()

        # save StartTime1
        while GPIO.input(GPIO_ECHO1) == 0:
                StartTime1 = time.time()

        # save time of arrival1
        while GPIO.input(GPIO_ECHO1) == 1:
                StopTime1 = time.time()

        #time differance
        TimeElapsed1 = StopTime1 - StartTime1
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance1 = (TimeElapsed1 * 34300) / 2

        distance = min(distance0, distance1)

        return distance



if __name__ == '__main__':
        try:
                while True:
                        dist = distance()
                        print ("Measured Distance = %.lf cm" % dist)
                        if dist > 75:
                                alert.play()
                        elif dist > 30:
                                alert.play(1)
                        elif dist <30:
                                alert.play(3)
                                print ("STOP")
                        time.sleep(0.75)

                # Reset by pressing CTRL + C
        except KeyboardInterrupt:
                print("Measurement stopped by User")
                GPIO.cleanup()
