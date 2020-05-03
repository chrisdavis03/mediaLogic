import videoInput
import serializer
import visualize


#vid = videoInput.VideoInput('/Users/davisc/Downloads/2019_03_31_001-edit.mp4')
vidShort = videoInput.VideoInput('/Users/davisc/Desktop/crop_Test/HDNDW101A_E1T1_OMN_156.mov')
vidShort.techAttributes()

#data = vidShort.videoRead()
#serializer.toJson(data)
#visualize.visMSE(data)

#if __name__ == "__main__":
#    mediaLogic().run()