# -*- coding: utf-8 -*-

__author__ = 'Adison'
__date__ = '13.03.2021'
__description__ = 'App class file'


# => 3-RD PARTY IMPORTS
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QFileDialog, QLabel, QFrame
import io
import datetime
import folium
import sys

# => IMPORTS
from lib import aggregate as ag
from lib import functions as func
from data import *
from lib import extract
from lib import request as req


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1262, 711)
        MainWindow.setStyleSheet("background-color: rgb(238, 94, 0);\n"
                                 "background-color: qlineargradient(spread:pad, x2:2.0508475, y1:0.28, x3:1, "
                                 "y2:1.994, stop:0 rgba(26, 23, 59, 255), stop:1 rgba(238, 94, 0, 255));\n "
                                 "")

        MainWindow.setWindowIcon(QIcon("res/app-icon.png"))
        MainWindow.setFixedSize(WINDOW_WIDTH, WIND0W_HEIGHT)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.headerF = QFrame(self.centralwidget)
        self.headerF.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerF.setGeometry(QtCore.QRect(0, -1, WINDOW_WIDTH+10, 90))
        self.headerF.setStyleSheet("background-color: rgb(255, 255, 255);\n")

        self.label = QtWidgets.QLabel(self.headerF)
        self.label.setGeometry(QtCore.QRect(70, 10, 450, 60))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "font: 24pt \"Montserrat\";\n"
                                 "text-shadow: 10px 10px #1A173B;")

        self.label.setObjectName("label")

        self.pixmap = QLabel(self.headerF)
        self.app_icon = QPixmap('res/header-icon.png')
        self.pixmap.setPixmap(self.app_icon)
        self.pixmap.setGeometry(QtCore.QRect(40, 15, 60, 60))

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(870, 130, 371, 441))
        self.frame.setStyleSheet("background-color: rgb(26, 23, 59);\n"
                                 "border-radius: 15px;")

        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.options = QtWidgets.QLabel(self.frame)
        self.options.setGeometry(QtCore.QRect(0, 0, 371, 61))
        self.options.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 16pt \"Open Sans\";\n"
                                   "\n"
                                   "border-bottom-left-radius: 0px;\n"
                                   "border-bottom-right-radius: 0px;\n"
                                   "\n"
                                   "")

        self.options.setObjectName("options")

        self.stats = QtWidgets.QLabel(self.frame)
        self.stats.setGeometry(QtCore.QRect(0, 190, 371, 61))
        self.stats.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "font: 16pt \"Open Sans\";\n"
                                 "\n"
                                 "border-bottom-left-radius: 0px;\n"
                                 "border-bottom-right-radius: 0px;\n"
                                 "\n"
                                 "")

        self.stats.setObjectName("stats")

        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 80, 241, 88))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.refresh_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.refresh_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.refresh_btn.setStyleSheet("border-radius: 20px;\n"
                                       "background-color: #EE5E00;\n"
                                       "border: solid 2px ;\n"
                                       "border-color: #fff;\n"
                                       "\n"
                                       "color: #fff;\n"
                                       "font-weight: 400;\n"
                                       "\n"
                                       "padding: 10px;\n"
                                       "\n"
                                       "QPushButton#refresh_btn:hover { \n"
                                       "    change-cursor: cursor(\'PointingHand\'); \n"
                                       "}")
        self.refresh_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refresh_btn.setObjectName("refresh_btn")

        self.gridLayout.addWidget(self.refresh_btn, 1, 0, 1, 1)

        self.save_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.save_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.save_btn.setStyleSheet("border-radius: 20px;\n"
                                    "background-color: #EE5E00;\n"
                                    "border: solid 2px ;\n"
                                    "border-color: #fff;\n"
                                    "\n"
                                    "color: #fff;\n"
                                    "font-weight: 400;\n"
                                    "\n"
                                    "padding: 10px;\n"
                                    "\n"
                                    "QPushButton#save_btn:hover { \n"
                                    "    change-cursor: cursor(\'PointingHand\'); \n"
                                    "}\n"
                                    "")
        self.save_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_btn.setObjectName("save_btn")

        self.gridLayout.addWidget(self.save_btn, 0, 0, 1, 1)

        self.change_c_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.change_c_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.change_c_btn.setStyleSheet("border-radius: 20px;\n"
                                        "background-color: #EE5E00;\n"
                                        "border: solid 2px ;\n"
                                        "border-color: #fff;\n"
                                        "\n"
                                        "color: #fff;\n"
                                        "font-weight: 400;\n"
                                        "\n"
                                        "padding: 10px;\n"
                                        "\n"
                                        "QPushButton#change_c_btn:hover { \n"
                                        "    change-cursor: cursor(\'PointingHand\'); \n"
                                        "}")
        self.change_c_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_c_btn.setObjectName("change_c_btn")

        self.gridLayout.addWidget(self.change_c_btn, 0, 1, 1, 1)

        self.exit_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.exit_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.exit_btn.setStyleSheet("border-radius: 20px;\n"
                                    "background-color: #EE5E00;\n"
                                    "border: solid 2px ;\n"
                                    "border-color: #fff;\n"
                                    "\n"
                                    "color: #fff;\n"
                                    "font-weight: 400;\n"
                                    "\n"
                                    "padding: 10px;\n"
                                    "\n"
                                    "QPushButton#exit_btn:hover { \n"
                                    "    change-cursor: cursor(\'PointingHand\'); \n"
                                    "}")

        self.exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_btn.setObjectName("exit_btn")

        self.gridLayout.addWidget(self.exit_btn, 1, 1, 1, 1)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 270, 331, 151))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setStyleSheet("color: #fff;\n"
                                   "font: 11pt \"Open Sans\";\n"
                                   "font-weight: bold;\n"
                                   "")

        self.label_2.setObjectName("label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setStyleSheet("color: #fff;\n"
                                   "font: 11pt \"Open Sans\";\n"
                                   "font-weight: bold;\n"
                                   "")

        self.label_4.setObjectName("label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.lastly_updated = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lastly_updated.setStyleSheet("color: #EE5E00;\n"
                                   "font: 11pt \"Open Sans\";")
        self.lastly_updated.setText("")
        self.lastly_updated.setObjectName("label_7")

        self.gridLayout_2.addWidget(self.lastly_updated, 2, 1, 1, 1)

        self.in_air = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.in_air.setMaximumSize(QtCore.QSize(100, 16777215))
        self.in_air.setStyleSheet("color: #EE5E00;\n"
                                   "font: 11pt \"Open Sans\";")
        self.in_air.setText("")
        self.in_air.setObjectName("label_5")

        self.gridLayout_2.addWidget(self.in_air, 0, 1, 1, 1)

        self.aggregate = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.aggregate.setStyleSheet("color: #EE5E00;\n"
                                   "font: 11pt \"Open Sans\";")
        self.aggregate.setText("")
        self.aggregate.setObjectName("label_6")

        self.gridLayout_2.addWidget(self.aggregate, 1, 1, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setStyleSheet("color: #fff;\n"
                                   "font: 11pt \"Open Sans\";\n"
                                   "font-weight: bold;")

        self.label_3.setObjectName("label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setStyleSheet("color: #fff;\n"
                                   "font: 11pt \"Open Sans\";\n"
                                   "font-weight: bold;\n"
                                   "")

        self.label_8.setObjectName("label_8")

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.velocity = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.velocity.setStyleSheet("color: #EE5E00;\n"
                                   "font: 11pt \"Open Sans\";")
        self.velocity.setText("")
        self.velocity.setObjectName("label_9")

        self.gridLayout_2.addWidget(self.velocity, 3, 1, 1, 1)

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(60, 130, 21, 441))
        self.frame_2.setStyleSheet("background-color: rgb(238, 94, 0);\n"
                                   "border-top-left-radius: 15px;\n"
                                   "border-bottom-left-radius: 15px;")

        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 130, 751, 441))
        self.widget.setStyleSheet("background-color: rgb(26, 23, 59);")
        self.widget.setObjectName("widget")

        self.WebWidget = QtWebEngineWidgets.QWebEngineView(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: rgb(26, 23, 59);\n"
                                     "border-top: 2px solid #fff;")

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # => STATUS BAR LABELS
        self.author_desc = QLabel('CODED AND DESIGNED BY ')
        self.author = QLabel('Adison')

        self.author_desc.setStyleSheet('font: 8pt Open Sans; border: none; color: #fff; font-weight: 700; ')
        self.author.setStyleSheet('font: 16pt Open Sans; border: solid 1px transparent; color: #fff;')
        self.statusbar.setStyleSheet(
                                     'color: #fff; '
                                     'background-color: '
                                     'rgb(26, 23, 59); '
                                     'border-top: 2px solid #fff; '
                                     'font: 12pt Open Sans; '
        )

        self.statusbar.showMessage('TIMATHON 2021')
        self.statusbar.addPermanentWidget(self.author_desc)
        self.statusbar.addPermanentWidget(self.author)
        self.statusbar.setFixedSize(WINDOW_WIDTH+20, 40)

        self.author.adjustSize()
        self.author_desc.adjustSize()

        self.author.move(WINDOW_WIDTH-10, WIND0W_HEIGHT-10)
        self.author_desc.move(WINDOW_WIDTH-20, WIND0W_HEIGHT-15)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.MAP = None
        self.create_new_map()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Flights Visualization"))

        self.label.setText(_translate("MainWindow", "    FLIGHTS VISUALIZATION"))
        self.options.setText(_translate("MainWindow", "   OPTIONS"))
        self.stats.setText(_translate("MainWindow", "   STATISTICS"))

        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.save_btn.setText(_translate("MainWindow", "Save current map"))
        self.change_c_btn.setText(_translate("MainWindow", "Change map colors"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))

        self.label_2.setText(_translate("MainWindow", "AGGREGATE:"))
        self.label_4.setText(_translate("MainWindow", "LASTLY UPDATED:"))
        self.label_3.setText(_translate("MainWindow", "IN AIR:"))
        self.label_8.setText(_translate("MainWindow", "FASTEST AIR CRAFT:"))

        # => CONNECT BUTTONS
        self.refresh_btn.clicked.connect(self.create_new_map)
        self.save_btn.clicked.connect(self.save_current_map)
        self.exit_btn.clicked.connect(self.exit_app)
        self.change_c_btn.clicked.connect(self.change_theme)

    # => CREATE A (NEW) MAP
    def create_new_map(self):
        del self.MAP

        # => CREATE NEW MAP
        self.MAP = folium.Map(location=func.LOCATION, zoom_start=4, tiles=THEME['map-theme'])

        # => CREATE MARKERS
        AIR_CRAFTS = []
        self.MAX_VELOCITY = 0

        for pack in extract.get_from_opensky(req.get_air_crafts_pos()):
            AIR_CRAFTS.append(pack)

        self.ALL_AIRCRAFTS = 0
        self.ALL_AIRCRAFTS = len(AIR_CRAFTS)

        self.aggr = ag.find_aggregate(AIR_CRAFTS)

        if self.aggr is False:
            again = []
            for pack in extract.get_from_opensky(req.get_air_crafts_pos()):
                again.append(pack)

            self.aggr = ag.find_aggregate(again)
            if self.aggr is False: self.aggr = LOCATION

        self.aggr = '' + str(round(self.aggr[1], 3)) + ', ' + str(round(self.aggr[0], 3))

        for index, scatter in enumerate(AIR_CRAFTS):

            # => UNPACK
            lon, lat, vel, heading, callsign, last = scatter

            # => SWAP THE EMPTY STRING IN PLANE NAME AND GET THE HIGHEST VELOCITY
            if callsign == "": callsign = 'no-data'

            if vel is not None:
                if vel > self.MAX_VELOCITY: self.MAX_VELOCITY = vel

            # => SHOW 600 MARKERS FOR APP OPTIMIZATION
            if index > 600: continue

            # => CREATE A MARKER
            folium.Marker(
                location=[lat, lon],
                color=THEME['marker-color'],
                icon=folium.Icon(color='orange', prefix='fa', icon='plane'),
                popup=self.create_popup(callsign, vel, last, heading),
                tooltip=f"<strong>{callsign}</strong>"
            ).add_to(self.MAP)

        # => SAVE AND SHOW MAP
        data = io.BytesIO()
        self.MAP.save(data, close_file=False)

        self.WebWidget.setHtml(data.getvalue().decode())
        self.WebWidget.resize(func.MAP_WIDTH, func.MAP_HEIGHT)

        # => UPDATE THE STATISTICS
        self.lastly_updated.setText(datetime.now().strftime('%H:%M:%S'))
        self.in_air.setText(str(self.ALL_AIRCRAFTS))
        self.aggregate.setText(self.aggr)
        self.velocity.setText(str(self.MAX_VELOCITY) + 'km/h')

        self.statusbar.showMessage('TIMATHON 2021')

    # => EXIT APP
    def exit_app(self):
        del self.MAP
        sys.exit()

    # => SAVE CURRENT MAP
    def save_current_map(self):
        options = QFileDialog.Options()
        filepath = QFileDialog.getSaveFileName(None, "Save the current map", "map", ".html", options=options)

        self.MAP.save(filepath[0] + filepath[1])

    # => CHANGE THE MAP COLORS
    def change_theme(self):
        MODE = func.change_the_current_map_colors()
        self.statusbar.showMessage(f'TIMATHON 2021 - theme will change to {MODE} when you refresh the map')

    def create_popup(self, callsign, vel, last, heading):

        content = f'<body style="font-family: sans-serif; "> ' \
                  f'<h4>Aircraft: {callsign}</h4>' \
                  f'<b>Speed: </b>{vel} km/h <br />' \
                  f'<b>Last seen: </b> {datetime.fromtimestamp(int(last)).strftime("%H:%M:%S")} <br />' \
                  f'<b>Direction: </b> {heading} deg - {func.angle(heading)}' \
                  f'</body>'

        iframe = folium.IFrame(content, width=200, height=140)

        return folium.Popup(iframe)
