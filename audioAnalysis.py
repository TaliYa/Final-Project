from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import os

CONST_LIMIT = 0.5 #הגבול לערכים בנורמה

sampFreq, data = wavfile.read('./test1.wav')
print(data)
print(data.dtype) #ייצוג המידע מהקובץ
print(sampFreq) #קצב
data = data / (2.**15)  # ממפים את הטונים לטווח מסויים
#print(data)
#data = data[0:200000]
#print(data[10000:400000])
# len(data) - זה מה שמכניסים ב np.arange
dataLength = len(data)
print(dataLength)
#print(data.shape)
#channel = data[:] # נשתמש בערוץ אחד
#print(channel)

timeArray = np.arange(0, dataLength, 1) # 5292 נקודות שיש למידע בקובץ
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000  #scale to milliseconds

'''
# שרטוט המידע - דיאגרמה 
plt.plot(timeArray, data, color='k') 
plt.ylabel('Amplitude')
plt.xlabel('Time (ms)')
plt.show()

'''


#function to cheack the the file creation month
def check_month(month):
    '''
    If the month is July or August
    '''
    START_MONTH = "July"
    END_MONTH = "August"
    if month is START_MONTH or month is END_MONTH:
        return False
    else:
        print("true")
        return True

#function to cheack the the file creation day
def check_day(day):
    '''
    If the day is Saturday 
    '''
    DAY = "Saturday"
    if day is DAY:
        return False
    else:
        print("true")
        return True

#function to cheack the the file creation time
def check_time(time):
    #print(time.replace(":", ""))
    START_TIME = "20:00:00"
    END_TIME = "07:00:00"
    '''
    if 1:
        return False
    else:'''
    return True


# function to check anomalous audio
def check_anomaly(anomalyParams):
    if check_month(anomalyParams["month"]) and check_day(anomalyParams["day"]) and check_time(anomalyParams["time"]):
        return True
            
               
#function to get the file creation date
def file_creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime
    
    
    
fileDateCreation = time.ctime(file_creation_date('./test1.wav'))
arrayDate = fileDateCreation.split(" ")
fileCreationDay = arrayDate[0]  #day
fileCreationMonth = arrayDate[1] #month
fileCreationYear = arrayDate[4] #year
fileCreationTime = arrayDate[3] #time
print(arrayDate)
#print(fileCreationDay)
#print(fileCreationYear)

# מערך של פרמטרים לבדיקת אנומאליות הקול
objAnomalyParams = {"month":fileCreationMonth,
                    "day":fileCreationDay,
                    "time":fileCreationTime}

if check_anomaly(objAnomalyParams):    
    # לולאה שרצה על הערכים ומוצאת את הגבוהים מLIMIT
    for audioPoint in data:
        if audioPoint > CONST_LIMIT:
            print("bumm")
            break


#  When finished processing - Deletes the file
# os.remove("recordtest.py") - שם הקובץ שיצרנו למעלה
