from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User


class Testcode(TestCase):
    App = TASchedulingApp()

    def test_create_course_successful(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertTrue(self.App.createCourse("234", "Example", "rock"))

    def test_create_course_unsuccessful_badClearance(self):
        self.App.LoggedInUser = User("TA", "TA", 4)
        self.assertFalse(self.App.createCourse("234", "Example", "rock"))
