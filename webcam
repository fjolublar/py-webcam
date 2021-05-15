from threading import Thread
import cv2

class WebcamVideoStream:
    
    def __init__(self, src=0, resolution=(320, 240), framerate=30, name="WebcamVideoStream"):
		# initialize the video camera stream and read the first frame
		# from the stream
        self.stream = cv2.VideoCapture(src)
        
        
        self.stream.set(cv2.CAP_PROP_FPS, framerate)
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH,  int(resolution[0]) )
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, int(resolution[1]) )
        
        
        (self.grabbed, self.frame) = self.stream.read()

		# initialize the thread 
        self.name = name
        self.t        = Thread(target=self.update, name=self.name, args=())
        self.t.daemon = True

		# initialize a variable used to stop the thread
        self.stopped  = False

    def start(self):
		# start the thread to read frames from the video stream
        self.t.start()
        return self

    def update(self):
		# keep looping infinitely until the thread is stopped
        while True:
			# if the thread indicator variable is set, stop the thread
            if self.stopped:
                break

			# otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()
            
        # release resources after thread is stopped
        self.stream.release()
        return

    def read(self):
		# return the frame most recently read
        return self.frame

    def stop(self):
		# indicate that the thread should be stopped
        self.stopped = True
        
