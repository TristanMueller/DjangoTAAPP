from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User

#PBI ID: 2495026
#As a TA, I want to view assignments of TA's, so that I know which TA is in teaching which particular course and section.
class Testcode(TestCase):
    App = TASchedulingApp()

    def test_display_labs_for_ta_sucessful(self):
        self.App.LoggedInUser = User("TA", "TA", 4)
        x = self.App.displayLabsForTA() != "Could Not Display Labs"
        self.assertTrue(x)

    def test_display_labs_for_ta_invalid_user(self):
        self.App.LoggedInUser = User("Professor", "Professor", 3)
        x = self.App.displayLabsForTA() == "Could Not Display Labs"
        self.assertTrue(x)

    def test_display_labs_for_ta_no_user(self):
        x = self.App.displayLabsForTA() == "Could Not Display Labs"
        self.assertTrue(x)
