from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User

#Tests for several PBIs
#PBI ID: 2494994, 2495035
class Testcode(TestCase):
    App = TASchedulingApp()

    def test_ContactInfo_invalid_info(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("bob", "bob", 3)
        self.App.createContact(8, "2624736485", "sheep@jeep.com")
        self.assertFalse(self.App.editAccount(7, 8, "2527364823", "boop.com"))

    def test_create_Contact_no_User(self):
        self.App.LoggedInUser = None;
        self.assertFalse(self.App.createContact(8, "2624736485", "sheep@jeep.com"))

    def test_edit_Contact_no_User(self):
        self.App.LoggedInUser = None;
        self.assertFalse(self.App.editContact("bob","tim", "2624736485", "sheep@jeep.com"))

    def test_create_Contact_valid(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("bob", "bob", 3)
        self.assertTrue(self.App.createContact("bob", "2624736485", "sheep@jeep.com"))

    def test_create_Contact_already_exists(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("bob", "bob", 3)
        self.App.createContact("bob", "2624736485", "sheep@jeep.com")
        self.assertFalse(self.App.createContact("bob", "2624736485", "sheep@jeep.com"))

    def test_edit_Contact_valid(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("bob", "bob", 3)
        self.App.createContact("bob", "2624736485", "sheep@jeep.com")
        self.assertTrue(self.App.editContact("bob", "tim", "2624736485", "sheep@jeep.com"))

    def test_edit_Contact_already_edited(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.App.createAccount("bob", "bob", 3)
        self.App.createContact("bob", "2624736485", "sheep@jeep.com")
        self.App.editContact("bob", "tim", "2624736485", "sheep@jeep.com")
        self.assertFalse(self.App.editContact("bob", "tim", "2624736485", "sheep@jeep.com"))

    def test_display_Contacts_sucessful(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        x = self.App.displayContacts() != "Could Not Display Contacts"
        self.assertTrue(x)

    def test_display_Contacts_no_user(self):
        self.App.LoggedInUser = None
        self.assertEquals("Could Not Display Contacts", self.App.displayContacts())

    def test_display_public_accounts_sucessful(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        x = self.App.displayPublicAccounts() != "Could Not Display Accounts"
        self.assertTrue(x)

    def test_display_public_accounts_no_user(self):
        self.App.LoggedInUser = None
        self.assertEquals("Could Not Display Accounts", self.App.displayPublicAccounts())

    def test_create_Contact_Account_does_not_exist(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertFalse(self.App.createContact("bob", "2624736485", "sheep@jeep.com"))

    def test_edit_Contact_does_not_exist(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        self.assertFalse(self.App.editContact("bob", "tim", "2624736485", "sheep@jeep.com"))
