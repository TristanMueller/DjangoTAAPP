from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User

#PBI ID: 2495012
# As the Supervisor or Admin, I should be able to access all data in the system so that I may make changes anywhere when it is necessary.
class Testcode(TestCase):
    App = TASchedulingApp()

    def test_display_contacts_sucessful(self):
        self.App.LoggedInUser = User("Admin", "Admin", 1)
        x = self.App.displayContacts() != "Could Not Display Contacts"
        self.assertTrue(x)

    def test_display_contacts_no_user(self):
        self.App.LoggedInUser = None
        x = self.App.displayContacts() == "Could Not Display Contacts"
        self.assertTrue(x)
