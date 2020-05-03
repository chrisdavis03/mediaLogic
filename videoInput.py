import numpy as np
import cv2
import shotDetect as sd
import subprocess
import json

class VideoInput(object):
    def __init__(self, videoFile):
        self.cap = cv2.VideoCapture(videoFile)

        #fetch techAttributes
        data = subprocess.check_output('ffprobe -loglevel quiet -print_format json -show_streams {}'.format(videoFile), shell=True)
        str = data.decode('ascii')
        attib = json.loads(str)
        for i in attib['streams']:
            if i['codec_type'] == 'video':
                self.videoAttribs = i

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

    def techAttributes(self):
        #todo - Video based validations
        print (self.videoAttribs)



