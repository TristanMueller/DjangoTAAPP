from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User

class Testcode(TestCase):

  
  App = TASchedulingApp()
  def test_create_lab_invalid_login(self):
    
    self.App.LoggedInUser is None
    self.assertEqual("Invalid command", self.App.createLab("John", "361", "1"))
  
  def test_create_lab_invalid_clearance(self):
    
    self.App.LoggedInUser = User("TA", "TA", )
    self.assertEqual("Invalid command", self.App.createLab("John", "361", "1"))
  
  def test_create_lab_succesful(self):
    
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertEqual("Lab Created", self.App.createLab("John", "361", "1"))

  def test_create_lab_no_class(self):
    
    self.App.LoggedInUser = User("Admin","Admin",1)
    self.assertEqual("Course does not exist", self.App.createLab("John", "431", "1"))

  def test_create_lab_succesful(self):
    
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertEqual("TA does not exist", self.App.createLab("Jim", "361", "1"))
  

  def test_create_account_successful(self):
  
    self.App.LoggedInUser = User("Admin","Admin",1)
    self.assertTrue(self.App.createAccount("Example","Example",3))

  def test_create_account_existing(self):
    
    self.App.LoggedInUser = User("Admin","Admin",1)
    self.App.createAccount("Existing","Existing",1)
    self.assertFalse(self.App.createAccount("Existing","Existing",1))

  def test_create_account_bad_input(self):
    
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertFalse(self.App.createAccount("co,mma","normal",1))
    self.assertFalse(self.App.createAccount("normal","co,mma",1))
    self.assertFalse(self.App.createAccount("normal","normal","bad"))

  def test_create_account_bad_clearance(self):
    self.App.LoggedInUser = User("TA", "TA", 4)
    self.assertFalse(self.App.createAccount("comma", "normal", 1))



  def test_login_successful(self):
    self.App.LoggedInUser = None
    self.assertTrue(self.App.login("Admin","Admin"))

  def test_login_unsuccessful(self):
    self.App.LoggedInUser = None
    self.assertFalse(self.App.login("DoesNotExist", "Admin"))

  def test_login_bad_input(self):
    self.App.LoggedInUser = None
    self.assertFalse(self.App.login(1,None))

  def test_create_course_successful(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertTrue(self.App.createCourse("234", "Example", "rock"))

  def test_create_course_unsuccessful_badClearance(self):
    self.App.LoggedInUser = User("TA", "TA", 4)
    self.assertFalse(self.App.createCourse("234", "Example", "rock"))

  def test_delete_account_invalid(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertFalse(self.App.deleteAccount("jack"))
  def test_delete_account_valid(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    file_object = open("Accounts.txt", "a")
    file_object.write("bob,bob,2")
    file_object.close()
    self.assertTrue(self.App.deleteAccount("bob"))
  def test_delete_account_invalid_clearance(self):
    self.App.LoggedInUser = User("TA", "TA", 4)
    self.assertEquals(self.App.deleteAccount("jack"), "Could Not Delete Account")

    #Brandon's
  def test_edit_user_success(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertEqual(self.App.editAccount("Admin", "Lol", "Admin", "1"), "Edited Account") #should be user that doesn't exist
  def test_edit_pass_success(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertEqual(self.App.editAccount("Admin", "Admin", "Lol", "1"), "Edited Account") #should be valid password
  def test_edit_clearance_success(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertEqual(self.App.editAccount("Admin", "Admin", "Lol", "1"), "Edited Account") #should be valid clearance
  def test_edit_user_fail(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertEqual(self.App.editAccount("Admin", "TA1", "Admin", "1"), "Invalid command or insufficient access") #should be user that does exist
  def test_edit_pass_fail(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertEqual(self.App.editAccount("Admin", "Admin", "", "1"), "Invalid command or insufficient access") #should be invalid password
  def test_edit_clearance_fail(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertEqual(self.App.editAccount("Admin", "Admin", "Lol", "37"), "Invalid command or insufficient access") #should be invalid clearance

  #tests definitely need some work. I'm having trouble with unit tests.

  def test_edit_course_successful(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createCourse("234", "Example", "rock")
    self.assertTrue(self.App.editCourse("234", "Example2", "sorenson"))

  def test_edit_course_unsuccessful(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createCourse("234", "Example", "rock")
    self.App.logout()
    self.App.LoggedInUser = User("TA", "TA", 4)
    self.assertFalse(self.App.editCourse("234", "Example", "rock"))
    self.App.logout()
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertFalse(self.App.editCourse("235", "Example", "rock"))
  
#suite = TestCase.TestSuite()
#suite.addTest(TestCase.makeSuite(Testcode))
#runner = TestCase.TextTestRunner()
#res=runner.run(suite)
#print(res)
#print("*"*20)
#for i in res.failures:
   # print(i[1])
