import matplotlib

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

from csv import reader
from glob import glob
from os import chdir
from os.path import abspath, dirname

EXIT_SUCCESS, EXIT_FAILURE = 0, 1

PROJECT_ROOT = abspath(dirname(__file__))


class Plotter:

    @staticmethod
    def _get_all_csv_files_in_dir(target_dir):
        """
        Retrieves a list of csv files in a certain directory.
        :type target_dir: target dir to search csv files in.
        :return:
        """
        chdir(target_dir)
        result = glob("*.csv")

        return result

    def plot_and_show_all_plot_files(self, target_dir):
        """
        Plots and shows all csv files in current directory.
        :type target_dir: target dir to search csv files in.
        :return:
        """
        for csv_file in self._get_all_csv_files_in_dir(target_dir):
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
            plt.show()

        return EXIT_SUCCESS

    def plot_and_save_all_plot_files(self, target_dir):
        """
        Plots and saves all plot files in current directory.
        :type target_dir: target dir to search csv files in.
        :return:
        """
        i = 0
        for csv_file in self._get_all_csv_files_in_dir(target_dir):
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
            plt.plot(x, y, label='Supposed Stock of {}'.format(str(csv_file)))
            plt.savefig("Figure-{}.png".format(i))
            i += 1
            plt.clf()

        return EXIT_SUCCESS
