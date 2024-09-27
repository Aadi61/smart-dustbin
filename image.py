from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=24, trigger=23)

from picamera2 import Picamera2
import time
from predict import Predict
import cv2

def ip():
    # Initialize the PiCamera2
    with Picamera2() as picam2:
        # Start the camera
        picam2.start()
        print('Camera started')        

        # Infinite loop to continuously capture photos and perform inference
        while True:
            try:
                ultrasonic.wait_for_in_range()
                print('in range')
                # Capture an image
                picam2.capture_file("test.jpg")

                # Initialize the predictor
                predictor = Predict()

                # Perform inference on the captured image
                frame = cv2.imread("test.jpg")
                predictor.inference(frame)

                # Wait for 10 seconds before capturing the next image
#                time.sleep(10)
            except KeyboardInterrupt:
                # Stop the camera and exit the loop on KeyboardInterrupt
                picam2.stop()
                break

# Call the function to continuously capture images and perform inference
ip()
