# standard libraries
from pathlib import Path

# personal files
from filereader import get_data
from plot_vals import plot_per_stroke_data_onefile
from plot_vals import plot_per_stroke_data_multifile
from plot_vals import plot_interval_summaries

if __name__ == '__main__':
    data_folder = Path("data-2023")
    print(data_folder)
    a, b, c = get_data(["2023-04-08_3-2k_1.csv"], data_folder)
    d, e, f = get_data(["2023-04-08_3-2k_2.csv"], data_folder)
    print(b.Total_Strokes)
    plot_per_stroke_data_multifile([c, f], "stroke rate")