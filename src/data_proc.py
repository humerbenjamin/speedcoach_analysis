# 
import numpy as np

# Rowing and Speedcoach Specific Functions
def smooth_rate(rate_arr):
    arr = np.array(rate_arr)
    sd = np.std(arr)
    mean = np.mean(arr)
    print(sd, mean)
    for i in range(len(arr)-2):
        if i < 2:
            if abs(arr[i]) > mean + 5*sd:
                arr[i] = mean
        else:
            interp_rate = (arr[i-1] + arr[i-2] + arr[i+1] + arr[i+2])/4
            if arr[i] > 45 or arr[i] < 25:
                arr[i] = mean
    return arr, mean, sd




# General Helper Functions
def make_float(L):
    for i in range(len(L)):
        L[i] = float(L[i])
    return L

def make_float_time(L):
    cutoff = 160
    for i in range(len(L)):
        print(L[i])
        L[i] = [float(L[i][0:2]), float(L[i][3:5]), float(L[i][6:])]
        L[i] = HMS_to_sec(L[i])
    for i in range(len(L)):
        if L[i] > cutoff:
            L[i] = cutoff
    for i in range(len(L)):
        L[i] = L[i] // 60 + (L[i] % 60)/100
    return L

def HMS_to_sec(hms):
    seconds = 60*(60*hms[0]+hms[1])+hms[2]
    return seconds



##########################################################
#                                                        #
#    Helper Functions for Polished Plotting Functions    #
#                                                        #
##########################################################

def get_dist_data(data):
    dist_arr = data[2].Distance_GPS
    dist_arr = make_float(dist_arr)
    return dist_arr

def get_split_data(data):
    data1 = data[2].Split_GPS
    split_arr = make_float_time(data1)
    np_split = np.array(split_arr)
    mean_split = make_float_time([data[0].Avg_Split_GPS])[0]
    sd_split = np.std(np_split)
    return split_arr, mean_split, sd_split

def get_rate_data(data):
    data2 = data[2].Stroke_Rate
    data2 = make_float(data2)
    rate_arr, mean_rate, sd_rate = smooth_rate(data2)
    mean_rate = float(data[0].Avg_Stroke_Rate)
    return rate_arr, mean_rate, sd_rate