from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User


class Testcode(TestCase):
    App = TASchedulingApp()

    def test_ContactInfo_invalid_info(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("bob", "bob", 3)
        self.App.createContact(8, "2624736485", "sheep@jeep.com")
        self.assertFalse(self.App.editAccount(7, 8, "2527364823", "boop.com"))