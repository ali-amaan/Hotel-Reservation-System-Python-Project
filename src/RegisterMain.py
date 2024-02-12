from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import csv
from PyQt5.QtWidgets import QMessageBox
from Classes.user_class import User_Class

class RegisWindow(QMainWindow):
        Regis_main = 0 # Setup initial Object
        
        def __init__(self, RegisWindow, parent=None):
                super().__init__(parent) # to inherit from parent class
                self.Regis_main = RegisWindow   
                RegisWindow.setObjectName("RegisWindow") 
                RegisWindow.resize(350, 550) # set size same as login page
                RegisWindow.setMinimumSize(QtCore.QSize(350, 550)) 
                RegisWindow.setMaximumSize(QtCore.QSize(350, 550))
                self.centralwidget = QtWidgets.QWidget(RegisWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget) # create label
                self.label.setGeometry(QtCore.QRect(130, 60, 101, 31))
                self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
        "font: 20pt \"MS Shell Dlg 2\";")
                self.label.setObjectName("label")
                self.textName = QtWidgets.QTextEdit(self.centralwidget) # Create text edit
                self.textName.setGeometry(QtCore.QRect(110, 130, 211, 31))
                self.textName.setObjectName("textName")
                self.textSurname = QtWidgets.QTextEdit(self.centralwidget)
                self.textSurname.setGeometry(QtCore.QRect(110, 180, 211, 31))
                self.textSurname.setObjectName("textSurname")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(130, 440, 101, 41))
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
                self.textEmail = QtWidgets.QTextEdit(self.centralwidget)
                self.textEmail.setGeometry(QtCore.QRect(110, 230, 211, 31))
                self.textEmail.setObjectName("textEmail")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(50, 230, 71, 20))
                self.label_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
        "font: 11pt \"MS Shell Dlg 2\";")
                self.label_4.setObjectName("label_4")
                self.textTel = QtWidgets.QTextEdit(self.centralwidget)
                self.textTel.setGeometry(QtCore.QRect(110, 280, 211, 31))
                self.textTel.setObjectName("textTel")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(70, 280, 31, 20))
                self.label_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
        "font: 11pt \"MS Shell Dlg 2\";")
                self.label_5.setObjectName("label_5")
                self.lineEdit_Pass = QtWidgets.QLineEdit(self.centralwidget) # Use lineEdit for password
                self.lineEdit_Pass.setGeometry(QtCore.QRect(110, 330, 211, 31))
                self.lineEdit_Pass.setObjectName("lineEdit_Pass")
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(30, 330, 71, 20))
                self.label_6.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
        "font: 11pt \"MS Shell Dlg 2\";")
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(10, 380, 111, 20))
                self.label_7.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
        "font: 11pt \"MS Shell Dlg 2\";")
                self.label_7.setObjectName("label_7")
                self.lineEdit_RePass = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_RePass.setGeometry(QtCore.QRect(110, 380, 211, 31))
                self.lineEdit_RePass.setObjectName("textEdit_RePass")
                RegisWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(RegisWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 21))
                self.menubar.setObjectName("menubar")
                RegisWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(RegisWindow)
                self.statusbar.setObjectName("statusbar")
                RegisWindow.setStatusBar(self.statusbar)

                self.prop(RegisWindow)
                QtCore.QMetaObject.connectSlotsByName(RegisWindow)

        def prop(self, RegisWindow):
                _translate = QtCore.QCoreApplication.translate
                RegisWindow.setWindowTitle(_translate("RegisWindow", "Register"))
                self.label.setText(_translate("RegisWindow", "Register"))
                self.pushButton.setText(_translate("RegisWindow", "Sign Up"))
                self.label_2.setText(_translate("RegisWindow", "Name :"))
                self.label_3.setText(_translate("RegisWindow", "Surname :"))
                self.label_4.setText(_translate("RegisWindow", "E-mail :"))
                self.label_5.setText(_translate("RegisWindow", "Tel :"))
                self.label_6.setText(_translate("RegisWindow", "Password :"))
                self.label_7.setText(_translate("RegisWindow", "Re-Password :"))
                self.lineEdit_Pass.setEchoMode(QtWidgets.QLineEdit.Password) # This line make password look ********
                self.lineEdit_RePass.setEchoMode(QtWidgets.QLineEdit.Password)

                self.pushButton.clicked.connect(self.Register_data) # Call Register Function
                
        def show_message(self, text): # Show Message Box
                        msg = QMessageBox() # Create QMessage Box as msg
                        msg.setWindowTitle('Message Box') # Set Window title
                        msg.setText(text) # Set text from argument
                        # msg.setIcon(QMessageBox.Information)
                        
                        x = msg.exec_()
                
        def openLogin(self): # Open Login Page when finished register
                from LogInMain import LoginWindow # import LoginWindow class from LogInMain
                self.window = QtWidgets.QMainWindow() # Create QMainWindow as window
                self.ui = LoginWindow(self.window) # Create Object from LoginWindow
                self.window.show() # Show Window
                self.Regis_main.close() # Hide Regis Window
                
        def Register_data(self): # Set Registering Data
                name = self.textName.toPlainText() # Get name
                surname = self.textSurname.toPlainText() # Get surname
                email = self.textEmail.toPlainText() # Get email
                tel = self.textTel.toPlainText() # Get Number
                password = self.lineEdit_Pass.text() # Get Password
                re_password = self.lineEdit_RePass.text() # Get Confrom-Password
                ID = 'id' # initial ID
                loyalty_point = 0 # new user's loyalty point = 0
                email_list = [] # Create List name email_list
                
                with open('DataCSV/user_data.csv', newline='') as f: # open user_data.csv to read lastest user
                                reader = csv.reader(f) # Read csv file as a reader
                                data = list(reader) # Turn reader to data list
                                for user in data: # loop in data
                                        email_list.append(user[3]) # append email in email_list
                                # print(data)
                                ID = int(data[-1][0])+1 # define ID from latest ID in csv file
                                
                
                if name == '' or surname == '' or email == '' or tel == '' or password == '' or re_password == '': # Check blank input
                        self.show_message('Registeration data can not be blank') # Show_Message

                elif '@' not in email: # Check '@' in email
                        self.show_message('E-mail must contain "@"') # Show_Message

                elif email in email_list: # Check duplicate email
                        self.show_message('This email already used!') # Show_Message
                        
                elif password == re_password: # Check password and re-password
                        uid = User_Class( # Create Object uid from User_Class
                                str(ID), # set ID
                                name, # set name 
                                surname, # set surname 
                                email , # set email
                                tel, # set number
                                password, # set pass
                                str(loyalty_point) # set loyalty_point
                        )
                        uid.appendUser() # call method appendUser()
                        self.openLogin() # openLogin Window
                        
                elif password != re_password:
                        self.show_message('Password and Re-Password must be the same!') # Show_Message

