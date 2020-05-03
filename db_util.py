import sqlite3
import json

def createTable():
    conn = sqlite3.connect('mediaDB.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE tasks
             (task_id VARCHAR(36), task_status VARCHAR(100), task_type VARCHAR(100), file_resource VARCHAR(255))''')

    conn.commit()
    conn.close()

def deleteTable():
    conn = sqlite3.connect('mediaDB.db')
    c = conn.cursor()

    c.execute('''DROP TABLE tasks;''')

    conn.commit()
    conn.close()

def selectAll():
    conn = sqlite3.connect('mediaDB.db')
    c = conn.cursor()

    c.execute('''SELECT * FROM tasks''')
    data=c.fetchall()

    conn.commit()
    conn.close()

    return data

def selectQueued():
    conn = sqlite3.connect('mediaDB.db')
    c = conn.cursor()

    c.execute('''SELECT * FROM tasks WHERE (task_status = 'queued')''')
    data=c.fetchall()

    queued = []
    for i in data:
        task_dict = {'taskID': i[0], 'status': i[1], 'taskType': i[2], 'fileResource': i[3]}
        queued.append(task_dict)
        print(i)
    conn.commit()
    conn.close()

    return queued

def insertTask(taskID, taskType, fileResource):
    conn = sqlite3.connect('mediaDB.db')
    c = conn.cursor()

    status = 'queued'

    c.execute('''INSERT INTO tasks (task_id, task_status, task_type, file_resource) VALUES (?,?,?, ?)''', (taskID, status, taskType, fileResource))

    conn.commit()
    conn.close()


def claimTask(taskID):
    conn = sqlite3.connect('mediaDB.db')
    c = conn.cursor()

    c.execute('''UPDATE tasks SET task_status = 'claimed' WHERE task_id = ?''',
              (taskID,))

    conn.commit()
    conn.close()

def completeTask(taskID):
    conn = sqlite3.connect('mediaDB.db')
    c = conn.cursor()

    c.execute('''UPDATE tasks SET task_status = 'complete' WHERE task_id = ?''',
              (taskID,))

    conn.commit()
    conn.close()

def removeTask(taskID):
    conn = sqlite3.connect('mediaDB.db')
    c = conn.cursor()

    c.execute('''DELETE FROM tasks WHERE (task_id = ?)''', (taskID,))

    conn.commit()
    conn.close()

def removeAllTasks():
    conn = sqlite3.connect('mediaDB.db')
    c = conn.cursor()

    c.execute('''DELETE FROM tasks''')

    conn.commit()
    conn.close()

def printTask(taskID):
    conn = sqlite3.connect('mediaDB.db')
    c = conn.cursor()

    c.execute('''SELECT * FROM tasks WHERE (task_id = ?)''', (taskID,))
    task = c.fetchall()

    task_dict = {'taskID': task[0][0], 'status': task[0][1], 'taskType': task[0][2], 'fileResource': task[0][3] }
    print (task_dict)
    conn.commit()
    conn.close()
    return task_dict

if __name__ == "__main__":
    selectQueued()

