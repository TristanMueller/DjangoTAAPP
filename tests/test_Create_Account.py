from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User


class Testcode(TestCase):
    App = TASchedulingApp()

    def test_create_account_successful(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertTrue(self.App.createAccount("Example", "Example", 3))

    def test_create_account_existing(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("Existing", "Existing", 1)
        self.assertFalse(self.App.createAccount("Existing", "Existing", 1))

    def test_create_account_bad_username(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertFalse(self.App.createAccount("co,mma", "normal", 1))

    def test_create_account_bad_password(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertFalse(self.App.createAccount("normal", "co,mma", 1))

    def test_create_account_bad_clearance(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertFalse(self.App.createAccount("normal", "normal", "bad"))

    def test_create_account_bad_clearance(self):
        self.App.LoggedInUser = User("TA", "TA", 4)
        self.assertFalse(self.App.createAccount("comma", "normal", 1))
    def test_create_account_no_logged_in_user(self):
        self.App.LoggedInUser = None
        self.assertFalse(self.App.createAccount("Example", "Example", 3))