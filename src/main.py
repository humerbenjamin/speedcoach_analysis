from pathlib import Path
from filereader import get_data

if __name__ == '__main__':
    data_folder = Path("data-2023")
    print(data_folder)
    a, b, c = get_data(["test.csv"], data_folder)
    print(b.Interval)