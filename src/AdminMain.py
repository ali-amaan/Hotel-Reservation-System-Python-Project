from PyQt5 import QtCore, QtWidgets
import csv
from PyQt5.QtWidgets import QMainWindow

class AdminWindow(QMainWindow):

    # set initial
##############################
    AdminMain = 0
    user_state_sort = 0
    reserve_state_sort = 0
##############################

    def __init__(self, AdminWindow, parent=None):
        super().__init__(parent) # to inherit from parent class
        self.AdminMain = AdminWindow
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(1219, 553)
        self.centralwidget = QtWidgets.QWidget(AdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1191, 461))
        self.tabWidget.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 1141, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(780, 390, 141, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(930, 390, 131, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(1070, 390, 81, 23))
        self.pushButton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 390, 91, 23))
        self.pushButton_2.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 20, 1141, 351))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(9)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(1070, 390, 81, 23))
        self.pushButton_3.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(930, 390, 131, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(830, 390, 91, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 390, 91, 23))
        self.pushButton_4.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.LogOut = QtWidgets.QPushButton(self.centralwidget)
        self.LogOut.setGeometry(QtCore.QRect(560, 490, 75, 23))
        self.LogOut.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.LogOut.setObjectName("LogOut")
        AdminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1219, 21))
        self.menubar.setObjectName("menubar")
        AdminWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminWindow)
        self.statusbar.setObjectName("statusbar")
        AdminWindow.setStatusBar(self.statusbar)

        self.prop(AdminWindow) # Call prop function
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def prop(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "Admin Dashboard"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AdminWindow", "User_ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AdminWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AdminWindow", "Surname"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("AdminWindow", "E-mail"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("AdminWindow", "Tel."))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("AdminWindow", "Password"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("AdminWindow", "Point"))
        self.label.setText(_translate("AdminWindow", "Delete By User_ID"))
        self.pushButton.setText(_translate("AdminWindow", "Submit"))
        self.pushButton_2.setText(_translate("AdminWindow", "Sort By Latest"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("AdminWindow", "User_data"))
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setColumnWidth(0, 70)
        self.tableWidget.setColumnWidth(1, 170)
        self.tableWidget.setColumnWidth(2, 170)
        self.tableWidget.setColumnWidth(3, 280)
        self.tableWidget.setColumnWidth(4, 195)
        self.tableWidget.setColumnWidth(5, 170)
        self.tableWidget.setColumnWidth(6, 80)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("AdminWindow", "ID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("AdminWindow", "Room_number"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("AdminWindow", "User_ID"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("AdminWindow", "Check In"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("AdminWindow", "Check Out"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("AdminWindow", "Adults"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("AdminWindow", "Children"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("AdminWindow", "Services"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("AdminWindow", "Price"))
        self.pushButton_3.setText(_translate("AdminWindow", "Submit"))
        self.label_2.setText(_translate("AdminWindow", "Delete By ID"))
        self.pushButton_4.setText(_translate("AdminWindow", "Sort By Latest"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("AdminWindow", "Reservation_data"))
        self.tableWidget_2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget_2.setColumnWidth(0, 50) # set table width
        self.tableWidget_2.setColumnWidth(1, 120)
        self.tableWidget_2.setColumnWidth(2, 80)
        self.tableWidget_2.setColumnWidth(3, 170)
        self.tableWidget_2.setColumnWidth(4, 170)
        self.tableWidget_2.setColumnWidth(5, 70)
        self.tableWidget_2.setColumnWidth(6, 70)
        self.tableWidget_2.setColumnWidth(7, 330)
        self.tableWidget_2.setColumnWidth(8, 60)
        
        self.LogOut.setText(_translate("AdminWindow", "Log out"))
        self.LogOut.clicked.connect(self.Login) # Call login function
        self.load_user_data() # Call load_user_data function
        self.load_reserve_data() # Call reserve_data function
        self.pushButton.clicked.connect(self.delete_user_Id) # Connect function when click
        self.pushButton_2.clicked.connect(self.sort_user_data)
        self.pushButton_3.clicked.connect(self.delete_reserve_Id)
        self.pushButton_4.clicked.connect(self.sort_reserve_data)

    def delete_user_Id(self): # Delete user data by ID
        data_list = [] # Create blank list data_list
        replace_list = [] # Create blank list replace_list
        #print(self.uid.Id)
                
        with open('DataCSV/user_data.csv', newline='') as f: # open user_data.csv
                reader = csv.reader(f) # Read csv as reader
                data = list(reader) # Turn reader into data list
                #print(data)
                for r in data: # for loop in data
                    data_list.append(r) # append r to data_list
                    
        user_d_text = self.lineEdit.text() # get user ID text
        
        for i in data_list: # loop in data_list
            if i[0] != user_d_text: # if ID != target uer ID
                replace_list.append(i) # append replace list
        
        with open('DataCSV/user_data.csv', 'w', newline='') as f: # open user_data.csv
                                fw = csv.writer(f) # set csv_writer as fw
                                fw.writerows(replace_list) # write replace list
        
        self.load_user_data() # load user data again to update table
        self.lineEdit.setText("") # set input to blank
        
    def sort_user_data(self): # Sort user by latest
        if self.user_state_sort == 0: # check that if user data are sorted or not
            data_list = [] # Create blank data_list
            with open('DataCSV/user_data.csv', newline='') as f: # open user_data.csv
                    reader = csv.reader(f) # read csv to reader
                    data = list(reader) # turn reader to list data
                    #print(data)
                    for r in data: # for in data
                        data_list.append(r) # append r in data_list
            
            new_list = [] # Create list new_list
            range_a = len(data_list) # find length of data_list
            reverse_index = -1 # reverse_index = latest index
            for i in range(range_a): # for loop by length 
                new_list.append(data_list[reverse_index]) # append data by latest index first
                reverse_index = reverse_index -1 # increase index
                
            row = 0 # initial row value
            self.tableWidget.setRowCount(len(new_list)) # Create tableWidget by length new_list
            for l in new_list:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(l[0])) # set row for 1st column
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(l[1])) # set row for 2nd column
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(l[2])) # set row for 3rd column
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(l[3])) # set row for 4th column
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(l[4])) # set row for 5th column
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(l[5])) # set row for 6th column
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(l[6])) # set row for 7th column
                    row = row + 1
            self.user_state_sort = 1 # set user_state = 1
        else:
            self.user_state_sort = 0 # set user_state = 0
            self.load_user_data() # Load_user_data for update table
            
    def load_user_data(self): # load user data to table
        data_list = [] # initial data list
                #print(self.uid.Id)
                
        with open('DataCSV/user_data.csv', newline='') as f: # open user_data.csv
                reader = csv.reader(f) # Read csv as reader
                data = list(reader) # turn reader into list 
                #print(data)
                for r in data: # loop in data
                    data_list.append(r) # append r to data_list
                    
        
        row = 0 # intial row value
        self.tableWidget.setRowCount(len(data_list)) # Create tableWidget by length new_list
        for l in data_list:        
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(l[0])) # set row for 1st column
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(l[1])) # set row for 2nd column
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(l[2])) # set row for 3rd column
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(l[3])) # set row for 4th column
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(l[4])) # set row for 5th column
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(l[5])) # set row for 6th column
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(l[6])) # set row for 7th column
                row = row + 1
                
    def load_reserve_data(self): # Load reserve data to table
        your_book_list = [] # Create new list name your_book_list
        #print(self.uid.Id)
        
        with open('DataCSV/reservation_data.csv', newline='') as f: # open reservation_data.csv
                reader = csv.reader(f) # Read csv as reader
                data = list(reader) # turn reader  
                your_book_list = data

        row = 0 # initial row value
        self.tableWidget_2.setRowCount(len(your_book_list)) # Create tableWidget_2 by length new_list
        for l in your_book_list:
            A_list = self.Convert(l[8][1:-1]) # get additional services from reservation_data.csv
            strt = "" # initial string variable
            for i, r in enumerate(A_list): # loop in A_list
                    if r == 'True' and i == 0: 
                            strt = strt + "Meal " # add Meal string
                    elif r =='True' and i == 1:
                            strt = strt + "Pick and Drop " # add Pick and Drop string
                    elif r =='True' and i == 2:
                            strt = strt + "Car " # add Car string
                    elif r =='True' and i == 3:
                            strt = strt + "Grooming " # add Grooming string
                    elif r =='True' and i == 4:
                            strt = strt + "Wellbeing " # add Wellbeing string
                            
                
            self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(l[0])) # set row for 1st column
            self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(l[2])) # set row for 2nd column
            self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(l[1])) # set row for 3rd column
            self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(l[3])) # set row for 4th column
            self.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(l[4])) # set row for 5th column
            self.tableWidget_2.setItem(row, 5, QtWidgets.QTableWidgetItem(l[6])) # set row for 6th column
            self.tableWidget_2.setItem(row, 6, QtWidgets.QTableWidgetItem(l[7])) # set row for 7th column
            self.tableWidget_2.setItem(row, 7, QtWidgets.QTableWidgetItem(strt)) # set row for 8th column
            self.tableWidget_2.setItem(row, 8, QtWidgets.QTableWidgetItem(l[9])) # set row for 9th column
            
            row = row + 1
    
    def sort_reserve_data(self): # Sort reserve data by latest
        if self.reserve_state_sort == 0: # set reverse_state = 0
            
            self.reserve_state_sort = 1 # set reverse_state = 1
            your_book_list = [] # Create blank list
            reverse_index = -1 # reverse index as latest
            
            with open('DataCSV/reservation_data.csv', newline='') as f: # open reservation_data.csv
                    reader = csv.reader(f) # read csv as reader
                    data = list(reader) # turn reader to list
                    for i in data: # loop in data
                        your_book_list.append(data[reverse_index]) # append your_book_list from latest index
                        reverse_index = reverse_index - 1 # increase index
                    
            
            row = 0 # initial row value
            self.tableWidget_2.setRowCount(len(your_book_list)) # Create tableWidget_2 by length new_list
            
            for l in your_book_list:
                A_list = self.Convert(l[8][1:-1]) # get additional services from reservation_data.csv
                strt = "" # initial string variable
                for i, r in enumerate(A_list): # loop in A_list
                        if r == 'True' and i == 0:
                                strt = strt + "Meal " # add Meal string
                        elif r =='True' and i == 1:
                                strt = strt + "Pick and Drop " # add Pick and Drop string
                        elif r =='True' and i == 2:
                                strt = strt + "Car " # add Car string
                        elif r =='True' and i == 3:
                                strt = strt + "Grooming " # add Grooming string
                        elif r =='True' and i == 4:
                                strt = strt + "Wellbeing " # add Wellbeing string
                                
                self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(l[0])) # set row for 1st column
                self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(l[2])) # set row for 2nd column
                self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(l[1])) # set row for 3rd column 
                self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(l[3])) # set row for 4th column
                self.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(l[4])) # set row for 5th column
                self.tableWidget_2.setItem(row, 5, QtWidgets.QTableWidgetItem(l[6])) # set row for 6th column
                self.tableWidget_2.setItem(row, 6, QtWidgets.QTableWidgetItem(l[7])) # set row for 7th column
                self.tableWidget_2.setItem(row, 7, QtWidgets.QTableWidgetItem(strt)) # set row for 8th column
                self.tableWidget_2.setItem(row, 8, QtWidgets.QTableWidgetItem(l[9])) # set row for 9th column
                
                row = row + 1
        else:
            self.reserve_state_sort = 0 # set user_state = 0
            self.load_reserve_data() # Load_user_data for update table
            
    def delete_reserve_Id(self): # Delete reserve data by Id
        data_list = [] # Create blank list data_list
        replace_list = [] # Create blank list replace_list
                
        with open('DataCSV/reservation_data.csv', newline='') as f: # open reservation_data.csv
                reader = csv.reader(f) # read csv as reader
                data = list(reader) # turn reader into list
                for r in data: # loop in data
                    data_list.append(r) # append r to data_list
                    
        reserve_d_text = self.lineEdit_2.text() # get ID for delete
        
        for i in data_list: # loop in data
            if i[0] != reserve_d_text: # if ID != target ID
                replace_list.append(i) # Append i in replace_list
        
        with open('DataCSV/reservation_data.csv', 'w', newline='') as f: # open reservation_data.csv
                                fw = csv.writer(f)
                                fw.writerows(replace_list) # write replace_list
        
        self.load_reserve_data() # Load_user_data for update table
        self.lineEdit_2.setText("") # set blank text
            
    def Convert(self, string):
                li = list(string.split(", ")) # split string by comma
                return li

    def Login(self): # Open Login page
        from LogInMain import LoginWindow # import LoginWindow class from LogInMain
        self.window = QtWidgets.QMainWindow() # Create QMainWindow as window
        self.ui = LoginWindow(self.window) # Create Object from LoginWindow 
        self.window.show() # Show Login Window
        self.AdminMain.close() # hide Admin Window

