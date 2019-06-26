from csv import reader
from glob import glob
from os import chdir
from os.path import abspath, dirname

import matplotlib.pyplot as plt

EXIT_SUCCESS, EXIT_FAILURE = 0, 1

PROJECT_ROOT = abspath(dirname(__file__))


def get_all_csv_files_in_dir(target_dir):
    """
    Retrieves a list of csv files in a certain directory.
    :return:
    """
    chdir(target_dir)
    result = glob("*.csv")

    return result


def plot_and_show_all_csv_files():
    """
    Plots and shows all csv files in current directory.
    :return:
    """
    for csv_file in get_all_csv_files_in_dir("."):
        x, y = [], []

        with open(csv_file, 'r') as csvfile:
            plots = reader(csvfile, delimiter=';')
            next(plots, None)
            for row in plots:
                x.append(row[0][0:-10])
                y.append(int(row[1]))

        plt.plot(x, y, label='Supposed Stock of {}'.format(str(csv_file)))
        plt.xlabel('date')
        plt.xticks(rotation=35, fontsize=5)
        plt.ylabel('items')
        plt.title('Plot: {}'.format(str(csv_file)))
        plt.legend()
        plt.show()

    return EXIT_SUCCESS


def main():
    plot_and_show_all_csv_files()


if __name__ == '__main__':
    main()
