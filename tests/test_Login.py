from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User


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