# standard libraries
from pathlib import Path

# personal files
from filereader import get_data
import plot_vals as plt

if __name__ == '__main__':
    ##################################################
    #    SPECIFY DATA SOURCE FOLDER AND FILE LIST    #
    ##################################################

    data_folder = Path("2023-fall")
    file_list = ['2023-10-21_1250-1.csv', '2023-10-21_1250-2.csv', '2023-10-21_1250-3.csv', '2023-10-21_1250-4.csv']

    data = get_data(file_list, data_folder)
    print(data)

    # plt.plot_race_summary(data[0], Title="2023/10/18 1900m Time Trial")
    # plt.plot_race_summary(data[1], Title="2023/10/18 2000m Time Trial")

    plt.plot_per_stroke_data_multifile(data, "split")