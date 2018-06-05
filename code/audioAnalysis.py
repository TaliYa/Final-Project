from scipy.io import wavfile
import numpy as np
#import matplotlib.pyplot as plt
import platform
import time
import os

constLimit = 500
arrayPattern = []

sampFreq, data = wavfile.read('./shots1.wav')
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
'''
timeArray = np.arange(0, dataLength, 1) # 5292 נקודות שיש למידע בקובץ
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000  #scale to milliseconds


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
    
    if time < START_TIME and time > END_TIME:
        return True
    else:
        return False


# function to check anomalous audio
def check_normal(anomalyParams["month"]) and check_day(anomalyParams["day"]) and check_time(anomalyParams["time"]):
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


def calc_distances(sound_file):
    
    fs, data = wavfile.read(sound_file)
    #print(data)
    data_size = len(data)

    min_val = 250
    print(fs)
    focus_size = int(0.15*fs)
    
    print(focus_size)

    focuses = [] # critical point 
    distances = [] # distances between the criticsl points
    idx = 0

    while idx < len(data):
        if data[idx] > min_val:
            mean_idx = idx + focus_size // 2
            focuses.append(float(mean_idx)/data_size)
            if len(focuses) > 1:
                last_focus = focuses[-2]
                actual_focus = focuses[-1]
                distances.append(actual_focus - last_focus)
            idx+=focus_size
        else:
            idx+=1
    return distances

#comparing the files
def accept_test(pattren, test, min_error):
    if len(pattern) > len(test):
        return False
    for i, dt in enumerate(pattren):
        if not dt - test[i] < min_error:
            return False
        
    return True
         
    
fileDateCreation = time.ctime(file_creation_date('./shots1.wav'))
arrayDate = fileDateCreation.split(" ")
fileCreationDay = arrayDate[0]  #day
fileCreationMonth = arrayDate[1] #month
fileCreationYear = arrayDate[5] #year
fileCreationTime = arrayDate[4] #time
print(arrayDate)
#print(fileCreationDay)
#print(fileCreationYear)

# מערך של פרמטרים לבדיקת אנומאליות הקול
objAnomalyParams = {"month":fileCreationMonth,
                    "day":fileCreationDay,
                    "time":fileCreationTime}

pattern = calc_distances('./shots1.wav')    
#arrayPattern.append(pattern)
min_error = 0.1
for patternItem in arrayPattern:
    if accept_test(pattern, patternItem, min_error)):
        print('buum')


if !check_normal(objAnomalyParams):
    # לולאה שרצה על הערכים ומוצאת את הגבוהים מLIMIT
    for audioPoint in data:
       # if audioPoint > constLimit:
            arrayPattern.append(pattern)
            print("bumm")
            break



