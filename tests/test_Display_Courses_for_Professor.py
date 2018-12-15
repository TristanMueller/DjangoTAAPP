from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User

#PBI ID: 2495001
#As an instructor, I need to be able to view course assignments so that I can determine which TAs need to go where.
class Testcode(TestCase):
    App = TASchedulingApp()

    def test_display_courses_for_professor_sucessful(self):
        self.App.LoggedInUser = User("Professor", "Professor", 3)
        x = self.App.displayCoursesForProfessor() != "Could Not Display Courses"
        self.assertTrue(x)

    def test_display_courses_for_professor_invalid_user(self):
        self.App.LoggedInUser = User("TA", "TA", 4)
        x = self.App.displayCoursesForProfessor() == "Could Not Display Courses"
        self.assertTrue(x)

    def test_display_courses_for_professor_no_user(self):
        x = self.App.displayCoursesForProfessor() == "Could Not Display Courses"
        self.assertTrue(x)
