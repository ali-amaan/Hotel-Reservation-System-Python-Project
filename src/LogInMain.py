from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMainWindow
import csv 

# for the Login main, on __init__ of LoginWindow class use for create the Qt GUI and the prop method is use for define properties and values

class LoginWindow(QMainWindow):
        Login = 0 # Setup Initial Object
        def __init__(self, LoginWindow, parent=None):
                super().__init__(parent) # to inherit from parent class
                self.Login = LoginWindow # set variable for use QMainWindow
                LoginWindow.setObjectName("LoginWindow")
                LoginWindow.resize(350, 550)
                LoginWindow.setMinimumSize(QtCore.QSize(350, 550)) # set Minimum size
                LoginWindow.setMaximumSize(QtCore.QSize(350, 550)) # set Maximum size
                self.centralwidget = QtWidgets.QWidget(LoginWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(150, 60, 71, 31))
                self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n" # select font family and size style
        "font: 20pt \"MS Shell Dlg 2\";")
                self.label.setObjectName("label") # set label
                self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.textEdit.setGeometry(QtCore.QRect(110, 130, 211, 31)) # set position
                self.textEdit.setObjectName("textEdit")
                self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit.setGeometry(QtCore.QRect(110, 180, 211, 31))
                self.lineEdit.setObjectName("lineEdit")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(130, 260, 101, 41))
                self.pushButton.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
                self.pushButton.setObjectName("pushButton")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(50, 130, 71, 20))
                self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
        "font: 11pt \"MS Shell Dlg 2\";")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(30, 180, 71, 20))
                self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
        "font: 11pt \"MS Shell Dlg 2\";")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(110, 450, 171, 20))
                self.label_4.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
                self.label_4.setObjectName("label_4")
                self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget) # Create Button
                self.pushButton_2.setGeometry(QtCore.QRect(270, 450, 75, 23))
                self.pushButton_2.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
                self.pushButton_2.setObjectName("pushButton_2")
                LoginWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(LoginWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 21))
                self.menubar.setObjectName("menubar")
                LoginWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(LoginWindow)
                self.statusbar.setObjectName("statusbar")
                LoginWindow.setStatusBar(self.statusbar)

                self.prop(LoginWindow)
                QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        def prop(self, LoginWindow): # properties method to set properties of items
                _translate = QtCore.QCoreApplication.translate
                LoginWindow.setWindowTitle(_translate("LoginWindow", "Login")) # set window name of login window
                self.label.setText(_translate("LoginWindow", "Login"))
                self.pushButton.setText(_translate("LoginWindow", "Submit"))
                self.label_2.setText(_translate("LoginWindow", "E-mail :"))
                self.label_3.setText(_translate("LoginWindow", "Password :"))
                self.label_4.setText(_translate("LoginWindow", "Don\'t have ID, register now:"))
                self.pushButton_2.setText(_translate("LoginWindow", "Register"))
                self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
                self.pushButton.clicked.connect(self.checkUser) # check if user had registerd or not
                self.pushButton_2.clicked.connect(self.openRegis) # open register page
        
        def show_message(self, text): # Show message box function
                msg = QMessageBox() # Create QMessageBox() as msg
                msg.setWindowTitle('Message Box') # Set Message title
                msg.setText(text) # Set text from argument
                
                x = msg.exec_()

        def openReserve(self, email): # Open Main Page
                from ReserveMain import ReserveWindow # Import Class ReserveWindow from ReserveMain
                self.window = QtWidgets.QMainWindow() # Create QMainWindow() as window
                self.ui = ReserveWindow(self.window, email) # Create Object from ReserveWindow class and pass email address to check the currently user
                self.window.show() # Show Reserve Window
                self.Login.hide() # Hide Login Window
                
        def openRegis(self): # Open Register Page
                from RegisterMain import RegisWindow # Import RegisWindow class from RegisterMain
                self.window = QtWidgets.QMainWindow() # Create QMainWindow() as window
                self.ui = RegisWindow(self.window) # Create Object from RegisWindow class
                self.window.show() # Show Regis Window
                self.Login.hide() # Hide Login Window
                
        def openAdmin(self): # Open Admin Page
                from AdminMain import AdminWindow # Import AdminWindow class from AdminMain 
                self.window = QtWidgets.QMainWindow() # Create QMainWindow() as window
                self.ui = AdminWindow(self.window) # Create Object from AdminWindow class
                self.window.show() # Show Admin Window
                self.Login.hide() # Hide Login Window

        def checkUser(self): # Check valid input
                username = self.textEdit.text() # get email text
                password = self.lineEdit.text() # get password text

                if username !='' and password !='': # check blank data
                        login_index = 0 # Initial value login_index
                        data = [] # Create data = blank list
                        with open('DataCSV/user_data.csv', newline='') as f: # read user_data.csv
                                reader = csv.reader(f) # Read csv file as reader
                                data = list(reader) # Turn reader to list as data
                                for i, row in enumerate(data): # for loop check username
                                        if username in row[3]: # on user_data.csv file username is the 4th index then use 3
                                                login_index = i # login index = i  
                                                
                        if username == 'admin' and password == '1234': # Set admin Authentication
                                self.openAdmin() # Call openAdmin function
                        elif username == data[login_index][3] and password == data[login_index][-2]: # if the username and password are correct write currently login file
                                self.openReserve(username) # Call openReserve function
                        else:
                                self.show_message('Username or Password is not correct!') # Show message 
                else:
                        self.show_message('Username or Password can not be blank') # Show message
                        

if __name__ == "__main__": # This is main function of this file
        import sys
        app = QtWidgets.QApplication(sys.argv) # Create QApplication as app
        Window = QtWidgets.QMainWindow() # Create QMainWindow as Window
        ui = LoginWindow(Window) # Create Object
        Window.show() # Show LoginWindow
        sys.exit(app.exec_())
        


