class session_summary:
    def __init__(self, Total_Intervals, Total_Distance_GPS, Total_Distance_IMP, Total_Elapsed_Time, Avg_Split_GPS, Avg_Speed_GPS, Avg_Split_IMP, Avg_Speed_IMP, Avg_Stroke_Rate, Total_Strokes, Distance_Stroke_GPS, Distance_Stroke_IMP, Avg_Heart, Avg_Power, Avg_Catch, Avg_Slip, Avg_Finish, Avg_Wash, Avg_Force_Avg, Avg_Work, Avg_Force_Max, Avg_Max_Force_Angle, Start_GPS_Lat, Start_GPS_Lon):
        self.Total_Intervals = Total_Intervals
        self.Total_Distance_GPS = Total_Distance_GPS
        self.Total_Distance_IMP = Total_Distance_IMP
        self.Total_Elapsed_Time = Total_Elapsed_Time
        self.Avg_Split_GPS = Avg_Split_GPS
        self.Avg_Speed_GPS = Avg_Speed_GPS
        self.Avg_Split_IMP = Avg_Split_IMP
        self.Avg_Speed_IMP = Avg_Speed_IMP
        self.Avg_Stroke_Rate = Avg_Stroke_Rate
        self.Total_Strokes = Total_Strokes
        self.Distance_Stroke_GPS = Distance_Stroke_GPS
        self.Distance_Stroke_IMP = Distance_Stroke_IMP
        self.Avg_Heart = Avg_Heart
        self.Avg_Power = Avg_Power
        self.Avg_Catch = Avg_Catch
        self.Avg_Slip = Avg_Slip
        self.Avg_Finish = Avg_Finish
        self.Avg_Wash = Avg_Wash
        self.Avg_Force_Avg = Avg_Force_Avg
        self.Avg_Work = Avg_Work
        self.Avg_Force_Max = Avg_Force_Max
        self.Avg_Max_Force_Angle = Avg_Max_Force_Angle
        self.Start_GPS_Lat = Start_GPS_Lat
        self.Start_GPS_Lon = Start_GPS_Lon

class interval_summary:
    def __init__(self, Interval, Total_Distance_GPS, Total_Distance_IMP, Total_Elapsed_Time, Avg_Split_GPS, Avg_Speed_GPS, Avg_Split_IMP, Avg_Speed_IMP, Avg_Stroke_Rate, Total_Strokes, Distance_Stroke_GPS, Distance_Stroke_IMP, Avg_Heart, Avg_Power, Avg_Catch, Avg_Slip, Avg_Finish, Avg_Wash, Avg_Force_Avg, Avg_Work, Avg_Force_Max, Avg_Max_Force_Angle, Start_GPS_Lat, Start_GPS_Lon):
        self.Interval = Interval
        self.Total_Distance_GPS = Total_Distance_GPS
        self.Total_Distance_IMP = Total_Distance_IMP
        self.Total_Elapsed_Time = Total_Elapsed_Time
        self.Avg_Split_GPS = Avg_Split_GPS
        self.Avg_Speed_GPS = Avg_Speed_GPS
        self.Avg_Split_IMP = Avg_Split_IMP
        self.Avg_Speed_IMP = Avg_Speed_IMP
        self.Avg_Stroke_Rate = Avg_Stroke_Rate
        self.Total_Strokes = Total_Strokes
        self.Distance_Stroke_GPS = Distance_Stroke_GPS
        self.Distance_Stroke_IMP = Distance_Stroke_IMP
        self.Avg_Heart = Avg_Heart
        self.Avg_Power = Avg_Power
        self.Avg_Catch = Avg_Catch
        self.Avg_Slip = Avg_Slip
        self.Avg_Finish = Avg_Finish
        self.Avg_Wash = Avg_Wash
        self.Avg_Force_Avg = Avg_Force_Avg
        self.Avg_Work = Avg_Work
        self.Avg_Force_Max = Avg_Force_Max
        self.Avg_Max_Force_Angle = Avg_Max_Force_Angle
        self.Start_GPS_Lat = Start_GPS_Lat
        self.Start_GPS_Lon = Start_GPS_Lon

class per_stroke_data:
    def __init__(self, Interval, Distance_GPS, Distance_IMP, Elapsed_Time, Split_GPS, Speed_GPS, Split_IMP, Speed_IMP, Stroke_Rate, Total_Strokes, Distance_Stroke_GPS, Distance_Stroke_IMP, Heart_Rate, Power, Catch, Slip, Finish, Wash, Force_Avg, Work, Force_Max, Max_Force_Angle, GPS_Lat, GPS_Lon):
        self.Interval = Interval
        self.Distance_GPS = Distance_GPS
        self.Distance_IMP = Distance_IMP
        self.Elapsed_Time = Elapsed_Time
        self.Split_GPS = Split_GPS
        self.Speed_GPS = Speed_GPS
        self.Split_IMP = Split_IMP
        self.Speed_IMP = Speed_IMP
        self.Stroke_Rate = Stroke_Rate
        self.Total_Strokes = Total_Strokes
        self.Distance_Stroke_GPS = Distance_Stroke_GPS
        self.Distance_Stroke_IMP = Distance_Stroke_IMP
        self.Heart_Rate = Heart_Rate
        self.Power = Power
        self.Catch = Catch
        self.Slip = Slip
        self.Finish = Finish
        self.Wash = Wash
        self.Force_Avg = Force_Avg
        self.Work = Work
        self.Force_Max = Force_Max
        self.Max_Force_Angle = Max_Force_Angle
        self.GPS_Lat = GPS_Lat
        self.GPS_Lon = GPS_Lon