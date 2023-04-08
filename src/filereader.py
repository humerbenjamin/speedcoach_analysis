from pathlib import Path

from classes import session_summary, interval_summary, per_stroke_data

def get_data(filenames, data_folder):
    for name in filenames:
        file_to_open = data_folder / name
        f = open(file_to_open)
        lines = f.readlines()
        cycle = 0
        for line in lines:
            # state control
            if cycle == 0:
                if line[0:16] == "Session Summary:":
                    cycle = 1
                    space = 0
                elif line[0:19] == "Interval Summaries:":
                    cycle = 2
                    space = 0
                    first = True
                elif line[0:16] == "Per-Stroke Data:":
                    cycle = 3
                    space = 0
                    first = True
            # state 1 commands
            if cycle == 1:
                if space == 4:
                    session_sum = make_session_summary(line)
                    cycle = 0
                space += 1
            # state 2 commands
            if cycle == 2:
                if space == 4:
                    if first:
                        interval_sum = initialize_interval_summary()
                        interval_sum = add_additional_interval(interval_sum, line)
                        first = False
                    else:
                        if interval_sum.Interval[-1] == session_sum.Total_Intervals:
                            cycle = 0
                        else:
                            interval_sum = add_additional_interval(interval_sum, line)
                else:
                    space += 1
            # state 3 commands
            if cycle == 3:
                if space == 4:
                    if first:
                        per_s_data = initialize_per_stroke_data()
                        per_s_data = add_additional_stroke(per_s_data, line)
                        first = False
                    else:
                        per_s_data = add_additional_stroke(per_s_data, line)
                        if line == lines[-1]:
                            return session_sum, interval_sum, per_s_data
                else:
                    space += 1

        
        
        # for i in range(3):
        #     print(lines[i+11])



# HELPER FUNCTIONS

def get_Total_Intervals(line):
    i = 0
    letter = line[i]
    Total_Intervals = ""
    while letter != ",":
        Total_Intervals += letter
        i += 1
        letter = line[i]
    return Total_Intervals, (i + 1)

def get_nextval(line, i):
    letter = line[i]
    next_val = ""
    while letter != ",":
        next_val += letter
        i += 1
        letter = line[i]
    return next_val, (i + 1)

def get_lastval(line, i):
    last_val = line[i:]
    return last_val

def make_session_summary(line):
    Total_Intervals, i = get_Total_Intervals(line)
    Total_Distance_GPS, i = get_nextval(line, i)
    Total_Distance_IMP, i = get_nextval(line, i)
    Total_Elapsed_Time, i =  get_nextval(line, i)
    Avg_Split_GPS, i = get_nextval(line, i)
    Avg_Speed_GPS, i = get_nextval(line, i)
    Avg_Split_IMP, i = get_nextval(line, i)
    Avg_Speed_IMP, i = get_nextval(line, i)
    Avg_Stroke_Rate, i = get_nextval(line, i)
    Total_Strokes, i = get_nextval(line, i)
    Distance_Stroke_GPS, i = get_nextval(line, i)
    Distance_Stroke_IMP, i = get_nextval(line, i)
    Avg_Heart, i = get_nextval(line, i)
    Avg_Power, i = get_nextval(line, i)
    Avg_Catch, i = get_nextval(line, i)
    Avg_Slip, i = get_nextval(line, i)
    Avg_Finish, i = get_nextval(line, i)
    Avg_Wash, i = get_nextval(line, i)
    Avg_Force_Avg, i = get_nextval(line, i)
    Avg_Work, i = get_nextval(line, i)
    Avg_Force_Max, i = get_nextval(line, i)
    Avg_Max_Force_Angle, i = get_nextval(line, i)
    Start_GPS_Lat, i = get_nextval(line, i)
    Start_GPS_Lon = get_lastval(line, i)
    session_sum = session_summary(Total_Intervals, Total_Distance_GPS, Total_Distance_IMP, Total_Elapsed_Time, Avg_Split_GPS, Avg_Speed_GPS, Avg_Split_IMP, Avg_Speed_IMP, Avg_Stroke_Rate, Total_Strokes, Distance_Stroke_GPS, Distance_Stroke_IMP, Avg_Heart, Avg_Power, Avg_Catch, Avg_Slip, Avg_Finish, Avg_Wash, Avg_Force_Avg, Avg_Work, Avg_Force_Max, Avg_Max_Force_Angle, Start_GPS_Lat, Start_GPS_Lon)
    return session_sum

def initialize_interval_summary():
    interval_sum = interval_summary([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
    return interval_sum

def add_additional_interval(interval_sum, line):
    Interval, i = get_Total_Intervals(line)
    Total_Distance_GPS, i = get_nextval(line, i)
    Total_Distance_IMP, i = get_nextval(line, i)
    Total_Elapsed_Time, i =  get_nextval(line, i)
    Avg_Split_GPS, i = get_nextval(line, i)
    Avg_Speed_GPS, i = get_nextval(line, i)
    Avg_Split_IMP, i = get_nextval(line, i)
    Avg_Speed_IMP, i = get_nextval(line, i)
    Avg_Stroke_Rate, i = get_nextval(line, i)
    Total_Strokes, i = get_nextval(line, i)
    Distance_Stroke_GPS, i = get_nextval(line, i)
    Distance_Stroke_IMP, i = get_nextval(line, i)
    Avg_Heart, i = get_nextval(line, i)
    Avg_Power, i = get_nextval(line, i)
    Avg_Catch, i = get_nextval(line, i)
    Avg_Slip, i = get_nextval(line, i)
    Avg_Finish, i = get_nextval(line, i)
    Avg_Wash, i = get_nextval(line, i)
    Avg_Force_Avg, i = get_nextval(line, i)
    Avg_Work, i = get_nextval(line, i)
    Avg_Force_Max, i = get_nextval(line, i)
    Avg_Max_Force_Angle, i = get_nextval(line, i)
    Start_GPS_Lat, i = get_nextval(line, i)
    Start_GPS_Lon = get_lastval(line, i)
    (interval_sum.Interval).append(Interval)
    (interval_sum.Total_Distance_GPS).append(Total_Distance_GPS)
    (interval_sum.Total_Distance_IMP).append(Total_Distance_IMP)
    (interval_sum.Total_Elapsed_Time).append(Total_Elapsed_Time)
    (interval_sum.Avg_Split_GPS).append(Avg_Split_GPS)
    (interval_sum.Avg_Speed_GPS).append(Avg_Speed_GPS)
    (interval_sum.Avg_Split_IMP).append(Avg_Split_IMP)
    (interval_sum.Avg_Speed_IMP).append(Avg_Speed_IMP)
    (interval_sum.Avg_Stroke_Rate).append(Avg_Stroke_Rate)
    (interval_sum.Total_Strokes).append(Total_Strokes)
    (interval_sum.Distance_Stroke_GPS).append(Distance_Stroke_GPS)
    (interval_sum.Distance_Stroke_IMP).append(Distance_Stroke_IMP)
    (interval_sum.Avg_Heart).append(Avg_Heart)
    (interval_sum.Avg_Power).append(Avg_Power)
    (interval_sum.Avg_Catch).append(Avg_Catch)
    (interval_sum.Avg_Slip).append(Avg_Slip)
    (interval_sum.Avg_Finish).append(Avg_Finish)
    (interval_sum.Avg_Wash).append(Avg_Wash)
    (interval_sum.Avg_Force_Avg).append(Avg_Force_Avg)
    (interval_sum.Avg_Work).append(Avg_Work)
    (interval_sum.Avg_Force_Max).append(Avg_Force_Max)
    (interval_sum.Avg_Max_Force_Angle).append(Avg_Max_Force_Angle)
    (interval_sum.Start_GPS_Lat).append(Start_GPS_Lat)
    (interval_sum.Start_GPS_Lon).append(Start_GPS_Lon)
    return interval_sum

def initialize_per_stroke_data():
    per_s_data = per_stroke_data([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
    return per_s_data

def add_additional_stroke(per_s_data, line):
    Interval, i = get_Total_Intervals(line)
    Total_Distance_GPS, i = get_nextval(line, i)
    Total_Distance_IMP, i = get_nextval(line, i)
    Total_Elapsed_Time, i =  get_nextval(line, i)
    Avg_Split_GPS, i = get_nextval(line, i)
    Avg_Speed_GPS, i = get_nextval(line, i)
    Avg_Split_IMP, i = get_nextval(line, i)
    Avg_Speed_IMP, i = get_nextval(line, i)
    Avg_Stroke_Rate, i = get_nextval(line, i)
    Total_Strokes, i = get_nextval(line, i)
    Distance_Stroke_GPS, i = get_nextval(line, i)
    Distance_Stroke_IMP, i = get_nextval(line, i)
    Avg_Heart, i = get_nextval(line, i)
    Avg_Power, i = get_nextval(line, i)
    Avg_Catch, i = get_nextval(line, i)
    Avg_Slip, i = get_nextval(line, i)
    Avg_Finish, i = get_nextval(line, i)
    Avg_Wash, i = get_nextval(line, i)
    Avg_Force_Avg, i = get_nextval(line, i)
    Avg_Work, i = get_nextval(line, i)
    Avg_Force_Max, i = get_nextval(line, i)
    Avg_Max_Force_Angle, i = get_nextval(line, i)
    Start_GPS_Lat, i = get_nextval(line, i)
    Start_GPS_Lon = get_lastval(line, i)
    (per_s_data.Interval).append(Interval)
    (per_s_data.Distance_GPS).append(Total_Distance_GPS)
    (per_s_data.Distance_IMP).append(Total_Distance_IMP)
    (per_s_data.Elapsed_Time).append(Total_Elapsed_Time)
    (per_s_data.Split_GPS).append(Avg_Split_GPS)
    (per_s_data.Speed_GPS).append(Avg_Speed_GPS)
    (per_s_data.Split_IMP).append(Avg_Split_IMP)
    (per_s_data.Speed_IMP).append(Avg_Speed_IMP)
    (per_s_data.Stroke_Rate).append(Avg_Stroke_Rate)
    (per_s_data.Total_Strokes).append(Total_Strokes)
    (per_s_data.Distance_Stroke_GPS).append(Distance_Stroke_GPS)
    (per_s_data.Distance_Stroke_IMP).append(Distance_Stroke_IMP)
    (per_s_data.Heart_Rate).append(Avg_Heart)
    (per_s_data.Power).append(Avg_Power)
    (per_s_data.Catch).append(Avg_Catch)
    (per_s_data.Slip).append(Avg_Slip)
    (per_s_data.Finish).append(Avg_Finish)
    (per_s_data.Wash).append(Avg_Wash)
    (per_s_data.Force_Avg).append(Avg_Force_Avg)
    (per_s_data.Work).append(Avg_Work)
    (per_s_data.Force_Max).append(Avg_Force_Max)
    (per_s_data.Max_Force_Angle).append(Avg_Max_Force_Angle)
    (per_s_data.GPS_Lat).append(Start_GPS_Lat)
    (per_s_data.GPS_Lon).append(Start_GPS_Lon)
    return per_s_data

# a, b, c = get_data(['test2.csv'])
# print(c)