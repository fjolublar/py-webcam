from webcam import WebcamVideoStream
import numpy as np
import cv2

class VideoStream:
    
    def __init__(self, src=0, usePiCamera=False, resolution=(320, 240), 
                 framerate=32, image_flip = 0, **kwargs):
        
        self.image_flip = 1
        # check to see if the picamera module should be used
        if usePiCamera:
            from pi_camera import PiVideoStream

			# initialize picamera stream and let the camera sensor to warmup
            self.stream = PiVideoStream(resolution=resolution, 
                                        framerate=framerate, **kwargs)

		# otherwise, we are using OpenCV so initialize the webcam stream
        else:
            self.stream = WebcamVideoStream(src=src,resolution=resolution, 
                                            framerate=framerate)

    def start(self):
		# start the threaded video stream
        return self.stream.start()

    def read(self):
		# return the current frame
        return self.flip_if_needed( self.stream.read() )
    
    def read_jpg(self):
        frame =  self.flip_if_needed ( self.stream.read() )
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def flip_if_needed(self, frame):
        if self.image_flip:
            return np.fliplr(frame)
        return frame
    
    def stop(self):
		# stop the thread and release any resources
        self.stream.stop()
