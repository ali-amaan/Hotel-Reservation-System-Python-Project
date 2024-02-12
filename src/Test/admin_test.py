import pytest # import pytest into project
from PyQt5 import QtCore, QtWidgets # import Qt5 and QtWidget
import sys # import System lib
sys.path.append('../') # Define path to the program
from AdminMain import AdminWindow # import admin window class to test admin page

@pytest.fixture # pytest-command
def app(qtbot): # define function and set argument name qtbot
    test_hello_app = AdminWindow(QtWidgets.QMainWindow()) # create object from AdminWindow class and pass QMainWindow in
    qtbot.addWidget(test_hello_app) # add widget

    return test_hello_app # return it-self 

def test_label(app):
    assert app.LogOut.text() == 'Log out' # assert the LogOut label is that equal 'Log out'