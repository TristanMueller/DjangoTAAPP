from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User


class Testcode(TestCase):
    App = TASchedulingApp()

    def test_edit_user_success(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("billy", "billy", 2)
        self.assertTrue(self.App.editAccount("billy", "pauly", "billy", "2"))  # should be user that doesn't exist

    def test_edit_pass_success(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("paul", "paul", 4)
        self.assertTrue(self.App.editAccount("paul", "paul", "Lol", "4"))  # should be valid password

    def test_edit_clearance_success(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("brandon", "brandon", 3)
        self.assertTrue(self.App.editAccount("brandon", "isaiah", "isaiah", "2"))  # should be valid clearance

    def test_edit_user_fail(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("TA1", "TA1", 4)
        self.assertFalse(self.App.editAccount("Admin", "TA1", "Admin", "1"))  # should be user that does exist

    def test_edit_pass_fail(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertFalse(self.App.editAccount("Admin", "Admin", "", "1"))  # should be invalid password

    def test_edit_clearance_fail(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertFalse(self.App.editAccount("Admin", "Admin", "Lol", "37"))  # should be invalid clearance

    def test_edit_no_user(self):
        self.App.LoggedInUser = None
        self.assertFalse(self.App.editAccount("Admin", "Admin", "Lol", "37"))
    def test_edit_invalid_user(self):
        self.App.LoggedInUser = User("TA", "TA", 4)
        self.assertFalse(self.App.editAccount("Admin", "Admin", "Lol", "37"))

    def test_edit_other_pass_fail(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertFalse(self.App.editAccount("Bill", "Bill", "", "1"))  # should be invalid password

    def test_edit_other_clearance_fail(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertFalse(self.App.editAccount("Bill", "Bill", "Bill", "8"))  # should be invalid clearance

    def test_edit_delete_account(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertTrue(self.App.editAccount("Bill", "", "", ""))  # should this work?