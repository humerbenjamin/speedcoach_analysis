# 

def make_float(L):
    for i in range(len(L)):
        L[i] = float(L[i])
    return L

def make_float_time(L):
    cutoff = 180
    for i in range(len(L)):
        L[i] = [float(L[i][0:2]), float(L[i][3:5]), float(L[i][6:])]
        L[i] = HMS_to_sec(L[i])
    for i in range(len(L)):
        if L[i] > cutoff:
            L[i] = cutoff
    return L

def HMS_to_sec(hms):
    seconds = 60*hms[1]+hms[2]
    return seconds
    