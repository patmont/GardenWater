import RPi.GPIO as GPIO
from apscheduler.schedulers.blocking import BlockingScheduler
import time, datetime

print("Starting up!")

sched = BlockingScheduler()

try:
    while True:
        @sched.scheduled_job('cron', hour='8,18')
        def water():
            # Initialize GPIO
            GPIO.cleanup()
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(18, GPIO.OUT)
            GPIO.setup(21, GPIO.OUT)

            # Actions
            GPIO.output(21, GPIO.HIGH)
            print('On @ ' + str(datetime.datetime.now()))
            time.sleep(1800)
            GPIO.output(21, GPIO.LOW)
            print('Off @ ' + str(datetime.datetime.now()))
        sched.start()

except KeyboardInterrupt:
    sched.shutdown(wait=False)
    print('Shutdown the Scheduler.')