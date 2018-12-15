from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User

#PBI ID: 2505441
#As a user, I want to be able to log in.
class Testcode(TestCase):
  App = TASchedulingApp()
  def test_login_successful(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createAccount("matt", "matt", 3)
    self.App.logout()
    self.assertTrue(self.App.login("matt", "matt"))

  def test_login_unsuccessful(self):
    self.App.LoggedInUser = None
    self.assertFalse(self.App.login("DoesNotExist", "Admin"))

  def test_login_bad_input(self):
    self.App.LoggedInUser = None
    self.assertFalse(self.App.login(1,None))

#Log out

  def test_logout_succeed(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertTrue(self.App.logout())

  def test_logout_no_user(self):
    self.App.LoggedInUser = None
    self.assertFalse(self.App.logout())
