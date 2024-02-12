import pytest # import pytest into project
from PyQt5 import QtCore, QtWidgets # import Qt5 and QtWidget
import sys # import System lib
sys.path.append('../') # Define path to the program
from ReserveMain import ReserveWindow # import Reserve window class to test admin page

@pytest.fixture # pytest-command
def app(qtbot): # define function and set argument name qtbot
    test_hello_app = ReserveWindow(QtWidgets.QMainWindow(), 'alex@gmail.com') # create object from LoginWindow class and pass QMainWindow in
    qtbot.addWidget(test_hello_app) # add widget

    return test_hello_app # return it-self

def test_label(app):
    assert app.label_2.text() == '<html><head/><body><p><span style=\" font-size:12pt;\">Cancel Reservation : Type Room Number</span></p></body></html>'
    # assert is app.label in register_main text equal to '<html><head/><body><p><span style=\" font-size:12pt;\">Cancel Reservation : Type Room Number</span></p></body></html>' or not
    # html tag is use for define the style for that widget
