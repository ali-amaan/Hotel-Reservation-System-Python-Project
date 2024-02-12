import pytest # import pytest into project
from PyQt5 import QtCore, QtWidgets # import Qt5 and QtWidget
import sys # import System lib
sys.path.append('../') # Define path to the program
from RegisterMain import RegisWindow # import Regis window class to test admin page

@pytest.fixture # pytest-command
def app(qtbot): # define function and set argument name qtbot
    test_hello_app = RegisWindow(QtWidgets.QMainWindow()) # create object from LoginWindow class and pass QMainWindow in
    qtbot.addWidget(test_hello_app) # add widget

    return test_hello_app # return it-self

def test_label(app):
    assert app.label_3.text() == 'Surname :' # assert is app.label in register_main text equal to 'Surname :' or not