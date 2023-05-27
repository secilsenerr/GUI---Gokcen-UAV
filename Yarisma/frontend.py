
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import folium # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1929, 1024)
        MainWindow.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n" 
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0.954, y2:0.0619545, stop:0.0421053 rgba(0, 5, 46, 255), stop:1 rgba(0, 0, 76, 249));\n"
"color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Menu = QtWidgets.QTabWidget(self.centralwidget)
        self.Menu.setGeometry(QtCore.QRect(20, 19, 1871, 931))
        self.Menu.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Menu.setStyleSheet("QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"background: #97DEFF;\n"
"}")
        self.Menu.setTabPosition(QtWidgets.QTabWidget.North)
        self.Menu.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Menu.setIconSize(QtCore.QSize(20, 20))
        self.Menu.setElideMode(QtCore.Qt.ElideNone)
        self.Menu.setUsesScrollButtons(True)
        self.Menu.setDocumentMode(True)
        self.Menu.setTabsClosable(False)
        self.Menu.setMovable(False)
        self.Menu.setTabBarAutoHide(False)
        self.Menu.setObjectName("Menu")
        self.control = QtWidgets.QWidget()
        self.control.setObjectName("control")
        self.title1 = QtWidgets.QLabel(self.control)
        self.title1.setGeometry(QtCore.QRect(40, 10, 221, 51))
        self.title1.setStyleSheet("font: 25pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));")
        self.title1.setObjectName("title1")
        self.battery = QtWidgets.QProgressBar(self.control)
        self.battery.setGeometry(QtCore.QRect(810, 650, 71, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.battery.sizePolicy().hasHeightForWidth())
        self.battery.setSizePolicy(sizePolicy)
        self.battery.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.battery.setStyleSheet("background-image:url(\"C:\\Users\\zeyne\\Masaüstü\\daire.png\");")
        self.battery.setProperty("value", 34)
        self.battery.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.battery.setOrientation(QtCore.Qt.Vertical)
        self.battery.setObjectName("battery")
        self.liveCamera = QtWidgets.QLabel(self.control)
        self.liveCamera.setGeometry(QtCore.QRect(1120, 110, 721, 711))
        self.liveCamera.setStyleSheet("border-radius:10px;\n"
"border-style: outset;\n"
"border-width: 6;\n"
"border-color: #2B3467;\n"
"backgorund-color: linear-gradient(to right, #0f0c29, #302b63, #24243e);")
        self.liveCamera.setText("")
        self.liveCamera.setObjectName("liveCamera")
        self.powerCon_Label = QtWidgets.QLabel(self.control)
        self.powerCon_Label.setGeometry(QtCore.QRect(700, 600, 301, 37))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.powerCon_Label.setFont(font)
        self.powerCon_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 12pt;")
        self.powerCon_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.powerCon_Label.setObjectName("powerCon_Label")
        self.liveCamera_Label = QtWidgets.QLabel(self.control)
        self.liveCamera_Label.setGeometry(QtCore.QRect(1530, 840, 311, 51))
        self.liveCamera_Label.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));")
        self.liveCamera_Label.setObjectName("liveCamera_Label")
        self.longtitude_Qlabel = QtWidgets.QLabel(self.control)
        self.longtitude_Qlabel.setGeometry(QtCore.QRect(770, 330, 151, 51))
        self.longtitude_Qlabel.setAutoFillBackground(False)
        self.longtitude_Qlabel.setStyleSheet("color:white;")
        self.longtitude_Qlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.longtitude_Qlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.longtitude_Qlabel.setObjectName("longtitude_Qlabel")
        self.information = QtWidgets.QGroupBox(self.control)
        self.information.setGeometry(QtCore.QRect(40, 380, 521, 251))
        self.information.setStyleSheet("border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0.954, y2:0.0619545, stop:0.0421053 rgba(0, 17, 156, 189), stop:0.950249 rgba(4, 4, 74, 90))")
        self.information.setObjectName("information")
        self.terminal_TextEdit = QtWidgets.QTextEdit(self.information)
        self.terminal_TextEdit.setGeometry(QtCore.QRect(10, 50, 501, 181))
        self.terminal_TextEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"")
        self.terminal_TextEdit.setObjectName("terminal_TextEdit")
        self.battery_Label = QtWidgets.QLabel(self.control)
        self.battery_Label.setGeometry(QtCore.QRect(780, 790, 131, 31))
        self.battery_Label.setAutoFillBackground(False)
        self.battery_Label.setStyleSheet("color:white;")
        self.battery_Label.setFrameShape(QtWidgets.QFrame.Box)
        self.battery_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.battery_Label.setObjectName("battery_Label")
        self.disconnect_PushButton = QtWidgets.QPushButton(self.control)
        self.disconnect_PushButton.setGeometry(QtCore.QRect(1300, 20, 181, 61))
        self.disconnect_PushButton.setStyleSheet(".QPushButton{\n"
"    font: 75 15pt \"MS Shell Dlg 2\";\n"
"    background-color: qlineargradient(spread:pad, x1:0.073, y1:0.932, x2:0.948579, y2:0.057, stop:0.527363 rgba(234, 0, 0, 255));\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0.073, y1:0.932, x2:0.948579, y2:0.057, stop:0.527363 rgba(153, 0, 0, 255))\n"
"}")
        self.disconnect_PushButton.setObjectName("disconnect_PushButton")
        self.connection_Group = QtWidgets.QGroupBox(self.control)
        self.connection_Group.setGeometry(QtCore.QRect(40, 80, 521, 281))
        self.connection_Group.setStyleSheet("border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.954, y2:0.0619545, stop:0.0421053 rgba(0, 10, 99, 184), stop:0.950249 rgba(4, 4, 74, 249))")
        self.connection_Group.setObjectName("connection_Group")
        self.ip_Label = QtWidgets.QLabel(self.connection_Group)
        self.ip_Label.setGeometry(QtCore.QRect(30, 40, 71, 31))
        self.ip_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 12pt;\n"
"")
        self.ip_Label.setObjectName("ip_Label")
        self.port_Label = QtWidgets.QLabel(self.connection_Group)
        self.port_Label.setGeometry(QtCore.QRect(20, 100, 51, 41))
        self.port_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 12pt;")
        self.port_Label.setObjectName("port_Label")
        self.type_Label = QtWidgets.QLabel(self.connection_Group)
        self.type_Label.setGeometry(QtCore.QRect(20, 220, 61, 31))
        self.type_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 12pt;")
        self.type_Label.setObjectName("type_Label")
        self.baudrate_Label = QtWidgets.QLabel(self.connection_Group)
        self.baudrate_Label.setGeometry(QtCore.QRect(20, 170, 61, 20))
        self.baudrate_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 12pt;")
        self.baudrate_Label.setObjectName("baudrate_Label")
        self.ip_LineEdit = QtWidgets.QLineEdit(self.connection_Group)
        self.ip_LineEdit.setGeometry(QtCore.QRect(90, 40, 141, 41))
        self.ip_LineEdit.setStyleSheet("border:2px solid #BAD7E9;\n"
"")
        self.ip_LineEdit.setObjectName("ip_LineEdit")
        self.date_Label = QtWidgets.QLabel(self.connection_Group)
        self.date_Label.setGeometry(QtCore.QRect(270, 100, 61, 41))
        self.date_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 12pt;")
        self.date_Label.setObjectName("date_Label")
        self.connection_Lable = QtWidgets.QLabel(self.connection_Group)
        self.connection_Lable.setGeometry(QtCore.QRect(250, 40, 101, 31))
        self.connection_Lable.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 12pt;")
        self.connection_Lable.setObjectName("connection_Lable")
        self.location_Label = QtWidgets.QLabel(self.connection_Group)
        self.location_Label.setGeometry(QtCore.QRect(270, 220, 61, 31))
        self.location_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 12pt;")
        self.location_Label.setObjectName("location_Label")
        self.time_Label = QtWidgets.QLabel(self.connection_Group)
        self.time_Label.setGeometry(QtCore.QRect(270, 170, 61, 20))
        self.time_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 12pt;")
        self.time_Label.setObjectName("time_Label")
        self.port_LineEdit = QtWidgets.QLineEdit(self.connection_Group)
        self.port_LineEdit.setGeometry(QtCore.QRect(90, 100, 141, 41))
        self.port_LineEdit.setStyleSheet("border:2px solid #BAD7E9;")
        self.port_LineEdit.setObjectName("port_LineEdit")
        self.baudrate_LineEdit = QtWidgets.QLineEdit(self.connection_Group)
        self.baudrate_LineEdit.setGeometry(QtCore.QRect(90, 160, 141, 41))
        self.baudrate_LineEdit.setStyleSheet("border:2px solid #BAD7E9;")
        self.baudrate_LineEdit.setObjectName("baudrate_LineEdit")
        self.type_LineEdit = QtWidgets.QLineEdit(self.connection_Group)
        self.type_LineEdit.setGeometry(QtCore.QRect(90, 220, 141, 41))
        self.type_LineEdit.setStyleSheet("border:2px solid #BAD7E9;")
        self.type_LineEdit.setObjectName("type_LineEdit")
        self.connection_LineEdit = QtWidgets.QLineEdit(self.connection_Group)
        self.connection_LineEdit.setGeometry(QtCore.QRect(350, 40, 141, 41))
        self.connection_LineEdit.setStyleSheet("border:2px solid #BAD7E9;")
        self.connection_LineEdit.setObjectName("connection_LineEdit")
        self.date_LineEdit = QtWidgets.QLineEdit(self.connection_Group)
        self.date_LineEdit.setGeometry(QtCore.QRect(350, 100, 141, 41))
        self.date_LineEdit.setStyleSheet("border:2px solid #BAD7E9;")
        self.date_LineEdit.setObjectName("date_LineEdit")
        self.time_LineEdit = QtWidgets.QLineEdit(self.connection_Group)
        self.time_LineEdit.setGeometry(QtCore.QRect(350, 160, 141, 41))
        self.time_LineEdit.setStyleSheet("border:2px solid #BAD7E9;")
        self.time_LineEdit.setObjectName("time_LineEdit")
        self.location_LineEdit = QtWidgets.QLineEdit(self.connection_Group)
        self.location_LineEdit.setGeometry(QtCore.QRect(350, 220, 141, 41))
        self.location_LineEdit.setStyleSheet("border:2px solid #BAD7E9;")
        self.location_LineEdit.setObjectName("location_LineEdit")
        self.disarm_PushButton = QtWidgets.QPushButton(self.control)
        self.disarm_PushButton.setGeometry(QtCore.QRect(1680, 20, 181, 61))
        self.disarm_PushButton.setStyleSheet(".QPushButton{\n"
"    font: 75 15pt \"MS Shell Dlg 2\";\n"
"    background-color: qlineargradient(spread:pad, x1:0.073, y1:0.932, x2:0.948579, y2:0.057, stop:0.527363 rgba(0, 121, 223, 255));\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0.073, y1:0.932, x2:0.948579, y2:0.057, stop:0.527363 rgba(0, 85, 156, 255));\n"
"}")
        self.disarm_PushButton.setObjectName("disarm_PushButton")
        self.delivery_PushButton = QtWidgets.QPushButton(self.control)
        self.delivery_PushButton.setGeometry(QtCore.QRect(1490, 20, 181, 61))
        self.delivery_PushButton.setStyleSheet(".QPushButton{\n"
"    font: 75 13pt \"MS Shell Dlg 2\";\n"
"    background-color: #fdc600;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background-color: #ddaa00;\n"
"}")
        self.delivery_PushButton.setObjectName("delivery_PushButton")
        self.title2 = QtWidgets.QLabel(self.control)
        self.title2.setGeometry(QtCore.QRect(240, 10, 101, 51))
        self.title2.setStyleSheet("font: 25pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"color: #BAD7E9;")
        self.title2.setObjectName("title2")
        self.connect_PushButton = QtWidgets.QPushButton(self.control)
        self.connect_PushButton.setGeometry(QtCore.QRect(1110, 20, 181, 61))
        self.connect_PushButton.setStyleSheet(".QPushButton{\n"
"    font: 75 15pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(0, 150, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background-color: rgb(0, 110, 0);\n"
"}")
        self.connect_PushButton.setObjectName("connect_PushButton")
        self.detection_Group = QtWidgets.QGroupBox(self.control)
        self.detection_Group.setGeometry(QtCore.QRect(40, 650, 521, 251))
        self.detection_Group.setStyleSheet("border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.954, y2:0.0619545, stop:0.0421053 rgba(0, 10, 99, 184), stop:0.950249 rgba(4, 4, 74, 249));")
        self.detection_Group.setObjectName("detection_Group")
        self.detection_LineEdit = QtWidgets.QLineEdit(self.detection_Group)
        self.detection_LineEdit.setGeometry(QtCore.QRect(230, 40, 261, 41))
        self.detection_LineEdit.setStyleSheet("border:2px solid #BAD7E9;")
        self.detection_LineEdit.setObjectName("detection_LineEdit")
        self.detection_Label = QtWidgets.QLabel(self.detection_Group)
        self.detection_Label.setGeometry(QtCore.QRect(20, 50, 161, 31))
        self.detection_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 12pt;\n"
"")
        self.detection_Label.setObjectName("detection_Label")
        self.detectionTime_Label = QtWidgets.QLabel(self.detection_Group)
        self.detectionTime_Label.setGeometry(QtCore.QRect(20, 90, 181, 41))
        self.detectionTime_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 12pt;")
        self.detectionTime_Label.setObjectName("detectionTime_Label")
        self.detectionTime_LineEdit = QtWidgets.QLineEdit(self.detection_Group)
        self.detectionTime_LineEdit.setGeometry(QtCore.QRect(230, 90, 261, 41))
        self.detectionTime_LineEdit.setStyleSheet("border:2px solid #BAD7E9;")
        self.detectionTime_LineEdit.setObjectName("detectionTime_LineEdit")
        self.delivery_Label = QtWidgets.QLabel(self.detection_Group)
        self.delivery_Label.setGeometry(QtCore.QRect(20, 140, 151, 41))
        self.delivery_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 12pt;")
        self.delivery_Label.setObjectName("delivery_Label")
        self.delivery_LineEdit = QtWidgets.QLineEdit(self.detection_Group)
        self.delivery_LineEdit.setGeometry(QtCore.QRect(230, 140, 261, 41))
        self.delivery_LineEdit.setStyleSheet("border:2px solid #BAD7E9;")
        self.delivery_LineEdit.setObjectName("delivery_LineEdit")
        self.deliveryTime_LineEdit = QtWidgets.QLineEdit(self.detection_Group)
        self.deliveryTime_LineEdit.setGeometry(QtCore.QRect(230, 190, 261, 41))
        self.deliveryTime_LineEdit.setStyleSheet("border:2px solid #BAD7E9;")
        self.deliveryTime_LineEdit.setObjectName("deliveryTime_LineEdit")
        self.deliveryTime_Label = QtWidgets.QLabel(self.detection_Group)
        self.deliveryTime_Label.setGeometry(QtCore.QRect(20, 190, 151, 41))
        self.deliveryTime_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 12pt;")
        self.deliveryTime_Label.setObjectName("deliveryTime_Label")
        self.longtitude_Qgroupbox = QtWidgets.QGroupBox(self.control)
        self.longtitude_Qgroupbox.setGeometry(QtCore.QRect(760, 400, 171, 161))
        self.longtitude_Qgroupbox.setStyleSheet("border-radius:80%;\n"
"border:3px solid #BAD7E9;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.954, y2:0.0619545, stop:0.0497512 rgba(4, 4, 74, 249), stop:0.945274 rgba(0, 17, 156, 189));\n"
"color:")
        self.longtitude_Qgroupbox.setTitle("")
        self.longtitude_Qgroupbox.setObjectName("longtitude_Qgroupbox")
        self.longtitude_Qlcdnumber = QtWidgets.QLCDNumber(self.longtitude_Qgroupbox)
        self.longtitude_Qlcdnumber.setGeometry(QtCore.QRect(0, 60, 161, 41))
        self.longtitude_Qlcdnumber.setStyleSheet("border:none;\n"
"text-align:center;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 75 15pt \"MS Shell Dlg 2\";")
        self.longtitude_Qlcdnumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.longtitude_Qlcdnumber.setDigitCount(3)
        self.longtitude_Qlcdnumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.longtitude_Qlcdnumber.setProperty("intValue", 0)
        self.longtitude_Qlcdnumber.setObjectName("longtitude_Qlcdnumber")
        self.latitude_Qlabel = QtWidgets.QLabel(self.control)
        self.latitude_Qlabel.setGeometry(QtCore.QRect(780, 70, 131, 51))
        self.latitude_Qlabel.setAutoFillBackground(False)
        self.latitude_Qlabel.setStyleSheet("color:white;")
        self.latitude_Qlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.latitude_Qlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.latitude_Qlabel.setObjectName("latitude_Qlabel")
        self.latitude_Qgroupbox = QtWidgets.QGroupBox(self.control)
        self.latitude_Qgroupbox.setGeometry(QtCore.QRect(760, 140, 171, 161))
        self.latitude_Qgroupbox.setStyleSheet("border-radius:80%;\n"
"border:3px solid #BAD7E9;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.954, y2:0.0619545, stop:0.0497512 rgba(4, 4, 74, 249), stop:0.945274 rgba(0, 17, 156, 189));\n"
"color:")
        self.latitude_Qgroupbox.setTitle("")
        self.latitude_Qgroupbox.setObjectName("latitude_Qgroupbox")
        self.latitude_Qlcdnumber = QtWidgets.QLCDNumber(self.latitude_Qgroupbox)
        self.latitude_Qlcdnumber.setGeometry(QtCore.QRect(0, 60, 161, 41))
        self.latitude_Qlcdnumber.setStyleSheet("border:none;\n"
"text-align:center;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 75 15pt \"MS Shell Dlg 2\";")
        self.latitude_Qlcdnumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.latitude_Qlcdnumber.setDigitCount(3)
        self.latitude_Qlcdnumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.latitude_Qlcdnumber.setProperty("intValue", 0)
        self.latitude_Qlcdnumber.setObjectName("latitude_Qlcdnumber")
        self.Menu.addTab(self.control, "")
        self.data = QtWidgets.QWidget()
        self.data.setObjectName("data")

        #self.map = QtWidgets.QLabel(self.tab_6)
        #self.map.setGeometry(QtCore.QRect(20, 130, 861, 761))
        #self.map.setStyleSheet("border-radius:10px;\n" "border-style: outset;\n""border-width: 6;\n""border-color: #2B3467;\n""backgorund-color: linear-gradient(to right, #0f0c29, #302b63, #24243e);")
        #self.map.setText("")
        #self.map.setObjectName("map")

        
        #MAP
        m = folium.Map(location=[41.0082, 28.9784], zoom_start=13) #istanbul koordinatları 
        folium.Marker(location=[41.010302, 29.051585],popup='Acıbadem',tooltip='<strong>Gökçen UAV</strong>',icon=folium.Icon(color='red',icon='plane')).add_to(m)
        self.map = QtWebEngineWidgets.QWebEngineView(self.data)
        self.map.setHtml(m.get_root().render())
        self.map.resize(861, 761)
        self.map.move(20, 130)
        self.map.show()



        self.telemetry_information = QtWidgets.QGroupBox(self.data)
        self.telemetry_information.setGeometry(QtCore.QRect(930, 570, 951, 321))
        self.telemetry_information.setStyleSheet("border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0.954, y2:0.0619545, stop:0.0421053 rgba(0, 17, 156, 189), stop:0.950249 rgba(4, 4, 74, 90))")
        self.telemetry_information.setObjectName("telemetry_information")
        self.altitude_LineEdit = QtWidgets.QLineEdit(self.telemetry_information)
        self.altitude_LineEdit.setGeometry(QtCore.QRect(130, 80, 141, 71))
        self.altitude_LineEdit.setStyleSheet("border:2px solid #F9CEEE;\n"
"")
        self.altitude_LineEdit.setObjectName("altitude_LineEdit")
        self.altitude_Label = QtWidgets.QLabel(self.telemetry_information)
        self.altitude_Label.setGeometry(QtCore.QRect(130, 40, 151, 31))
        self.altitude_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"

"font: bold 16pt;\n"
"color: #F9CEEE;\n"
"")
        self.altitude_Label.setObjectName("altitude_Label")
        self.disttoMav_LineEdit = QtWidgets.QLineEdit(self.telemetry_information)
        self.disttoMav_LineEdit.setGeometry(QtCore.QRect(650, 80, 141, 71))
        self.disttoMav_LineEdit.setStyleSheet("border:2px solid #B8FFF9;\n"
"")
        self.disttoMav_LineEdit.setObjectName("disttoMav_LineEdit")
        self.yaw_Label = QtWidgets.QLabel(self.telemetry_information)
        self.yaw_Label.setGeometry(QtCore.QRect(400, 160, 151, 31))
        self.yaw_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font:bold 14pt;\n"
"color: #B3FFAE;\n"
"")
        self.yaw_Label.setObjectName("yaw_Label")
        self.disttoMav_Label = QtWidgets.QLabel(self.telemetry_information)
        self.disttoMav_Label.setGeometry(QtCore.QRect(660, 40, 131, 31))
        self.disttoMav_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: bold 14pt;\n"
"color: #B8FFF9;\n"
"")
        self.disttoMav_Label.setObjectName("disttoMav_Label")
        self.groundSpeed_Label = QtWidgets.QLabel(self.telemetry_information)
        self.groundSpeed_Label.setGeometry(QtCore.QRect(360, 40, 231, 31))
        self.groundSpeed_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: bold 14pt;\n"
"color: #FFE69A;\n"
"")
        self.groundSpeed_Label.setObjectName("groundSpeed_Label")
        self.verticalSpeed_LineEdit = QtWidgets.QLineEdit(self.telemetry_information)
        self.verticalSpeed_LineEdit.setGeometry(QtCore.QRect(650, 200, 141, 71))
        self.verticalSpeed_LineEdit.setStyleSheet("border:2px solid #FFF38C;\n"
"")
        self.verticalSpeed_LineEdit.setObjectName("verticalSpeed_LineEdit")
        self.groundSpeed_LineEdit = QtWidgets.QLineEdit(self.telemetry_information)
        self.groundSpeed_LineEdit.setGeometry(QtCore.QRect(390, 80, 141, 71))
        self.groundSpeed_LineEdit.setStyleSheet("border:2px solid #FFE69A;\n"
"")
        self.groundSpeed_LineEdit.setObjectName("groundSpeed_LineEdit")
        self.distToHome_LineEdit = QtWidgets.QLineEdit(self.telemetry_information)
        self.distToHome_LineEdit.setGeometry(QtCore.QRect(130, 200, 141, 71))
        self.distToHome_LineEdit.setStyleSheet("border:2px solid #F9C5D5;\n"
"")
        self.distToHome_LineEdit.setObjectName("distToHome_LineEdit")
        self.verticalSpeed_Label = QtWidgets.QLabel(self.telemetry_information)
        self.verticalSpeed_Label.setGeometry(QtCore.QRect(600, 160, 241, 31))
        self.verticalSpeed_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: bold 14pt;\n"
"color: #FFF38C;\n"
"")
        self.verticalSpeed_Label.setObjectName("verticalSpeed_Label")
        self.disttoHome_Label = QtWidgets.QLabel(self.telemetry_information)
        self.disttoHome_Label.setGeometry(QtCore.QRect(100, 160, 211, 31))
        self.disttoHome_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: bold 14pt;\n"
"color: #F9C5D5;\n"
"")
        self.disttoHome_Label.setObjectName("disttoHome_Label")
        self.yaw_LineEdit = QtWidgets.QLineEdit(self.telemetry_information)
        self.yaw_LineEdit.setGeometry(QtCore.QRect(390, 200, 141, 71))
        self.yaw_LineEdit.setStyleSheet("border:2px solid #BAD7E9;\n"
"")
        self.yaw_LineEdit.setObjectName("yaw_LineEdit")
        self.telemetryDisconnect_PushButton = QtWidgets.QPushButton(self.data)
        self.telemetryDisconnect_PushButton.setGeometry(QtCore.QRect(640, 20, 211, 61))
        self.telemetryDisconnect_PushButton.setStyleSheet(".QPushButton{\n"
"    font: 75 15pt \"MS Shell Dlg 2\";\n"
"    background-color: qlineargradient(spread:pad, x1:0.073, y1:0.932, x2:0.948579, y2:0.057, stop:0.527363 rgba(234, 0, 0, 255));\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0.073, y1:0.932, x2:0.948579, y2:0.057, stop:0.527363 rgba(153, 0, 0, 255))\n"
"}")
        self.telemetryDisconnect_PushButton.setObjectName("telemetryDisconnect_PushButton")
        self.telemetryConnect_PushButton = QtWidgets.QPushButton(self.data)
        self.telemetryConnect_PushButton.setGeometry(QtCore.QRect(390, 20, 221, 61))
        self.telemetryConnect_PushButton.setStyleSheet(".QPushButton{\n"
"    font: 75 15pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(0, 150, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background-color: rgb(0, 110, 0);\n"
"}")
        self.telemetryConnect_PushButton.setObjectName("telemetryConnect_PushButton")
        self.telemetry_information_2 = QtWidgets.QGroupBox(self.data)
        self.telemetry_information_2.setGeometry(QtCore.QRect(1320, 50, 541, 491))
        self.telemetry_information_2.setStyleSheet("border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0.954, y2:0.0619545, stop:0.0421053 rgba(0, 17, 156, 189), stop:0.950249 rgba(4, 4, 74, 90))")
        self.telemetry_information_2.setObjectName("telemetry_information_2")
        self.telemetry_information_terminal = QtWidgets.QTextEdit(self.telemetry_information_2)
        self.telemetry_information_terminal.setGeometry(QtCore.QRect(20, 40, 501, 431))
        self.telemetry_information_terminal.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"")
        self.telemetry_information_terminal.setObjectName("telemetry_information_terminal")
        self.title4 = QtWidgets.QLabel(self.data)
        self.title4.setGeometry(QtCore.QRect(220, 20, 121, 51))
        self.title4.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"color: #BAD7E9;")
        self.title4.setObjectName("title4")
        self.title3 = QtWidgets.QLabel(self.data)
        self.title3.setGeometry(QtCore.QRect(20, 20, 221, 51))
        self.title3.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));")
        self.title3.setObjectName("title3")
        self.counters = QtWidgets.QGroupBox(self.data)
        self.counters.setGeometry(QtCore.QRect(930, 50, 351, 491))
        self.counters.setStyleSheet("border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0.954, y2:0.0619545, stop:0.0421053 rgba(0, 17, 156, 189), stop:0.950249 rgba(4, 4, 74, 90))")
        self.counters.setObjectName("counters")
        self.airSpeed_Qgroupbox = QtWidgets.QGroupBox(self.counters)
        self.airSpeed_Qgroupbox.setGeometry(QtCore.QRect(100, 90, 161, 161))
        self.airSpeed_Qgroupbox.setStyleSheet("border-radius:80%;\n"
"border:3px solid #BAD7E9;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.954, y2:0.0619545, stop:0.0497512 rgba(4, 4, 74, 249), stop:0.945274 rgba(0, 17, 156, 189));\n"
"color:")
        self.airSpeed_Qgroupbox.setTitle("")
        self.airSpeed_Qgroupbox.setObjectName("airSpeed_Qgroupbox")
        self.airSpeed_Qlcdnumber = QtWidgets.QLCDNumber(self.airSpeed_Qgroupbox)
        self.airSpeed_Qlcdnumber.setGeometry(QtCore.QRect(0, 60, 161, 41))
        self.airSpeed_Qlcdnumber.setStyleSheet("border:none;\n"
"text-align:center;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 75 15pt \"MS Shell Dlg 2\";")
        self.airSpeed_Qlcdnumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.airSpeed_Qlcdnumber.setDigitCount(3)
        self.airSpeed_Qlcdnumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.airSpeed_Qlcdnumber.setProperty("intValue", 0)
        self.airSpeed_Qlcdnumber.setObjectName("airSpeed_Qlcdnumber")
        self.groundSpeed_Qgroupbox = QtWidgets.QGroupBox(self.counters)
        self.groundSpeed_Qgroupbox.setGeometry(QtCore.QRect(100, 320, 161, 161))
        self.groundSpeed_Qgroupbox.setStyleSheet("border-radius:80%;\n"
"border:3px solid #BAD7E9;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.954, y2:0.0619545, stop:0.0497512 rgba(4, 4, 74, 249), stop:0.945274 rgba(0, 17, 156, 189));\n"
"color:")
        self.groundSpeed_Qgroupbox.setTitle("")
        self.groundSpeed_Qgroupbox.setObjectName("groundSpeed_Qgroupbox")
        self.groundSpeed_Qlcdnumber = QtWidgets.QLCDNumber(self.groundSpeed_Qgroupbox)
        self.groundSpeed_Qlcdnumber.setGeometry(QtCore.QRect(0, 60, 161, 41))
        self.groundSpeed_Qlcdnumber.setStyleSheet("border:none;\n"
"text-align:center;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));\n"
"font: 75 15pt \"MS Shell Dlg 2\";")
        self.groundSpeed_Qlcdnumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.groundSpeed_Qlcdnumber.setDigitCount(3)
        self.groundSpeed_Qlcdnumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.groundSpeed_Qlcdnumber.setProperty("intValue", 0)
        self.groundSpeed_Qlcdnumber.setObjectName("groundSpeed_Qlcdnumber")
        self.airSpeed_Qlabel = QtWidgets.QLabel(self.data)
        self.airSpeed_Qlabel.setGeometry(QtCore.QRect(1060, 90, 111, 41))
        self.airSpeed_Qlabel.setAutoFillBackground(False)
        self.airSpeed_Qlabel.setStyleSheet("color:white;")
        self.airSpeed_Qlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.airSpeed_Qlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.airSpeed_Qlabel.setObjectName("airSpeed_Qlabel")
        self.groundSpeed_Qlabel = QtWidgets.QLabel(self.data)
        self.groundSpeed_Qlabel.setGeometry(QtCore.QRect(1040, 320, 151, 41))
        self.groundSpeed_Qlabel.setAutoFillBackground(False)
        self.groundSpeed_Qlabel.setStyleSheet("color:white;")
        self.groundSpeed_Qlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.groundSpeed_Qlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.groundSpeed_Qlabel.setObjectName("groundSpeed_Qlabel")
        self.map_Label = QtWidgets.QLabel(self.data)
        self.map_Label.setGeometry(QtCore.QRect(810, 850, 71, 51))
        self.map_Label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.983, x2:0.952, y2:0.091, stop:0.00526316 rgba(16, 7, 13, 0), stop:1 rgba(5, 11, 3, 0));")
        self.map_Label.setObjectName("map_Label")
        self.Menu.addTab(self.data, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1929, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Menu.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title1.setText(_translate("MainWindow", "GOKCEN"))
        self.powerCon_Label.setText(_translate("MainWindow", "POWER CONSUMPTION"))
        self.liveCamera_Label.setText(_translate("MainWindow", "LIVE CAMERA IMAGE"))
        self.longtitude_Qlabel.setText(_translate("MainWindow", "LONGTITUDE"))
        self.information.setTitle(_translate("MainWindow", "Information"))
        self.battery_Label.setText(_translate("MainWindow", "BATTERY"))
        self.disconnect_PushButton.setText(_translate("MainWindow", "Disconnect"))
        self.connection_Group.setTitle(_translate("MainWindow", "Connection"))
        self.ip_Label.setText(_translate("MainWindow", "IP:"))
        self.port_Label.setText(_translate("MainWindow", "Port:"))
        self.type_Label.setText(_translate("MainWindow", "Type:"))
        self.baudrate_Label.setText(_translate("MainWindow", "Baud:"))
        self.date_Label.setText(_translate("MainWindow", "Date:"))
        self.connection_Lable.setText(_translate("MainWindow", "Connect: "))
        self.location_Label.setText(_translate("MainWindow", "Loc:"))
        self.time_Label.setText(_translate("MainWindow", "Time:"))
        self.disarm_PushButton.setText(_translate("MainWindow", "Disarm"))
        self.delivery_PushButton.setText(_translate("MainWindow", "Arm"))
        self.title2.setText(_translate("MainWindow", "UAV"))
        self.connect_PushButton.setText(_translate("MainWindow", "Connect"))
        self.detection_Group.setTitle(_translate("MainWindow", "Detection"))
        self.detection_Label.setText(_translate("MainWindow", "Detection: "))
        self.detectionTime_Label.setText(_translate("MainWindow", "Detection Time:"))
        self.delivery_Label.setText(_translate("MainWindow", "Delivery : "))
        self.deliveryTime_Label.setText(_translate("MainWindow", "Delivery Time:"))
        self.latitude_Qlabel.setText(_translate("MainWindow", "LATITUDE"))
        self.Menu.setTabText(self.Menu.indexOf(self.control), _translate("MainWindow", "Control"))
        self.telemetry_information.setTitle(_translate("MainWindow", "Telemetry Information"))
        self.altitude_Label.setText(_translate("MainWindow", "Altitude"))
        self.yaw_Label.setText(_translate("MainWindow", "Yaw(deg)"))
        self.disttoMav_Label.setText(_translate("MainWindow", "MODE"))
        self.groundSpeed_Label.setText(_translate("MainWindow", "GroundSpeed"))
        self.verticalSpeed_Label.setText(_translate("MainWindow", "VerticalSpeed"))
        self.disttoHome_Label.setText(_translate("MainWindow", "Dist to Home"))
        self.telemetryDisconnect_PushButton.setText(_translate("MainWindow", "Disconnect"))
        self.telemetryConnect_PushButton.setText(_translate("MainWindow", "Connect"))
        self.telemetry_information_2.setTitle(_translate("MainWindow", "Information"))
        self.title4.setText(_translate("MainWindow", " UAV"))
        self.title3.setText(_translate("MainWindow", "GOKCEN"))
        self.counters.setTitle(_translate("MainWindow", "Counters"))
        self.airSpeed_Qlabel.setText(_translate("MainWindow", "Air Speed"))
        self.groundSpeed_Qlabel.setText(_translate("MainWindow", "Ground Speed"))
        self.map_Label.setText(_translate("MainWindow", "MAP"))
        self.Menu.setTabText(self.Menu.indexOf(self.data), _translate("MainWindow", "Data"))

"""
if _name_ == "_main_":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())"""