from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import os
import cmath
import random
from numpy import fft as fft
import scikits.audiolab as audio


constLimit = 500
arrayPattern = []

sampFreq, data = wavfile.read('./s-y.wav')
print(sampFreq) #rate
#data = data / (2.**15)  # ממפים את הטונים לטווח מסויים

dataLength = len(data)
channel = data[:0] # נשתמש בערוץ אחד
n = len(channel)

timeArray = np.arange(0, dataLength, 1) # 5292 נקודות שיש למידע בקובץ
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000  #scale to milliseconds

#fftData = fft.fft(channel)

# שרטוט המידע - דיאגרמה 
#plt.plot(timeArray, data, color='k') 
plt.plot(fftData, color='k')
plt.ylabel('Amplitude')
plt.xlabel('Time (ms)')
plt.show()



def check_month(month):
    '''
    Cheack if the file creation month is normal
    If the month is July or August
    '''
    START_MONTH = "July"
    END_MONTH = "August"
    if month is START_MONTH or month is END_MONTH:
        return False
    else:
        print("true")
        return True


def check_day(day):
    '''
    Cheack if the file creation day is normal
    If the day is Saturday 
    '''
    DAY = "Saturday"
    if day is DAY:
        return False
    else:
        print("true")
        return True


def check_time(time):
    '''
    Cheack if the file creation time is normal
    '''
    START_TIME = "20:00:00"
    END_TIME = "07:00:00"
    
    if time < START_TIME and time > END_TIME:
        return True
    else:
        return False


def check_normal(anomalyParams):
    '''
    Check anomalous of audio parameters
    '''
    if check_month(anomalyParams["month"]) and check_day(anomalyParams["day"]) and check_time(anomalyParams["time"]):
        return True
            
               
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
    '''
    Calculate the distances between criticsl points in an audio file
    '''
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


def compare_patterns(pattren, test, min_error):
    '''
    Compare between 2 patterns off files audio 
    '''
    if len(pattern) > len(test):
        return False
    for i, dt in enumerate(pattren):
        if not dt - test[i] < min_error:
            return False       
    return True
         


'''
P R O C E S S 
'''

# creat a pattern from the audio file
pattern = calc_distances('./s-y.wav')    

min_error = 0.1
for patternItem in arrayPattern:
    '''
    checks whether the pattern matches an existing pattern
    '''
    if compare_patterns(pattern, patternItem, min_error):
        print('the pattern match to existing pattren')

'''
checks anothers parameters of the audio file to check anomaly:
year, month, day, time...
'''
fileDateCreation = time.ctime(file_creation_date('./shots1.wav')) # get the date creation of the audio file

arrayDate = fileDateCreation.split(" ")
fileCreationDay = arrayDate[0]  #day
fileCreationMonth = arrayDate[1] #month
fileCreationYear = arrayDate[5] #year
fileCreationTime = arrayDate[4] #time
print(arrayDate)

# array of parameters for check the anomaly of sound
objAnomalyParams = {"month":fileCreationMonth,
                    "day":fileCreationDay,
                    "time":fileCreationTime}

if !check_normal(objAnomalyParams):
    # if the parameters do not meet the normal audio conditions 
    for audioPoint in data:
       # if audioPoint > constLimit:
            arrayPattern.append(pattern)
            print("bumm")
            break
