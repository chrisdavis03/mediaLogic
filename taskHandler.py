import schedule
import time
import db_util
from ffService import MediaEngine


def claimTask():
    queued_data = db_util.selectQueued()


    #claim the first task in the queue
    if len(queued_data) > 0:
        job_data = queued_data[0]

        if job_data['taskType'] == 'initiate':
            print ("initiate job found")
            db_util.claimTask(job_data['taskID'])
            db_util.printTask(job_data['taskID'])

            mediaHandler(job_data['fileResource'])

            db_util.completeTask(job_data['taskID'])
            db_util.printTask(job_data['taskID'])

        if job_data['taskType'] == 'encode':
            print("encode job found")
            encode = MediaEngine(job_data['fileResource'])
            encode.encodeVideo()
            db_util.completeTask(job_data['taskID'])

    else:
        print ('No queued Tasks')


def mediaHandler(fileInput):
    media = MediaEngine(fileInput)

    media.metaExtract()


schedule.every(10).seconds.do(claimTask)

while True:
    schedule.run_pending()
    time.sleep(1)