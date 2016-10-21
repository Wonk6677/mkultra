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

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

#pygame statup
pygame.init()
pygame.mixer.init()
alert = pygame.mixer.Sound("bell.wav")


def distance():
        # set Trigger to HIGH
        GPIO.output(GPIO_TRIGGER, True)

        # set Trigger after 0.05ms to LOW
        time.sleep(0.00005)
        GPIO.output(GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
                StartTime = time.time()

        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
                StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

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
