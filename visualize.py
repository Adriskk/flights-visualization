# -*- coding: utf-8 -*-

""" Description: visualize file - shows the map with current flights up the US """

# => 3-RD PARTY IMPORTS
# from mpl_toolkits.basemap import Basemap
# import matplotlib.pyplot as plt
# import numpy as np
# import time
# from IPython.display import HTML, display
# import webbrowser
# import io


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
