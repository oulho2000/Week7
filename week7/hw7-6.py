import RPi.GPIO as GPIO
import time

PWMA = 18
PWMB = 23
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24

SW1 = 5  
SW2 = 6   
SW3 = 13  
SW4 = 19  

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

L_Motor = GPIO.PWM(PWMA, 500)
R_Motor = GPIO.PWM(PWMB, 500)
L_Motor.start(0)
R_Motor.start(0)

try:
    while True:
        if GPIO.input(SW1) == 1:
            print("SW1: forword")
            GPIO.output(AIN1, 0)
            GPIO.output(AIN2, 1)
            L_Motor.ChangeDutyCycle(100)
            GPIO.output(BIN1, 0)
            GPIO.output(BIN2, 1)
            R_Motor.ChangeDutyCycle(100)

        elif GPIO.input(SW2) == 1:
            print("SW2: right")
            GPIO.output(AIN1, 0)
            GPIO.output(AIN2, 0)
            L_Motor.ChangeDutyCycle(0)
            GPIO.output(BIN1, 0)
            GPIO.output(BIN2, 1)
            R_Motor.ChangeDutyCycle(100)

        elif GPIO.input(SW3) == 1:
            print("SW3: left")
            GPIO.output(AIN1, 0)
            GPIO.output(AIN2, 1)
            L_Motor.ChangeDutyCycle(100)
            GPIO.output(BIN1, 0)
            GPIO.output(BIN2, 0)
            R_Motor.ChangeDutyCycle(0)

        elif GPIO.input(SW4) == 1:
            print("SW4: back")
            GPIO.output(AIN1, 1)
            GPIO.output(AIN2, 0)
            L_Motor.ChangeDutyCycle(100)
            GPIO.output(BIN1, 1)
            GPIO.output(BIN2, 0)
            R_Motor.ChangeDutyCycle(100)

        else:
            GPIO.output(AIN1, 0)
            GPIO.output(AIN2, 0)
            L_Motor.ChangeDutyCycle(0)
            GPIO.output(BIN1, 0)
            GPIO.output(BIN2, 0)
            R_Motor.ChangeDutyCycle(0)

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

L_Motor.stop()
R_Motor.stop()
GPIO.cleanup()