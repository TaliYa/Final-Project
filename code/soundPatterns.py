import scipy.io.wavfile as wavfile

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

array = calc_distances('./shots1.wav') 
print (array)
print(len(array))



#comparing the files
def accept_test(pattren, test, min_error):
    if len(pattern) > len(test):
        return False
    for i, dt in enumerate(pattren):
        if not dt - test[i] < min_error:
            return False
        
    return True
pattern = calc_distances('./shots1.wav')
test = calc_distances('./shots1.wav')

min_error = 0.1
print (accept_test(pattern, test, min_error))
      




