from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User


class Testcode(TestCase):
    App = TASchedulingApp()

    def test_AssignProfToCourse_valid(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("Tristan", "Tristan", 3)
        self.App.createCourse("12345", "CS361", "")
        self.assertTrue(self.App.assignProfToCourse("12345", "Tristan"))

    def test_AssignProfToCourse_NotAProfessor(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("Tristan", "Tristan", 4)
        self.App.createCourse("12345", "CS361", "")
        self.assertFalse(self.App.assignProfToCourse("12345", "Tristan"))

    def test_AssignProfToCourse_ProfDoesntExist(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createCourse("12345", "CS361", "")
        self.assertFalse(self.App.assignProfToCourse("12345", "Tristan"))

    def test_AssignProfToCourse_no_logged_in_user(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createCourse("12345", "CS361", "")
        self.App.createAccount("Tristan", "Tristan", 3)
        self.App.logout()
        self.assertFalse(self.App.assignProfToCourse("12345", "Tristan"))

    def test_AssignProfToCourse_Course_Does_not_exist(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("Tristan", "Tristan", 3)
        self.assertFalse(self.App.assignTAToLab("12345", "Tristan"))


