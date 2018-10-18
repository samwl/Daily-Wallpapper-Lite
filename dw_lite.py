"""
Daily Wallpapper Lite
ver. 0.10
Smirnov Alexey
https://github.com/samwl
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtCore import Qt, QTimer, QRect, QPoint, QThread

#import datetime, os, random, requests, bs4, sys
import sys, os, urllib.request, json, ctypes
from win10toast import ToastNotifier

class Notifi(QThread):
    def __init__(self, *args, **kwargs):
        super(Notifi, self).__init__(*args, **kwargs)
    def run(self):
        js = urllib.request.urlopen('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1')
        js_obj = json.load(js)
        url = 'http://www.bing.com' + js_obj['images'][0]['url']
        wall_name = js_obj['images'][0]['copyright']
        js.close()
        logo = os.getcwd() + os.sep + 'img/' + 'icoo.ico'
        toaster = ToastNotifier()
        toaster.show_toast("Daily Wallpapper Lite",
                        wall_name,
                        icon_path=logo,
                        duration=30)
        
class N_connect(QThread):
    def __init__(self, *args, **kwargs):
        super(N_connect, self).__init__(*args, **kwargs)
    def run(self):
        toaster = ToastNotifier()
        toaster.show_toast("Daily Wallpapper Lite",
                        "No internet connection \n Please check your internet connection and try again",
                        icon_path="icoo.ico",
                        duration=10)       

class Set_wall(QThread):
    def __init__(self, *args, **kwargs):
        super(Set_wall, self).__init__(*args, **kwargs)
    def run(self):
        js = urllib.request.urlopen('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1')
        js_obj = json.load(js)
        url = 'http://www.bing.com' + js_obj['images'][0]['url']
        js.close()
        img = urllib.request.urlopen(url).read()
        name_jpg = os.getcwd() + os.sep + 'dw.jpg'
        out = open(name_jpg, "wb")
        out.write(img)
        out.close()      
        SPI_SETDESKWALLPAPER = 20 
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, name_jpg, 0)

class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel(self)
        self.label.setGeometry(QRect(0, 0, 400, 300))
        self.label.setAlignment(Qt.AlignHCenter| Qt.AlignVCenter)
        load_p = os.getcwd() + os.sep + 'gif/'+ '1f.gif'
        movie = QMovie(load_p)
        self.label.setMovie(movie)
        movie.start()

        self.button6 = QPushButton(self)
        self.button6.clicked.connect(self.final_animation)
        self.button6.move(370, 270)
        self.button6.setMaximumHeight(30)
        self.button6.setMaximumWidth(30)
        self.button6.setStyleSheet("""
        QPushButton:!hover { border-image: url(img/cl.png) 10 10 10 10; border-top: 10px transparent; border-bottom: 10px transparent;
            border-right: 10px transparent; border-left: 10px transparent;}
        QPushButton:hover { border-image: url(img/cl_h.png) 10 10 10 10; border-top: 10px transparent; border-bottom: 10px transparent;
            border-right: 10px transparent; border-left: 10px transparent;}
        QPushButton:pressed { border-image: url(img/cl_p.png) 10 10 10 10; border-top: 10px transparent; border-bottom: 10px transparent;
            border-right: 10px transparent; border-left: 10px transparent;} """)

        self.label_title = QLabel(self)
        self.label_title.setGeometry(QRect(0, 270, 150, 30))
        self.label_title.setStyleSheet("background:transparent; font: 10pt \"Segoe UI\"; color: #555;")
        self.label_title.setAlignment(Qt.AlignHCenter| Qt.AlignVCenter) 
        self.label_title.setText("Daily Wallpapper Lite")


        self.setWindowTitle('Daily Wallpapper Lite')
        logo = os.getcwd() + os.sep + 'img/' + 'icoo.ico'
        self.setWindowIcon(QIcon(logo))
        self.setFixedSize(400, 300)
        self.setStyleSheet("background: #fff; font: 10pt \"Segoe UI\";")
        self.setWindowFlags(Qt.CustomizeWindowHint)
        QTimer.singleShot(2000, self.main)
        

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def quit_e(self):
        app.quit()

    def notifi(self):
        self.task = Notifi(self)
        self.task.start()

    def error_noti(self):
        self.task = N_connect(self)
        self.task.start()

    def set_wall(self):
        self.task = Set_wall(self)
        self.task.start()

    def pars_try(self):
        js = urllib.request.urlopen('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1')
        
    def animation_2(self):
        my = os.getcwd() + os.sep + 'gif/'+ '2f.gif'
        movie_y = QMovie(my)
        self.label.setMovie(movie_y)
        self.label.setScaledContents(False)
        movie_y.start()
        QTimer.singleShot(300, self.animation_2_freez) 

    def animation_2_freez(self):
        my = os.getcwd() + os.sep + 'gif/'+ '2fx.gif'
        movie_y = QMovie(my)
        self.label.setMovie(movie_y)
        self.label.setScaledContents(False)
        movie_y.start()

    def animation_3(self):
        my = os.getcwd() + os.sep + 'gif/'+ 'ef.gif'
        movie_y = QMovie(my)
        self.label.setMovie(movie_y)
        self.label.setScaledContents(False)
        movie_y.start()

    def final_animation(self):
        my = os.getcwd() + os.sep + 'gif/'+ 'ff2.gif'
        movie_y = QMovie(my)
        self.label.setMovie(movie_y)
        self.label.setScaledContents(False)
        movie_y.start()
        QTimer.singleShot(1000, self.quit_e)        

    def main(self):
        try:
            self.pars_try()
        except urllib.error.URLError:
            self.error_noti()
            self.animation_3()
            QTimer.singleShot(6000, self.quit_e)
        else:
            QTimer.singleShot(2000, self.set_wall)
            QTimer.singleShot(3000, self.notifi)
            QTimer.singleShot(3000, self.animation_2)
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())