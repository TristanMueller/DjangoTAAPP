from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User


class Testcode(TestCase):
    App = TASchedulingApp()

    def test_create_course_successful(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("rock", "rock", 3)
        self.assertTrue(self.App.createCourse("234", "Example", "rock"))

    def test_create_course_unsuccessful_badClearance(self):
        self.App.LoggedInUser = User("TA", "TA", 4)
        self.assertFalse(self.App.createCourse("234", "Example", "rock"))
    def test_create_course_no_logged_in_User(self):
        self.App.LoggedInUser = None
        self.assertFalse(self.App.createCourse("234","Example","rock"))
    def test_create_course_already_exists(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createCourse("234", "Example", "rock")
        self.assertFalse(self.App.createCourse("234", "Example", "rock"))
    def test_create_course_invalid_Professor(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertFalse(self.App.createCourse("234", "Example", "Trevor"))
    def test_create_course_invalid_coursename(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertFalse(self.App.createCourse("234", "!^^*&^%", "rock"))
