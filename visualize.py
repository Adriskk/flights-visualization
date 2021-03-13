# -*- coding: utf-8 -*-


__author__ = 'Adison'
__date__ = '13.03.2021'
__description__ = 'Flights visualization project ' \
                  'coded for TIMATHON 2021 (Theme: VISUALIZATION).' \
                  'The project shows a USA map with plane markers' \
                  '- using OpenSky API to get air crafts data.'

# => IMPORTS
from window import *


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

