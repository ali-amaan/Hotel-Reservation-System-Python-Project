import unittest
from Classes.reserve_class import Reserve_Class
from Classes.user_class import User_Class

reserveclassobject1 = Reserve_Class(10, 100, (2023, 1, 26), (2023, 1, 27), 1, 1, 0, [1, 0, 0, 0, 0])
reserveclassobject1.cal_price()
expectedOutput1 = 40 + 7

reserveclassobject2 = Reserve_Class(10, 100, (2022, 5, 30), (2022, 6, 10), 11, 1, 0, [1, 1, 1, 1, 1])
reserveclassobject2.cal_price()
expectedOutput2 = (40 * 11) + (7 * 11) + 12 + (20 * 11) + 9 + 5

userclassobject3 = User_Class()
userclassobject3.readById("4")
expectedOutput3 = "John"

userclassobject4 = User_Class()
userclassobject4.readById("3")
expectedOutput4 = "John"

class tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reserveclassobject1.get_total_price(), expectedOutput1, "Incorrect Price Calculation.")

    def test_2(self):
        self.assertEqual(reserveclassobject2.get_total_price(), expectedOutput2, "Incorrect Price Calculation.")

    def test_3(self):
        self.assertEqual(userclassobject3.get_name(), expectedOutput3, "Incorrect User Searched.")

    def test_4(self):
        self.assertNotEqual(userclassobject4.get_name(), expectedOutput4, "Incorrect User Searched.")
