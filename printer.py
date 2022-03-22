#!/usr/bin/python3

import threading
import time
import requests
import json
import win32api
import win32print
import win32con
import traceback
import serial
import sqlite3
from PIL import Image
import os
import os.path
import sys
import wmi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout

global scanresult
global printvariable
global machinename
global machineaddress
global machineid
global Remainingpapers
global secret


class Gettask(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        gettask()


class UI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        ui()


class Qrcode(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        qrcode()


class Ui_cloudprinter(object):
    global printvariable
    global Remainingpapers

    def setupUi(self, cloudprinter):
        cloudprinter.setObjectName("cloudprinter")
        cloudprinter.setWindowModality(QtCore.Qt.NonModal)
        cloudprinter.resize(1024, 600)
        cloudprinter.setMinimumSize(QtCore.QSize(1024, 600))
        cloudprinter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        cloudprinter.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        cloudprinter.setWindowState(QtCore.Qt.WindowMaximized)
        font = QtGui.QFont()
        font.setFamily("造字工房悦黑体验版纤细体")
        cloudprinter.setFont(font)
        cloudprinter.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        cloudprinter.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(cloudprinter)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 60, 681, 101))
        font = QtGui.QFont()
        font.setFamily("造字工房悦黑体验版纤细体")
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 153, 204);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 150, 731, 101))
        font = QtGui.QFont()
        font.setFamily("造字工房悦黑体验版纤细体")
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 153, 204);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 290, 1011, 81))
        font = QtGui.QFont()
        font.setFamily("造字工房悦黑体验版纤细体")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 153, 204);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 460, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 153, 204);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 530, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 153, 204);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 500, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 153, 204);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(820, 350, 201, 211))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("C:\\Users\\alpha1066\\Desktop\\码.png"))
        self.label_7.setObjectName("label_7")
        cloudprinter.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(cloudprinter)
        self.statusbar.setObjectName("statusbar")
        cloudprinter.setStatusBar(self.statusbar)

        self.retranslateUi(cloudprinter)
        QtCore.QMetaObject.connectSlotsByName(cloudprinter)

    def retranslateUi(self, cloudprinter):
        global printvariable
        global Remainingpapers
        printvariable = "请扫码 开始打印"
        _translate = QtCore.QCoreApplication.translate
        cloudprinter.setWindowTitle(_translate("cloudprinter", "云上印记"))
        self.label.setText(_translate("cloudprinter", "Hi 我是云上印记"))
        self.label_2.setText(_translate("cloudprinter", "来自未来的自助打印机"))
        self.label_3.setText(_translate("cloudprinter", printvariable))
        self.label_4.setText(_translate("cloudprinter", Remainingpapers))
        self.label_5.setText(_translate("cloudprinter", machineaddress))
        self.label_6.setText(_translate("cloudprinter", machinename))

    def run(self):
        global printvariable
        global Remainingpapers
        while 1:
            self.label_3.setText(QtCore.QCoreApplication.translate("cloudprinter", printvariable))
            self.label_4.setText(QtCore.QCoreApplication.translate("cloudprinter", str(Remainingpapers)))
            time.sleep(0.5)
            QApplication.processEvents()


def qrcode():
    global printvariable
    global machineid
    global Remainingpapers
    global scanresult
    global secret
    portx = "COM3"
    # 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
    bps = 115200
    # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
    timex = 1
    # 打开串口，并得到串口对象
    while 1:
        try:
            ser = serial.Serial(portx, bps, timeout=timex)
            while True:
                if ser.in_waiting:
                    scanresult = ser.read(8).decode("gbk")
                    admincode = VigenereDecrypto(scanresult, "printer").split(".")
                    print(VigenereDecrypto(scanresult, "printer"))
                    if admincode[0] == "Addp":
                        machineid = admincode[1]
                        updata(machineid, Remainingpapers)
                        break
                    printvariable = scanresult
                    print("收到数据：", scanresult)
                    break
            ser.close()  # 关闭串口
        except Exception:
            print("扫码器异常，请检查串口参数是否输入正确！")


        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        sql = "SELECT * FROM task WHERE pw ='%s'" % scanresult
        cursor.execute(sql)
        results = cursor.fetchone()

        if results:
            print(results)
            filetype = results[2].split(".")
            if filetype[1] == "jpg" or filetype[1] == "png" or filetype[1] == "bmp":
                im = Image.open(results[2])
                print("图片分辨率:", im.size[0], im.size[1])
                if im.size[0] < im.size[1]:
                    out = im.transpose(Image.ROTATE_90)
                    out.save(results[2])
            printvariable = "正在打印 请注意取件"
            PRINTER_DEFAULTS = {"DesiredAccess": win32print.PRINTER_ALL_ACCESS}
            pHandle = win32print.OpenPrinter(win32print.GetDefaultPrinter(), PRINTER_DEFAULTS)
            properties = win32print.GetPrinter(pHandle, 2)
            properties['pDevMode'].Color = results[3]
            properties['pDevMode'].Copies = results[5]
            properties['pDevMode'].Orientation = win32con.DMORIENT_PORTRAIT
            print(properties['pDevMode'].Copies)
            properties['pDevMode'].Duplex = results[4]
            win32print.SetPrinter(pHandle, 2, properties, 0)
            win32api.ShellExecute(0, "print", 'files\\' +results[2], None, ".", 0)
            win32print.ClosePrinter(pHandle)
            sql = "DELETE FROM task WHERE id=%s" % results[0]
            cursor.execute(sql)
            db.commit()
            db.close()
            url = "https://print.mauac.com/finishTask.php"
            payload = {"machine": machineid, "tid": results[0], "secret": secret}
            requests.post(url=url, data=payload)
            Remainingpapers = int(Remainingpapers) - results[8]
            updata(machineid, Remainingpapers)
            time.sleep(30)
            printvariable = "请扫码 开始打印"


def ui():
    app = QtWidgets.QApplication(sys.argv)
    cloudprinter = QtWidgets.QMainWindow()
    ui = Ui_cloudprinter()
    ui.setupUi(cloudprinter)
    cloudprinter.show()
    Ui_cloudprinter.run(ui)
    sys.exit(app.exec_())


def updata(Id, paper):
    try:
        fn = open("config.txt", "w")
        str1 = str(Id) + "." + str(paper)
        fn.write(str1)
        fn.close()
    except Exception:
        print("配置文件写入失败")


def VigenereDecrypto(output, key):
    ptLen = len(output)
    keyLen = len(key)
    quotient = int(ptLen / keyLen)
    remainder = ptLen % keyLen
    inp = ""
    for i in range(0, quotient):
        for j in range(0, keyLen):
            c = int((ord(output[i * keyLen + j]) - ord('a') + 26 - (ord(key[j]) - ord('a'))) % 26 + ord('a'))
            inp += chr(c)
    for i in range(0, remainder):
        c = int((ord(output[quotient * keyLen + i]) - ord('a') + 26 - (ord(key[i]) - ord('a'))) % 26 + ord('a'))
        inp += chr(c)
    return inp


def gettask():
    global secret
    global printvariable
    global machineid
    while 1:
        # ------------------------------------------获取任务
        url = "https://print.mauac.com/getTask.php"
        payload = {"machine": machineid, "secret": secret}
        try:
            response = requests.post(url=url, data=payload, timeout=10)
        except requests.exceptions.RequestException as e:
            print(e)
            print('失败')
            continue
        result = json.loads(response.text)
        print(result)
        # --------------------------------------------储存到数据库
        if response:
            for i in result:
                print(i)
                db = sqlite3.connect('database.db')
                cursor = db.cursor()
                sql = """INSERT INTO task(id,status,
                         filename,color,side,copies,mode,pw,paper)
                         VALUES (%s,%s,'%s',%s,%s,%s,%s,'%s',%s)""" % \
                      (i["id"], i["status"], i["filename"], i["color"], i["side"], i["copies"], i["mode"], i["pw"],
                       i["page"])
                cursor.execute(sql)
                db.commit()
                db.close()
                # ----------------------------------------下载文件
                downloadurl = "https://print-1303205921.cos.ap-beijing.myqcloud.com/"
                try:
                    r = requests.get(downloadurl + i["filename"], timeout=2)
                except Exception:
                    printvariable = "错误:检查网络"

                with open('files\\' + i["filename"], 'wb') as f:
                    f.write(r.content)
                # -------------------------------------------记录下载过任务
                url = "https://print.mauac.com/recordTask.php"
                payload = {"machine": "1", "tid": i["id"], "secret": secret}
                requests.post(url=url, data=payload)
        time.sleep(5)


if __name__ == "__main__":

    with open('config.txt', 'r') as f:
        machineconfig = f.read().split(".")
        machineid = machineconfig[0]
        Remainingpapers = machineconfig[1]
        print(Remainingpapers)
        f.close()
    secret = wmi.WMI().Win32_OperatingSystem()[0].SerialNumber
    print(machineid)
    print(secret)
    baseurl = 'https://print.mauac.com/getMachineInfo.php?'
    params = {'machine': machineid, "secret": secret}
    res = requests.get(baseurl, params=params)
    res = json.loads(res.text)
    print(res)
    machinename = res["name"]
    machineaddress = res["address"]

    # 创建新线程
    thread1 = Gettask()
    thread2 = UI()
    thread3 = Qrcode()

    # 开启新线程
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
