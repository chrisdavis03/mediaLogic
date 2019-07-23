import numpy as np
import cv2
import shotDetect as sd

class VideoInput(object):
    def __init__(self, videoFile):
        self.cap = cv2.VideoCapture(videoFile)

    def videoRead(self):
        lastFrame = None
        count = 0
        frameData = []
        while (self.cap.isOpened()):
            ret, frame = self.cap.read()

            if ret == False:
                break
            try:
                mseFF = sd.mseFF(frame, lastFrame)
                frameData.append({'frameNum': count, 'frameMSE': mseFF})
            except:
                pass

            lastFrame = frame

            count += 1
        #return list of dictionaries that will end up as json.
        return frameData
