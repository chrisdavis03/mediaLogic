import videoInput
import serializer

vid = videoInput.VideoInput('/Users/davisc/Downloads/2019_03_31_001-edit.mp4')
vidShort = videoInput.VideoInput('/Users/davisc/Desktop/PG-Vick-SYR-15-CaHD_C001_SRC-EXT.mov')

data = vidShort.videoRead()
serializer.toJson(data)

#if __name__ == "__main__":
#    mediaLogic().run()