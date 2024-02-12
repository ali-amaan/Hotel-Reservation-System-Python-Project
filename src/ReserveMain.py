from PyQt5 import QtCore, QtWidgets
import csv
from PyQt5.QtWidgets import QMessageBox
from Classes.user_class import User_Class
from PyQt5.QtGui import QPixmap
from Classes.reserve_class import Reserve_Class
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ReserveWindow(QMainWindow):
        Reserve_main = 0
        Logout = 0
        
        ########## Initial Current User Data ##########
        userID = ''
        user_name = ''
        user_surname = ''
        user_point = ''
        ###############################################
        uid = User_Class() # Create Object from User_Class
        ###############################################
        
        def __init__(self, ReserveWindow, email, parent=None):
                super().__init__(parent) # to inherit from parent class
                self.Reserve_main = ReserveWindow
                login_user = 0
                with open('DataCSV/user_data.csv', newline='') as f: # Read current User's data
                        reader = csv.reader(f)
                        data = list(reader)  
                        for i in data:
                                if i[3] == email:
                                        login_user = i                        
                        userID = login_user[0]
                        self.uid.readById(userID)
                        self.user_name = self.uid.name
                        self.user_surname = self.uid.surname 
                ReserveWindow.setObjectName("ReserveWindow") # Set Object Name
                ReserveWindow.resize(1100, 750)
                ReserveWindow.setMinimumSize(QtCore.QSize(1100, 750))
                ReserveWindow.setMaximumSize(QtCore.QSize(1100, 750))
                self.centralwidget = QtWidgets.QWidget(ReserveWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.tabWidget = QtWidgets.QTabWidget(self.centralwidget) # Create Tab widget
                self.tabWidget.setGeometry(QtCore.QRect(10, 70, 1081, 641))
                self.tabWidget.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
        "font: 14pt \"MS Shell Dlg 2\";")
                self.tabWidget.setObjectName("tabWidget")
                self.tab = QtWidgets.QWidget()
                self.tab.setObjectName("tab")
                self.calendarWidget = QtWidgets.QCalendarWidget(self.tab) # Create Calendar
                self.calendarWidget.setGeometry(QtCore.QRect(30, 50, 781, 511))
                self.calendarWidget.setObjectName("calendarWidget")
                self.label_8 = QtWidgets.QLabel(self.tab)
                self.label_8.setGeometry(QtCore.QRect(860, 290, 156, 19))
                self.label_8.setObjectName("label_8")
                self.BookNow = QtWidgets.QPushButton(self.tab) # Create Button
                self.BookNow.setGeometry(QtCore.QRect(850, 500, 171, 41))
                self.BookNow.setStyleSheet("background-color: rgb(170, 255, 127);\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(0, 170, 255);\n"
        "background-color: rgb(0, 85, 255);")
                self.BookNow.setObjectName("BookNow")
                self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
                self.verticalLayoutWidget.setGeometry(QtCore.QRect(840, 70, 208, 117))
                self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
                self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.SelectRoom = QtWidgets.QComboBox(self.verticalLayoutWidget) # Create Combo Box
                self.SelectRoom.setObjectName("SelectRoom") 
                self.SelectRoom.addItem("")
                self.SelectRoom.addItem("")
                self.SelectRoom.addItem("")
                self.SelectRoom.addItem("")
                self.SelectRoom.addItem("")
                self.SelectRoom.addItem("")
                self.SelectRoom.addItem("")
                self.SelectRoom.addItem("")
                self.SelectRoom.addItem("")
                self.SelectRoom.addItem("")
                self.SelectRoom.addItem("")
                self.SelectRoom.addItem("")
                self.SelectRoom.addItem("")
                self.verticalLayout_4.addWidget(self.SelectRoom)
                spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_4.addItem(spacerItem)
                spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_4.addItem(spacerItem1)
                spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_4.addItem(spacerItem2)
                self.gridLayout = QtWidgets.QGridLayout()
                self.gridLayout.setObjectName("gridLayout")
                self.CheckIn = QtWidgets.QDateEdit(self.verticalLayoutWidget) # Create Qdateedit
                self.CheckIn.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
                self.CheckIn.setDateTime(QtCore.QDateTime.currentDateTime()) # Set Current Date
                self.CheckIn.setObjectName("CheckIn")
                self.gridLayout.addWidget(self.CheckIn, 0, 1, 1, 1)
                self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
                self.label_4.setObjectName("label_4")
                self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
                self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
                self.label_3.setObjectName("label_3")
                self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
                self.CheckOut = QtWidgets.QDateEdit(self.verticalLayoutWidget)
                self.CheckOut.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
                self.CheckOut.setDateTime(QtCore.QDateTime.currentDateTime().addDays(1)) # Set Current Date + 1 
                self.CheckOut.setObjectName("CheckOut")
                self.gridLayout.addWidget(self.CheckOut, 1, 1, 1, 1)
                self.verticalLayout_4.addLayout(self.gridLayout)
                self.layoutWidget = QtWidgets.QWidget(self.tab)
                self.layoutWidget.setGeometry(QtCore.QRect(880, 210, 114, 55))
                self.layoutWidget.setObjectName("layoutWidget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.verticalLayout = QtWidgets.QVBoxLayout()
                self.verticalLayout.setObjectName("verticalLayout")
                self.label_5 = QtWidgets.QLabel(self.layoutWidget)
                self.label_5.setObjectName("label_5")
                self.verticalLayout.addWidget(self.label_5)
                self.AdultsNumer = QtWidgets.QSpinBox(self.layoutWidget)
                self.AdultsNumer.setObjectName("AdultsNumer")
                self.verticalLayout.addWidget(self.AdultsNumer)
                self.horizontalLayout.addLayout(self.verticalLayout)
                spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout.addItem(spacerItem3)
                self.verticalLayout_2 = QtWidgets.QVBoxLayout() # Create Box layout
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.label_6 = QtWidgets.QLabel(self.layoutWidget)
                self.label_6.setObjectName("label_6")
                self.verticalLayout_2.addWidget(self.label_6)
                self.ChildrenNumber = QtWidgets.QSpinBox(self.layoutWidget)
                self.ChildrenNumber.setObjectName("ChildrenNumber")
                self.verticalLayout_2.addWidget(self.ChildrenNumber)
                self.horizontalLayout.addLayout(self.verticalLayout_2)
                self.layoutWidget1 = QtWidgets.QWidget(self.tab)
                self.layoutWidget1.setGeometry(QtCore.QRect(891, 320, 114, 161))
                self.layoutWidget1.setObjectName("layoutWidget1")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
                self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.addMeal = QtWidgets.QCheckBox(self.layoutWidget1) # Create Checkbox
                self.addMeal.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
                self.addMeal.setObjectName("addMeal")
                self.verticalLayout_3.addWidget(self.addMeal)
                self.addPick = QtWidgets.QCheckBox(self.layoutWidget1)
                self.addPick.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
                self.addPick.setObjectName("addPick")
                self.verticalLayout_3.addWidget(self.addPick)
                self.addCar = QtWidgets.QCheckBox(self.layoutWidget1)
                self.addCar.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
                self.addCar.setObjectName("addCar")
                self.verticalLayout_3.addWidget(self.addCar)
                self.addGrooming = QtWidgets.QCheckBox(self.layoutWidget1)
                self.addGrooming.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
                self.addGrooming.setObjectName("addGrooming")
                self.verticalLayout_3.addWidget(self.addGrooming)
                self.AddWellbeing = QtWidgets.QCheckBox(self.layoutWidget1)
                self.AddWellbeing.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
                self.AddWellbeing.setObjectName("AddWellbeing")
                self.verticalLayout_3.addWidget(self.AddWellbeing)
                self.tabWidget.addTab(self.tab, "")
                self.tab_2 = QtWidgets.QWidget()
                self.tab_2.setObjectName("tab_2")
                self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
                self.tableWidget.setGeometry(QtCore.QRect(30, 40, 1001, 451))
                self.tableWidget.setObjectName("tableWidget")
                self.tableWidget.setColumnCount(5)
                self.tableWidget.setRowCount(0)
                item = QtWidgets.QTableWidgetItem() # Create Table widget
                self.tableWidget.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(4, item)
                self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
                self.plainTextEdit.setGeometry(QtCore.QRect(760, 540, 141, 41))
                self.plainTextEdit.setObjectName("plainTextEdit")
                self.pushButton = QtWidgets.QPushButton(self.tab_2)
                self.pushButton.setGeometry(QtCore.QRect(920, 540, 121, 41))
                self.pushButton.setObjectName("pushButton")
                self.label_2 = QtWidgets.QLabel(self.tab_2)
                self.label_2.setGeometry(QtCore.QRect(750, 510, 301, 20))
                self.label_2.setStyleSheet("color: rgb(170, 0, 0);\n"
        "color: rgb(255, 0, 0);")
                self.label_2.setObjectName("label_2")
                self.tabWidget.addTab(self.tab_2, "")
                self.tab_4 = QtWidgets.QWidget()
                self.tab_4.setObjectName("tab_4")
                self.LogOut = QtWidgets.QPushButton(self.tab_4)
                self.LogOut.setGeometry(QtCore.QRect(970, 550, 81, 31))
                self.LogOut.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
                self.LogOut.setObjectName("LogOut")
                self.label_7 = QtWidgets.QLabel(self.tab_4)
                self.label_7.setGeometry(QtCore.QRect(380, 80, 671, 31))
                self.label_7.setObjectName("label_7")
                self.label_9 = QtWidgets.QLabel(self.tab_4)
                self.label_9.setGeometry(QtCore.QRect(380, 120, 691, 31))
                self.label_9.setObjectName("label_9")
                self.label_10 = QtWidgets.QLabel(self.tab_4)
                self.label_10.setGeometry(QtCore.QRect(380, 160, 691, 31))
                self.label_10.setObjectName("label_10")
                # self.label_11 = QtWidgets.QLabel(self.centralwidget)
                # self.label_11.setGeometry(QtCore.QRect(20, 30, 691, 31))
                # self.label_11.setObjectName("label_11")
                self.tabWidget.addTab(self.tab_4, "")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(880, 10, 201, 81))
                self.label.setText("")
                self.pixmap = QPixmap('Static/Y2_Logo.png')
                self.label.setPixmap(self.pixmap)
                self.label.setScaledContents(True)
                self.label.setObjectName("label")
                self.UserName_2 = QtWidgets.QLabel(self.centralwidget)
                self.UserName_2.setGeometry(QtCore.QRect(20, 20, 189, 23))
                self.UserName_2.setObjectName("UserName_2")
                ReserveWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(ReserveWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
                self.menubar.setObjectName("menubar")
                ReserveWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(ReserveWindow)
                self.statusbar.setObjectName("statusbar")
                ReserveWindow.setStatusBar(self.statusbar)
                self.Member_level = QtWidgets.QLabel(self.tab_4)
                self.Member_level.setGeometry(QtCore.QRect(380, 200, 691, 31))
                self.Member_level.setObjectName("Member_level")
                self.prop(ReserveWindow)
                self.tabWidget.setCurrentIndex(0)
                self.calendarWidget.clicked['QDate'].connect(self.CheckOut.setDate) # type: ignore
                self.calendarWidget.clicked['QDate'].connect(self.CheckIn.setDate) # type: ignore
                QtCore.QMetaObject.connectSlotsByName(ReserveWindow)

        def prop(self, ReserveWindow):
                _translate = QtCore.QCoreApplication.translate
                mem_point = int(self.uid.point)
                str_mem = 0
                if mem_point <= 100:
                        str_mem = 'Basic'
                elif mem_point > 100 and mem_point <= 250:
                        str_mem = 'Bronze'
                elif mem_point > 250 and mem_point <= 500:
                        str_mem = 'Silver'
                elif mem_point > 500:
                        str_mem = 'Gold'
                self.Member_level.setText(_translate("MainWindow", "Member Level : {} ({}) points".format(str_mem, self.uid.point)))
                ReserveWindow.setWindowTitle(_translate("ReserveWindow", "Reservation System"))
                self.label_8.setText(_translate("ReserveWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Additional Services</span></p></body></html>"))
                self.BookNow.setText(_translate("ReserveWindow", "Book Now!"))
                self.SelectRoom.setItemText(0, _translate("ReserveWindow", "Please Select Room")) # Set Room Number item for ComboBox
                self.SelectRoom.setItemText(1, _translate("ReserveWindow", "001"))
                self.SelectRoom.setItemText(2, _translate("ReserveWindow", "010"))
                self.SelectRoom.setItemText(3, _translate("ReserveWindow", "100"))
                self.SelectRoom.setItemText(4, _translate("ReserveWindow", "101"))
                self.SelectRoom.setItemText(5, _translate("ReserveWindow", "110"))
                self.SelectRoom.setItemText(6, _translate("ReserveWindow", "111"))
                self.SelectRoom.setItemText(7, _translate("ReserveWindow", "002"))
                self.SelectRoom.setItemText(8, _translate("ReserveWindow", "202"))
                self.SelectRoom.setItemText(9, _translate("ReserveWindow", "102"))
                self.SelectRoom.setItemText(10, _translate("ReserveWindow", "301"))
                self.SelectRoom.setItemText(11, _translate("ReserveWindow", "311"))
                self.SelectRoom.setItemText(12, _translate("ReserveWindow", "401"))
                self.CheckIn.setDisplayFormat(_translate("ReserveWindow", "d/M/yyyy"))
                self.label_4.setText(_translate("ReserveWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Check Out :</span></p></body></html>"))
                self.label_3.setText(_translate("ReserveWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Check In   :</span></p></body></html>"))
                self.CheckOut.setDisplayFormat(_translate("ReserveWindow", "d/M/yyyy"))
                self.label_5.setText(_translate("ReserveWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Adults</span></p></body></html>"))
                self.label_6.setText(_translate("ReserveWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Children</span></p></body></html>"))
                self.addMeal.setText(_translate("ReserveWindow", "Meal"))
                self.addPick.setText(_translate("ReserveWindow", "Pick and Drop"))
                self.addCar.setText(_translate("ReserveWindow", "Car"))
                self.addGrooming.setText(_translate("ReserveWindow", "Grooming"))
                self.AddWellbeing.setText(_translate("ReserveWindow", "Wellbeing"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ReserveWindow", "Reserve"))
                item = self.tableWidget.horizontalHeaderItem(0)
                item.setText(_translate("ReserveWindow", "Room Number"))
                item = self.tableWidget.horizontalHeaderItem(1)
                item.setText(_translate("ReserveWindow", "Check In"))
                item = self.tableWidget.horizontalHeaderItem(2)
                item.setText(_translate("ReserveWindow", "Check Out"))
                item = self.tableWidget.horizontalHeaderItem(3)
                item.setText(_translate("ReserveWindow", "Services"))
                item = self.tableWidget.horizontalHeaderItem(4)
                item.setText(_translate("ReserveWindow", "Total Price"))
                self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) # Set No Edit for table (read-only)
                self.tableWidget.setColumnWidth(0, 150) # set width size
                self.tableWidget.setColumnWidth(1, 170)
                self.tableWidget.setColumnWidth(2, 170)
                self.tableWidget.setColumnWidth(3, 385)
                self.load_book_list()
                self.pushButton.setText(_translate("ReserveWindow", "Select"))
                self.label_2.setText(_translate("ReserveWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Cancel Reservation : Type Room Number</span></p></body></html>"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ReserveWindow", "Booking List"))
                self.LogOut.setText(_translate("ReserveWindow", "Log Out"))
                self.label_7.setText(_translate("ReserveWindow", "Name : {} {}".format(self.uid.name, self.uid.surname)))
                self.label_9.setText(_translate("ReserveWindow", "E-mail : {}".format(self.uid.email)))
                self.label_10.setText(_translate("ReserveWindow", "Tel. : {}".format(self.uid.tel)))
                # self.label_11.setText(_translate("ReserveWindow", "Member Point : {}".format(self.uid.point)))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("ReserveWindow", "About"))
                #self.label.setText(_translate("ReserveWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Hotel Logo</span></p></body></html>"))
                self.UserName_2.setText(_translate("ReserveWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">User: {} {}</span></p></body></html>".format(self.user_name, self.user_surname)))
                self.AddWellbeing.setToolTip(_translate("MainWindow", "<html><head/><body><p>Add wellbeing services (advice and counselling) with your stay reservation. The price is $5.</p></body></html>"))
                self.addGrooming.setToolTip(_translate("MainWindow", "<html><head/><body><p>Add grooming services (hair, facial, and body care treatments) with your stay reservation. The price is $9.</p></body></html>"))
                self.LogOut.clicked.connect(self.openLogin) # Open Login Page for Logout button
                self.BookNow.clicked.connect(self.Booking) # Click BookNow
                self.addMeal.setToolTip(_translate("MainWindow", "<html><head/><body><p>Add a one-time meal per day with your stay reservation. The price is $7 per day.</p></body></html>"))
                self.addPick.setToolTip(_translate("MainWindow", "<html><head/><body><p>Add hotel pick and drop service to/from the airport or the railway station. The price is $12.</p></body></html>"))
                self.addCar.setToolTip(_translate("MainWindow", "<html><head/><body><p>Add a rental car with you stay reservation. The price is $20 per day.</p></body></html>"))
                self.pushButton.clicked.connect(self.delete_reserve) # Call delete_reserve function
                
                self.SelectRoom.currentIndexChanged.connect(self.Highlight) # Call Highlighting fucntion 
        
        ########################## Reset Calendar ###################################
        def resetCalendar(self, start, end):
                for j in range(start.daysTo(end)): # loop by start to end
                                self.calendarWidget.setDateTextFormat(start, QTextCharFormat()) # set style calendar as blank QTextCharFormat()
                                start = start.addDays(1) # increase day
                                
        last_start = QtCore.QDate.fromString('Apr-27-2001', "MMM-d-yyyy") # initial QDate
        last_end = QtCore.QDate.fromString('Apr-27-2100', "MMM-d-yyyy") # initial QDate
        ##############################################################################
        
                
        def Highlight(self):
                self.resetCalendar(self.last_start, self.last_end) # Reset Calendar before create new highlight
                aaa = self.SelectRoom.currentText() # get current text
                
                with open('DataCSV/reservation_data.csv', newline='') as f: # open user_data.csv to read lastest user
                        reader = csv.reader(f) 
                        data = list(reader)
                
                room = [] # Create list
                
                for same in data:
                        if same[2] == aaa: # Check same reserved room in reservation_data.csv
                                room.append(same) # append to list
                
                num = len(room) # Get number of same room
                CheckIn = [] # Create list
                CheckOut = [] # Create list
                highlight_format = QTextCharFormat() # Create QTextCharFormat() as highlight_format
                highlight_format.setBackground(QtGui.QColor("red")) # set color
                highlight_format.setForeground(self.palette().color(QPalette.HighlightedText)) # set text color
                
                for day in room:
                        CheckIn.append(day[3][4:].replace(' ', '-')) # loop in data and get check in date and append to list
                        CheckOut.append(day[4][4:].replace(' ', '-')) # loop in data and get check out date and append to list
                        
                # self.CheckIn.date().daysTo(self.CheckOut.date())

                for i in range(num): # loop bt range of number
                        dateStart = QtCore.QDate.fromString(CheckIn[i], "MMM-d-yyyy") # Create Qdate from string
                        dateEnd = QtCore.QDate.fromString(CheckOut[i], "MMM-d-yyyy") # Create Qdate from string
                        
                        # self.last_start = dateStart # set global variable for reset next time
                        # self.last_end = dateEnd # set global variable for reset next time
                        
                        for j in range(dateStart.daysTo(dateEnd)): # loop for from date start to check out 
                                self.calendarWidget.setDateTextFormat(dateStart, highlight_format) # highlight fate
                                dateStart = dateStart.addDays(1) # add day
        
        def show_message(self, text): # Show Message Box
                msg = QMessageBox()
                msg.setWindowTitle('Message Box')
                msg.setText(text)
                # msg.setIcon(QMessageBox.Information)
                
                x = msg.exec_()

        def openLogin(self): # Open Login Page
                from LogInMain import LoginWindow
                self.window = QtWidgets.QMainWindow()
                self.ui = LoginWindow(self.window)
                self.window.show()
                self.Reserve_main.close()
                
        def Confirm_Book(self):
                dialog = QMessageBox() # Create QMessageBox as dialog
                period = self.CheckIn.date().daysTo(self.CheckOut.date()) # period = checkout - checkin
                meal,pick,car,groom,well = 0,0,0,0,0 # initial additional services
                
                if self.addMeal.isChecked():
                        meal = 7*period
                if self.addPick.isChecked():
                        pick = 12
                if self.addCar.isChecked():
                        car = 20 * period
                if self.addGrooming.isChecked():
                        groom = 9
                if self.AddWellbeing.isChecked():
                        well = 5     
                        
                point = 0 # initial point
                
                with open('DataCSV/user_data.csv', newline='') as f: # open user_data.csv to read latest user
                        reader = csv.reader(f)
                        data = list(reader)
                        
                        for i in data:
                                if i[0] == self.uid.Id: # Check currently logged in user
                                        point = int(i[-1]) # read point
                                        
                discount = 0 # initial discount
                price_before = (period * 40) + meal + pick + car + groom + well
                
                if point <= 100:
                        discount = 0
                elif point > 100 and point <= 250:
                        discount = 5
                elif point > 250 and point <= 500:
                        discount = 10
                elif point > 500:
                        discount = 15
                        
                dis_dollar = price_before * (discount / 100)
                
                total_price = self.ConfirmPrice() # Call function ConfirmPrice()
                
                # show dialog on confirm pop-up
                dialog.setText('PRICE BREAKDOWN\nDuration (Days): {}\nRoom Charge: ${}\nMeal: ${}\nPick & Drop: ${}\nRent a Car: ${}\nGroom & Care: ${}\nWellbeing: ${}\nDiscount %: {}\nDiscount: ${}\nTotal Price: {}'.format(period, period*40,meal,pick,car,groom,well,discount,dis_dollar,total_price))
                dialog.setWindowTitle('Confirmation of Reservation')
                dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                dialog.buttonClicked.connect(self.Dialog_Click) # Call Dialog_Click
                
                dialog.exec()
        
        def Dialog_Click(self, clicked):
                if clicked.text() == 'OK': # if Click OK
                        additional = [
                                self.addMeal.isChecked(), # Check add-on
                                self.addPick.isChecked(), # Check add-on
                                self.addCar.isChecked(), # Check add-on
                                self.addGrooming.isChecked(), # Check add-on
                                self.AddWellbeing.isChecked() # Check add-on
                        ]
                        total_price = self.ConfirmPrice() # Confirm Price
                        ure = Reserve_Class(
                                        userId=self.uid.Id, # set User ID 
                                        RoomNumber=self.SelectRoom.currentText(), # set RoomNumber
                                        r_start=self.CheckIn.date().toString(), # set check in
                                        r_end=self.CheckOut.date().toString(), # set check out
                                        period=self.CheckIn.date().daysTo(self.CheckOut.date()), # set period
                                        add_on=additional, # set add-ons
                                        n_adult=self.AdultsNumer.text(), # set number of adult
                                        n_children=self.ChildrenNumber.text() # set number of child
                                )
                        ure.total_price = total_price # set price
                        ure.appendReserve() # append reservation
                        self.load_book_list() # load table list
                        
                        with open('DataCSV/user_data.csv', newline='') as f:
                                reader = csv.reader(f)
                                data = list(reader)
                                
                        for i in data:
                                if i[3] == self.uid.email: # check currently user's email
                                        i[-1] = int(int(i[-1]) + total_price) # add point
                                        _translate = QtCore.QCoreApplication.translate
                                        mem_point = int(i[-1])
                                        str_mem = 0
                                        if mem_point <= 100:
                                                str_mem = 'Basic'
                                        elif mem_point > 100 and mem_point <= 250:
                                                str_mem = 'Bronze'
                                        elif mem_point > 250 and mem_point <= 500:
                                                str_mem = 'Silver'
                                        elif mem_point > 500:
                                                str_mem = 'Gold'
                                        # show member level
                                        self.Member_level.setText(_translate("MainWindow", "Member Level : {} ({}) points".format(str_mem, i[-1])))
                
                        with open('DataCSV/user_data.csv', 'w', newline='') as f:
                                        fw = csv.writer(f)
                                        fw.writerows(data) # write new update
                        
                        self.Highlight() # highlight book
        
        def ConfirmPrice(self):
                price = 0 # initial price
                period = self.CheckIn.date().daysTo(self.CheckOut.date())
                price = period * 40
                
                if self.addMeal.isChecked():
                        price = price + (7 * period)
                if self.addPick.isChecked():
                        price = price + 12
                if self.addCar.isChecked():
                        price = price + (20 * period)
                if self.addGrooming.isChecked():
                        price = price + 9
                if self.AddWellbeing.isChecked():
                        price = price + 5
                
                before = price
                point = 0
                
                with open('DataCSV/user_data.csv', newline='') as f: # open user_data.csv to read lastest user
                        reader = csv.reader(f)
                        data = list(reader)
                        
                        for i in data:
                                if i[0] == self.uid.Id: # check user id and point to get discount
                                        point = int(i[-1])
                
                discount = 0
                
                if point <= 100:
                        discount = 0
                elif point > 100 and point <= 250:
                        discount = 5
                elif point > 250 and point <=500:
                        discount = 10
                elif point > 500:
                        discount = 15
                
                price = price - (price * (discount / 100))
                
                return price
                
                # Basic (0-100) = 0% discount
                # Bronze (100-250) = 5% discount
                # Silver (250-500) = 10% discount
                # Gold (500 & above) = 15% discount
                
        def Booking(self): # Booking function
                
                AdultNerverZero = self.AdultsNumer.text() # Check Adult have at least 1
                AdultNerverZero = int(AdultNerverZero)
                # self.checkAvailable()
                
                additional = [
                                self.addMeal.isChecked(),
                                self.addPick.isChecked(),
                                self.addCar.isChecked(),
                                self.addGrooming.isChecked(),
                                self.AddWellbeing.isChecked()
                        ]

                if self.SelectRoom.currentText() != 'Please Select Room' and self.CheckIn.date().daysTo(self.CheckOut.date()) >=1 and AdultNerverZero > 0 and self.NewCheckAvailible():
                        self.Confirm_Book() # call function Confirm_Book() 
                        
                elif self.SelectRoom.currentText() == 'Please Select Room':
                        self.show_message('Please select room before booking') # show message if user doesn't select room
                        
                elif not self.NewCheckAvailible():
                        
                        list_same_room = [] # Create list
                        
                        with open('DataCSV/reservation_data.csv', newline='') as f: # open user_data.csv to read lastest user
                                reader = csv.reader(f)
                                data = list(reader)
                                
                                for i in data:
                                        if self.SelectRoom.currentText() == i[2]: # Check same room in reservation_data.csv
                                                list_same_room.append(i) # append to list
                                                
                        message = 'This room has been reserved according to these day\n'
                        
                        for i in list_same_room:
                                day = 'Check In: {} | Check Out: {}\n'.format(i[3], i[4]) # show if room was reserved
                                message = message + day
                        
                        self.show_message(message)
                        
                elif self.CheckIn.date().daysTo(self.CheckOut.date()) < 1: # Check if check out less than check in
                        self.show_message('Check Out date much more than Check In date')
                        
                elif AdultNerverZero <= 0: # Adult can not be 0
                        self.show_message('Adult must at least 1')
                        
        def NewCheckAvailible(self):
                RoomNumber = self.SelectRoom.currentText() # get current select room
                new_checkIn = self.CheckIn.date() # get check in date
                new_checkOut = self.CheckOut.date() # get check out date
                
                status = [] # Create list       
                same_room = [] # Create list 
                
                with open('DataCSV/reservation_data.csv', newline='') as f: # open user_data.csv to read lastest user
                        reader = csv.reader(f)
                        data = list(reader)
                        
                for i in data:
                        if i[2] == RoomNumber: # Check same room
                                same_room.append(i) # append to list
                
                if len(same_room) < 1: # if no same room mean room never be reserve
                        return True
                else:
                        for i in same_room:
                                checkIn, checkOut = i[3], i[4] # Get check in, check out
                                checkIn = checkIn[4:].replace(' ', '-') # replace space by -
                                checkOut = checkOut[4:].replace(' ', '-') # replace space by -
                                
                                qdateCheckIn = QtCore.QDate.fromString(checkIn, "MMM-d-yyyy") # Create Qdate from string
                                qdateCheckOut = QtCore.QDate.fromString(checkOut, "MMM-d-yyyy") # Create Qdate from string
                                
                                P_checkin = QtWidgets.QDateEdit() # Create QdateEdit
                                P_checkin.setDate(qdateCheckIn) 
                                P_checkin.setObjectName("P_checkout")
                                
                                P_checkout = QtWidgets.QDateEdit() # Create QdateEdit
                                P_checkout.setDate(qdateCheckOut) 
                                P_checkout.setObjectName("P_checkiout")
                                
                                # if PreviousCheckOut.date().daysTo(Want_checkIn) >= 0:
                                
                                if P_checkin.date().daysTo(new_checkIn) == 0:
                                        status.append(False)
                                elif P_checkout.date().daysTo(new_checkIn) >= 0:
                                        status.append(True)
                                elif P_checkout.date().daysTo(new_checkIn) < 0:
                                        if P_checkin.date().daysTo(new_checkOut) <= 0:
                                                status.append(True)
                                        else :
                                                status.append(False)
                        
                        if (False in status): # if False in status mean if in the same room you want to book have day was booked so this room can not be book
                                return False
                        else :
                                return True
                        
        def Convert(self, string): # Convert string []
                li = list(string.split(", ")) # Split string by comma
                return li
        
        def delete_reserve(self): # Delete reserve function
                with open('DataCSV/reservation_data.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        
                that_index = 100 # initial value
                range_a = len(data)
                
                for i, row in enumerate(data):
                        if row[2] == self.plainTextEdit.toPlainText() and row[1] == self.uid.Id: # Check user ID
                                that_index = i
                
                new_list = []
                for i in range(range_a ):
                        if i != that_index:
                                new_list.append(data[i])
                
                with open('DataCSV/reservation_data.csv', 'w', newline='') as f:
                                fw = csv.writer(f)
                                fw.writerows(new_list)
                
                self.Highlight() # call highlight
                self.load_book_list() # load table
                self.plainTextEdit.setPlainText("") # set blank text     
                        
        def load_book_list(self): # lood booking list for table
                
                your_book_list = [] # Create list
                
                with open('DataCSV/reservation_data.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        #print(data)
                        
                        for row in data:
                                if row[1] == self.uid.Id: # Check user ID
                                        your_book_list.append(row)
                        
                
                row = 0
                self.tableWidget.setRowCount(len(your_book_list))
                for l in your_book_list:
                        A_list = self.Convert(l[8][1:-1]) 
                        strt = ""
                        for i, r in enumerate(A_list): # loop display additional services
                                if r == 'True' and i == 0:
                                        strt = strt + "Meal "
                                elif r =='True' and i == 1:
                                        strt = strt + "Pick and Drop "
                                elif r =='True' and i == 2:
                                        strt = strt + "Car "
                                elif r =='True' and i == 3:
                                        strt = strt + "Grooming "
                                elif r =='True' and i == 4:
                                        strt = strt + "Wellbeing "

                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(l[2])) # set row for 1st column
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(l[3])) # set row for 2nd column
                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(l[4])) # set row for 3rd column
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(strt)) # set row for 4th column
                        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(l[-2])) # set row for 5th column
                        row = row + 1


