import RPi.GPIO as GPIO
import time

f = open("/home/dhruv/Auto-Segregating-Bin/transfer.txt","r")
final = f.read()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

p = GPIO.PWM(11, 50)
final = final.strip()
print(final)

initial=3
left_cycle=0.1
right_cycle=4.5

p.start(initial)
print('changing cycle')
p.ChangeDutyCycle(initial)  # turn towards 90 degree
print('done')
if(final=='0' or final=='3'):
    print('Bio Degreadable Waste')	
    p.ChangeDutyCycle(right_cycle)
    time.sleep(3)
    p.ChangeDutyCycle(initial)
    print('Back to position')
    time.sleep(3)
elif(final=='1' or final=='2' or final=='4' or final=='5'):
    print('Non Bio Degreadable Waste')
    p.ChangeDutyCycle(left_cycle)
    time.sleep(3)
    p.ChangeDutyCycle(initial)
    print('Back to position')

    time.sleep(3)

p.stop()
GPIO.cleanup()
