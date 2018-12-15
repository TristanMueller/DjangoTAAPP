from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User


class Testcode(TestCase):
    App = TASchedulingApp()

    def test_display_ta_assignments_sucessful(self):
        self.App.LoggedInUser = User("TA", "TA", 4)
        x = self.App.displayTAAssignments() != "Could Not Display TA Assignments"
        self.assertTrue(x)

    def test_display_ta_assignments_invalid_user(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        x = self.App.displayTAAssignments() == "Could Not Display TA Assignments"
        self.assertTrue(x)

    def test_display_ta_assignments_no_user(self):
        x = self.App.displayTAAssignments() == "Could Not Display TA Assignments"
        self.assertTrue(x)