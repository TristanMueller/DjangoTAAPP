from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User


class Testcode(TestCase):
    App = TASchedulingApp()

    def test_AssignTAToLab_valid(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("Tristan", "Tristan", 3)
        self.App.createCourse("12345", "CS361", "Tristan")
        self.App.createAccount("Assistant", "Assistant", 4)
        self.App.createLab("001", "12345", "")
        self.App.logout()
        self.App.login("Tristan", "Tristan")
        self.assertTrue(self.App.assignTAToLab("001", "Assistant"))

    def test_AssignTAToLab_NotAProfessor(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("Tristan", "Tristan", 3)
        self.App.createCourse("12345", "CS361", "Tristan")
        self.App.createAccount("Assistant", "Assistant", 4)
        self.App.createLab("001", "12345", "")
        self.assertFalse(self.App.assignTAToLab("001", "Assistant"))

    def test_AssignTAToLab_WrongProfessor(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("Tristan", "Tristan", 3)
        self.App.createCourse("12345", "CS361", "Tristan")
        self.App.createAccount("Assistant", "Assistant", 4)
        self.App.createAccount("John", "John", 3)
        self.App.logout()
        self.App.login("Tristan", "Tristan")
        self.App.createLab("001", "12345", "")
        self.App.logout()
        self.App.login("John", "John")
        self.assertFalse(self.App.assignTAToLab("001", "Assistant"))

    def test_AssignTAToLab_TADoesntExist(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("Tristan", "Tristan", 3)
        self.App.createCourse("12345", "CS361", "Tristan")
        self.App.createAccount("John", "John", 3)
        self.App.logout()
        self.App.login("Tristan", "Tristan")
        self.App.createLab("001", "12345", "")
        self.assertFalse(self.App.assignTAToLab("001", "Assistant"))
    def test_AssignTAToLab_no_logged_in_user(self):
        self.App.LoggedInUser = None
        self.assertFalse(self.App.assignTAToLab("001", "Assistant"))
    def test_AssignTAToLab_Lab_Does_not_exist(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("Tristan", "Tristan", 3)
        self.App.createCourse("12345", "CS361", "Tristan")
        self.App.createAccount("Assistant", "Assistant", 4)
        self.App.logout()
        self.App.login("Tristan", "Tristan")
        self.assertTrue(self.App.assignTAToLab("001", "Assistant"))
    def test_AssignTAToLab_TA_already_assigned(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("Tristan", "Tristan", 3)
        self.App.createCourse("12345", "CS361", "Tristan")
        self.App.createAccount("Assistant", "Assistant", 4)
        self.App.createLab("001", "12345", "Assistant")
        self.App.logout()
        self.App.login("Tristan", "Tristan")
        self.assertTrue(self.App.assignTAToLab("001", "Assistant"))

