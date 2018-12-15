from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User


class Testcode(TestCase):
    App = TASchedulingApp()

    def test_display_courses_sucessful(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        x = self.App.displayCourses() != "Could Not Display Courses"
        self.assertTrue(x)

    def test_display_courses_invalid_user(self):
        self.App.LoggedInUser = User("TA", "TA", 4)
        x = self.App.displayCourses() == "Could Not Display Courses"
        self.assertTrue(x)

    def test_display_courses_no_user(self):
        x = self.App.displayCourses() == "Could Not Display Courses"
        self.assertTrue(x)