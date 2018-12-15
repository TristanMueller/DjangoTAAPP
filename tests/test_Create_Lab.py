from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User


class Testcode(TestCase):
    App = TASchedulingApp()

    def test_create_lab_invalid_login(self):
        self.App.LoggedInUser is None
        self.assertFalse(self.App.createLab("John", "361", "1"))

    def test_create_lab_invalid_clearance(self):
        self.App.LoggedInUser = User("TA", "TA", 4)
        self.assertFalse(self.App.createLab("John", "361", "1"))

    def test_create_lab_succesful(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("mark", "mark", 3)
        self.App.createCourse("1000", "CS999", "mark")
        self.App.createAccount("Bill", "Bill", 4)
        self.assertTrue(self.App.createLab("1", "1000", "Bill"))

    def test_create_lab_no_class(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertFalse(self.App.createLab("1", "431", "John"))

    def test_create_lab_no_TA(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertFalse(self.App.createLab("1", "361", "Jim"))

    def test_create_lab_already_exists(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("mark", "mark", 3)
        self.App.createCourse("1000", "CS999", "mark")
        self.App.createAccount("Bill", "Bill", 4)
        self.App.createLab("1", "1000", "Bill")
        self.assertFalse(self.App.createLab("1", "1000", "Bill"))

