import pytest # import pytest into project
from PyQt5 import QtCore, QtWidgets # import Qt5 and QtWidget
import sys # import System lib
sys.path.append('../') # Define path to the program
from LogInMain import LoginWindow # import login window class to test admin page

@pytest.fixture # pytest-command
def app(qtbot): # define function and set argument name qtbot
    test_hello_app = LoginWindow(QtWidgets.QMainWindow()) # create object from LoginWindow class and pass QMainWindow in
    qtbot.addWidget(test_hello_app) # add widget

    return test_hello_app # return it-self 

def test_label(app): # pass the app into the test_label function 
    assert app.label.text() == "Login" # assert is app.label equal to 'Login'
    
def show_message_test(app): # pass the app into the show_message_test function 
    assert app.show_message('Hello World').msg.text() == 'Hello World' # assert is QMessage.text is equal to 'Hello World' or not