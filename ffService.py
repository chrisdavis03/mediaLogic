from subprocess import Popen, PIPE
import os
import json
import time

class MediaEngine:
    def __init__(self,fileInput):
        self.source = fileInput
        self.defaultOutpath = '/Users/davisc/Desktop/mediaLogic_sources/output'
        # if os.path.isdir(self.defaultOutpath) != True:
        #     print ('outPath directory does not exist.  Creating it now.')
        #     os.mkdir(outPath)
        self.basename,_ = os.path.basename(self.source).split('.')

    def metaExtract(self):
        p = Popen(['ffprobe', '-loglevel', 'quiet', '-show_format', '-print_format', 'json', '-show_streams', self.source],
                  stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        meta = json.loads(output)
        return meta

    def extractAudio(self):
        outFile = os.path.join(self.defaultOutpath, '{}.wav'.format(self.basename))
        pWav = Popen(['ffmpeg', '-i', str(self.source), '-c:a', 'pcm_s24le', '-y', outFile],stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = pWav.communicate()

        #flac output
        #pFlac = Popen(['ffmpeg', '-i', str(self.source), '-c:a', 'flac', '-y', '/Users/davisc/Desktop/output_01.flac'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        #output, err = pFlac.communicate()

        #todo - return filepath of output file.
        return outFile

    def encodeVideo(self):

        #presets = ('ultrafast', 'superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow', 'slower', 'veryslow')
        presets = ('ultrafast', 'superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow') #slow and slower took FOREVER!


        # for preset in presets:
        #     for crf in range(0,51, 5):
        #         outFile = os.path.join(self.defaultOutpath, '{}_{}_crf{}.mp4'.format(self.basename, preset, crf))
        #         print (outFile)
        #
        #         x642 = Popen(['ffmpeg', '-t', '10', '-i', str(self.source), '-c:v', 'libx264', '-preset', preset, '-crf', str(crf), '-y', outFile],stdin=PIPE, stdout=PIPE, stderr=PIPE)
        #         output, err = x642.communicate()

        outFile = os.path.join(self.defaultOutpath, '{}_crf.mp4'.format(self.basename))
        x264 = Popen(['ffmpeg', '-progress', '/dev/stdout', '-i', str(self.source), '-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '23', '-y',
             outFile], stdin=PIPE, stdout=PIPE, stderr=PIPE)

        #wait until the encode completes.
        while True:
            time.sleep(1)
            if x264.poll() == 0:
                print ("encode complete")
                return 0



if __name__ == "__main__":
    mediaEngine = MediaEngine(fileInput='/Users/davisc/Desktop/mediaLogic_sources/input/2019_03_31_001-edit.mp4')
    mediaEngine.encodeVideo()
