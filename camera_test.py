from py_camera_client import VideoStream
import cv2

# initialization
stream = VideoStream(usePiCamera=False, resolution=(640, 480), 
                 framerate=30).start()

try:
    while True:                   
            cv2.imshow("1", stream.read())  
            cv2.waitKey(1)
            
except KeyboardInterrupt:
    print("Keyboard Interrupt")
    stream.stop()
    
finally:
    cv2.destroyAllWindows()
