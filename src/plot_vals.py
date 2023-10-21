# standard libraries
import matplotlib.pyplot as plt
import numpy as np

# other files
from classes import session_summary, interval_summary, per_stroke_data
import data_proc as dp
from data_proc import make_float, make_float_time, smooth_rate

# plot summary multifile
def plot_summary_multifile(data_arr, type, plotavg=False):
    L = []
    if plotavg:
        L.append("Average Split Across All Pieces")
        sum = 0
        for i in range(len(data_arr)):
            sum += make_float_time([data_arr[i][0].Avg_Split_GPS])[0]
        avg = sum / len(data_arr)
        plt.axhline(avg, color='r')
    interval_summaries = []
    for i in range(len(data_arr)):
        interval_summaries.append(data_arr[i][0])
    if type == "split":
        avg_splits = []
        for interval in interval_summaries:
            avg_splits.append(interval.Avg_Split_GPS)
        graph_1line(y=avg_splits, title="Split over Different Pieces", xlabel="Piece Number", ylabel="Average Split", type="split", first=True, last=True, plotavg=plotavg)
    L.append("Average Split in Each Individual Piece")
    plt.legend(L)
    plt.show()


# plotting interval summary
def plot_interval_summaries(interval_summary, type):
    if type == "stroke rate":
        graph_interval_avg(y=interval_summary.Avg_Stroke_Rate, title="Stroke Rate over each Interval", xlabel="Interval Number", ylabel="Stroke Rate")
    elif type == "split":
        graph_interval_avg(y=interval_summary.Avg_Split_GPS, title="Split over each Interval", xlabel="Interval Number", ylabel="Split")


def graph_interval_avg(y, x = [], title = "", xlabel="", ylabel="", type=""):
    if type == "split":
        y = make_float_time(y)
    else:
        y = make_float(y)
    for i in range(len(y)):
        x.append(i + 1)
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
    return


# plotting per stroke data
def plot_per_stroke_data_onefile(per_stroke_data, type, type2="stroke number"):
    if type == "stroke rate":
        graph_1line(y=per_stroke_data.Stroke_Rate, title="Stroke Rate at each Stroke", xlabel="Stroke Number", ylabel="Stroke Rate", type="stroke rate", first=True, last=True)
    elif type == "split":
        graph_1line(y=per_stroke_data.Split_GPS, title="Split at each Stroke", xlabel="Stroke Number", ylabel="Split", type="split", first=True, last=True)
    elif type == "heart rate":
        graph_1line(y=per_stroke_data.Heart_Rate, title="Heart Rate at Each Stroke", xlabel="Stroke Number", ylabel="Heart Rate", type="heart rate", first=True, last=True)


def plot_per_stroke_data_multifile(per_stroke_data_L, type, hline=False):
    # stroke rate
    if type == "stroke rate":
        for i in range(len(per_stroke_data_L)):
            if i == 0:
                graph_1line(y=per_stroke_data_L[i].Stroke_Rate, title="Stroke Rate at each Stroke", xlabel="Stroke Number", ylabel="Stroke Rate", type="stroke rate", first=True)
            elif i == (len(per_stroke_data_L)-1):
                graph_1line(y=per_stroke_data_L[i].Stroke_Rate, last=True, type="stroke rate")
            else:
                graph_1line(y=per_stroke_data_L[i].Stroke_Rate, type="stroke rate")
    # split
    elif type == "split":
        for i in range(len(per_stroke_data_L)):
            if i == 0:
                graph_1line(y=per_stroke_data_L[i][2].Split_GPS, title="Split at each Stroke", xlabel="Stroke Number", ylabel="Split", type="split", first=True, i=i, hline=hline)
            elif i == (len(per_stroke_data_L)-1):
                graph_1line(y=per_stroke_data_L[i][2].Split_GPS, last=True, type="split", i=i)
            else:
                graph_1line(y=per_stroke_data_L[i][2].Split_GPS, type="split", i=i)
    # heart rate
    elif type == "heart rate":
        for i in range(len(per_stroke_data_L)):
            if i == 0:
                graph_1line(y=per_stroke_data_L[i].Heart_Rate, title="Heart Rate at each Stroke", xlabel="Stroke Number", ylabel="Heart Rate", type="heart rate", first=True, i=i)
            elif i == (len(per_stroke_data_L)-1):
                graph_1line(y=per_stroke_data_L[i].Heart_Rate, last=True, type="heart rate", i=i)
            else:
                graph_1line(y=per_stroke_data_L[i].Heart_Rate, type="heart rate", i=i)



def graph_1line(y, title = "", xlabel="", ylabel="", type="", first=False, last=False, i=0, hline=False, plotavg=False):
    x = []
    L = []
    if type == "split":
        y = make_float_time(y)
    else:
        y = make_float(y)
    for i in range(len(y)):
        x.append(i + 1)

    if plotavg:
        L.append("Average Pace")

    if (hline != False) and first:
            plt.axhline(y = hline, color = 'r')
    plt.plot(x, y)

    if first:
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
    if last:
        for j in range(i):
            L.append("Piece "+ str(j+1))
        plt.legend(L)
    return
        




###########################################
#                                         #
#    Final Polished Plotting Functions    #
#                                         #
###########################################

def plot_race_summary(data, Title="Race Summary"):
    # process and prepare distance data
    dist_arr = dp.get_dist_data(data)

    # process and prepare splot data
    split_arr, mean_split, sd_split = dp.get_split_data(data)
    
    # process and prepare rate data
    rate_arr, mean_rate, sd_rate = dp.get_rate_data(data)

    # get arrays for mean splits
    mean_split_arr = []
    mean_rate_arr = []
    for i in range(len(rate_arr)):
        mean_split_arr.append(mean_split)
        mean_rate_arr.append(mean_rate)

    # set up plots
    fig, ax1 = plt.subplots()

    # plot split
    color = 'tab:red'
    ax1.set_xlabel('Distance (m)')
    ax1.set_ylabel('Split (min.sec/500m)')
    ax1.plot(dist_arr, split_arr, color=color)
    # ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim([mean_split/2, max(split_arr[5:] + 1.5*sd_split)])
    ax1.plot(dist_arr, mean_split_arr, "--", color=color)

    # set up second axis
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    # plot stroke rate
    color = 'tab:blue'
    ax2.set_ylabel('Stroke Rate (s/min)')  # we already handled the x-label with ax1
    ax2.plot(dist_arr, rate_arr, color=color)
    ax2.set_ylim([min(rate_arr[5:]) - 1,max(rate_arr)+2.5*sd_rate])
    ax2.plot(dist_arr, mean_rate_arr, "--", color=color)

    # Full Figure Settings
    fig.legend(["Split", "Average Split: " + str(mean_split)[:6], "Rate: " + str(mean_rate)[:6], "Average Rate"])    
    ax1.set_title(Title)
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()
    return

def plot_multipieces_stroke_by_stroke(data_arr, Title=""):
    dist_arrs = []
    split_arrs = []
    rate_arrs = []
    # get all the data
    for i in range(len(data_arr)):
        data = data_arr[i]
        # process and prepare distance, split, and rate data
        dist_arr = dp.get_dist_data(data)
        split_arr, mean_split, sd_split = dp.get_split_data(data)        
        rate_arr, mean_rate, sd_rate = dp.get_rate_data(data)

        # append to arrays of data
        dist_arrs.append(dist_arr)
        split_arrs.append([split_arr, mean_split, sd_split])
        rate_arrs.append([rate_arr, mean_rate, sd_rate])

    # 

    # plot splits
    for i in range(len(split_arrs)):
        
    return