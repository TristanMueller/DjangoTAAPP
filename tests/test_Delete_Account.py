from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User


class Testcode(TestCase):
    App = TASchedulingApp()

    def test_delete_account_invalid(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertFalse(self.App.deleteAccount("jack"))

    def test_delete_account_valid(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("bob", "bob", 2)
        self.assertTrue(self.App.deleteAccount("bob"))

    def test_delete_account_invalid_clearance(self):
        self.App.LoggedInUser = User("TA", "TA", 4)
        self.assertFalse(self.App.deleteAccount("jack"))
    def test_delete_account_no_logged_in_user(self):
        self.App.LoggedInUser = None
        self.assertFalse(self.App.deleteAccount("jack"))
    def test_delete_account_invalid_input(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("bob", "bob", 2)
        self.assertFalse(self.App.deleteAccount("$%^&#%^"))

    def test_delete_account_own(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertTrue(self.App.deleteAccount("Admin")) #this is bad