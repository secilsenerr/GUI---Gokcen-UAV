from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem, QTableWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, QMetaObject, pyqtSignal, pyqtSlot
from PyQt5 import QtCore
from pymavlink import mavutil
from frontend import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import threading
import math
import folium


class mainClass():
    def __init__(self):
        super(mainClass, self).__init__()

        print("hello1")
        self.should_stop = False
        # telemetri sayfasında bağlantı butonuna basıldığında...
        ui.telemetryConnect_PushButton.clicked.connect(self.connectTelemetry_Th)

    # connect butonu threadleri
    def connectTelemetry_Th(self):
        connectTelemetry = threading.Thread(target=self.connect)
        connectTelemetry.start()

        map_thread = threading.Thread(target=self.update_map)
        map_thread.start()

    # mavlink bağlanma fonksiyonu
    def connect(self):
        global vehicle
        vehicle = mavutil.mavlink_connection('tcp:127.0.0.1:5763')  # buraya kendi bağlantı bilgilerini giriceksiniz. örn: (COM4, baud = 57600) COM3*****
        while True:
            vehicle.wait_heartbeat()
            self.term = "Bağlantı başarılı.\n"
            print(self.term)
            self.get_data()

    # mavlink veri çekme fonksiyonu
    def get_data(self):
        while True:
            msg = vehicle.recv_match()
            if msg:
                # alınan mesajların grubuna göre veri çekme işlemi yapılır.

                # groundspeed, verticalspeed, yaw, altitude, lat, lon
                if msg.get_type() == 'GLOBAL_POSITION_INT':
                    self.groundSpeed = msg.vx / 100.0
                    self.verticalSpeed = msg.vz / 100.0
                    self.yaw = msg.hdg / 100.0
                    self.altitude = msg.relative_alt / 1000.0  # convert to meters
                    self.lat= msg.lat
                    self.lon = msg.lon
                # airspeed
                elif msg.get_type() == 'VFR_HUD':
                    self.airspeed = msg.airspeed
                # uçuşun modunu alma, otonom, manuel...
                elif msg.get_type() == 'HEARTBEAT':
                    self.mode = mavutil.mode_string_v10(msg)
                    # print(self.mode)

                elif msg.get_type() == 'SYS_STATUS':
                    self.batary = msg.current_battery
                    self.value = 70
                # yol: battery_status grubundan almak. bu grubun verisi gelmemişti.  voltaj ve akım üzerinden hesaplıyor.
                elif msg.get_type() == 'BATTERY_STATUS':
                    print("tmmm")
                    battery_voltage = msg.voltage / 1000.0  # mV cinsinden batarya gerilimi
                    battery_current = msg.current / 100.0  # 0.1A cinsinden batarya akımı
                    battery_remaining = msg.battery_remaining  # yüzde cinsinden kalan batarya kapasitesi
                    print("Batarya Gerilimi: ", battery_voltage, "V")
                    print("Batarya Akımı: ", battery_current, "A")
                    print("Kalan Batarya Kapasitesi: ", battery_remaining, "%")

                elif msg.get_type() == 'DISTANCE_SENSOR':
                    # simülasyonda yok. eğer pixhawkta da alınamıyorsa ik kalkış koordinatı el ile verilip hesaplanacak.
                    distance = msg.current_distance
                    print("Aracın ev konumuna olan mesafesi: ", distance, "m")

            data_thread = threading.Thread(target=self.data)
            data_thread.start()

    # verileri arayüzde gösterme
    def data(self):
        try:
            ui.altitude_LineEdit.setText(str(self.altitude))
            ui.groundSpeed_LineEdit.setText(str(self.groundSpeed))
            ui.groundSpeed_Qlcdnumber.display(str(self.groundSpeed))
            ui.verticalSpeed_LineEdit.setText(str(self.verticalSpeed))
            ui.yaw_LineEdit.setText(str(self.yaw))
            ui.latitude_Qlcdnumber.display(str(self.lat))
            ui.longtitude_Qlcdnumber.display(str(self.lon))
            ui.airSpeed_Qlcdnumber.display(str(self.airspeed))
            ui.disttoMav_LineEdit.setText(str(self.mode))
            # batarya
            ui.battery.setValue(self.value)
            son_deger = str(self.value) + "%"
            ui.batteryValue_lineEdit.setText(son_deger)
        except:
            
            pass

    def update_map(self):  # Konuma göre harita güncelleme
        pass

    # bağlantı koptuğunda ne yapmalı? hata mesajı vs. yazdırma.
    def disconnect(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    f = mainClass()
    MainWindow.show()

    # Uygulama döngüsünü başlat
    sys.exit(app.exec_())


