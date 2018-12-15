from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User


class Testcode(TestCase):
    App = TASchedulingApp()

    def test_edit_course_successful(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("rock", "rock", 3)
        self.App.createCourse("234", "Example", "rock")
        self.App.createAccount("Sorenson", "password", 3)
        self.assertTrue(self.App.editCourse("234", "235", "Example2", "Sorenson"))

    def test_edit_course_invalid_login(self):
        self.App.LoggedInUser is None
        self.assertFalse(self.App.editCourse("234", "235", "Example", "rock"))

    def test_edit_course_invalid_clearance(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createCourse("234", "Example", "rock")
        self.App.logout()
        self.App.LoggedInUser = User("TA", "TA", 4)
        self.assertFalse(self.App.editCourse("234", "235", "Example", "rock"))
        self.App.logout()

    def test_edit_course_invalid_professor(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createCourse("234", "Example", "rock")
        self.assertFalse(self.App.editCourse("234", "235", "Example2", "john"))
        self.App.logout()

    def test_edit_course_invalid_old_uniqueId(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createCourse("234", "Example", "rock")
        self.assertFalse(self.App.editCourse("236", "235", "Example", "Sorenson"))
        self.App.logout()

    def test_edit_course_new_uniqueId_exists(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createCourse("234", "Example", "rock")
        self.App.createCourse("235", "Example2", "rock")
        self.assertFalse(self.App.editCourse("234", "235", "Example3", "Sorenson"))
        self.App.logout()

    def test_edit_course_new_coursename_exists(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createCourse("234", "Example", "rock")
        self.App.createCourse("235", "Example2", "rock")
        self.assertFalse(self.App.editCourse("234", "236", "Example2", "Sorenson"))

    def test_edit_course_space(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createCourse("234", "Example", "rock")
        self.App.createCourse("235", "Example2", "rock")
        self.assertTrue(self.App.editCourse("234", "234", "CS 265", "Sorenson"))
