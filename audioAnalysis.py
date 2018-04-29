from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt 

CONST_LIMIT = 0.5 #הגבול לערכים בנורמה

sampFreq, data = wavfile.read('./outExpFinal.wav')
print(data)
print(data.dtype) #ייצוג המידע מהקובץ
print(sampFreq) #קצב
data = data / (2.**15)  # ממפים את הטונים לטווח מסויים
data = data[0:200000]
#print(data[10000:400000])
#print(len(data))
#print(data.shape)
#channel = data[:] # נשתמש בערוץ אחד
#print(channel)

timeArray = np.arange(0, 595968, 1) # 5292 נקודות שיש למידע בקובץ
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000  #scale to milliseconds

'''
# שרטוט המידע - דיאגרמה 
plt.plot(timeArray, data, color='k') 
plt.ylabel('Amplitude')
plt.xlabel('Time (ms)')
plt.show()
'''

# לולאה שרצה על הערכים ומוצאת את הגבוהים מLIMIT
for audioPoint in data:
    if audioPoint > CONST_LIMIT:
        print("bumm")
        break



