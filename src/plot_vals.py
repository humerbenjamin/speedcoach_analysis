# standard libraries
import matplotlib.pyplot as plt

# other files
from classes import session_summary, interval_summary, per_stroke_data
from data_proc import make_float
from data_proc import make_float_time

# plotting interval summary
def plot_interval_summaries(interval_summary, type):
    if type == "stroke rate":
        graph_interval_avg(y=interval_summary.Avg_Stroke_Rate, title="Stroke Rate over each Interval", xlabel="Interval Number", ylabel="Stroke Rate")



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
def plot_per_stroke_data_onefile(per_stroke_data, type):
    if type == "stroke rate":
        graph_1line(y=per_stroke_data.Stroke_Rate, title="Stroke Rate at each Stroke", xlabel="Stroke Number", ylabel="Stroke Rate", type="stroke rate", first=True, last=True)
    elif type == "split":
        graph_1line(y=per_stroke_data.Split_GPS, title="Split at each Stroke", xlabel="Stroke Number", ylabel="Split", type="split", first=True, last=True)
    elif type == "heart rate":
        graph_1line(y=per_stroke_data.Heart_Rate, title="Heart Rate at Each Stroke", xlabel="Stroke Number", ylabel="Heart Rate", type="heart rate", first=True, last=True)


def plot_per_stroke_data_multifile(per_stroke_data_L, type):
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
                graph_1line(y=per_stroke_data_L[i].Split_GPS, title="Split at each Stroke", xlabel="Stroke Number", ylabel="Split", type="split", first=True)
            elif i == (len(per_stroke_data_L)-1):
                graph_1line(y=per_stroke_data_L[i].Split_GPS, last=True, type="split")
            else:
                graph_1line(y=per_stroke_data_L[i].Split_GPS, type="split")


def graph_1line(y, title = "", xlabel="", ylabel="", type="", first=False, last=False):
    x = []
    if type == "split":
        y = make_float_time(y)
    else:
        y = make_float(y)
    for i in range(len(y)):
        x.append(i + 1)
    plt.plot(x, y)

    if first:
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
    if last:
        plt.show()
        