from django.test import TestCase
from TASchedulingApp import TASchedulingApp
from User import User

class Testcode(TestCase):

  
  App = TASchedulingApp()
  def test_create_lab_invalid_login(self):
    
    self.App.LoggedInUser is None
    self.assertFalse(self.App.createLab("John", "361", "1"))
  
  def test_create_lab_invalid_clearance(self):
    
    self.App.LoggedInUser = User("TA", "TA", 4)
    self.assertFalse(self.App.createLab("John", "361", "1"))
  
  def test_create_lab_succesful(self):
    
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createAccount("mark", "mark", 3)
    self.App.createCourse("1000", "CS999", "mark")
    self.App.createAccount("Bill", "Bill", 4)
    self.assertTrue(self.App.createLab("1", "1000", "Bill"))

  def test_create_lab_no_class(self):
    
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertFalse(self.App.createLab("1", "431", "John"))

  def test_create_lab_no_TA(self):
    
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertFalse(self.App.createLab("1", "361", "Jim"))
  

  def test_create_account_successful(self):
  
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertTrue(self.App.createAccount("Example", "Example", 3))

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
    self.App.createAccount("bob", "bob", 2)
    self.assertTrue(self.App.deleteAccount("bob"))

  def test_delete_account_invalid_clearance(self):
    self.App.LoggedInUser = User("TA", "TA", 4)
    self.assertEquals(self.App.deleteAccount("jack"), "Could Not Delete Account")

    #Brandon's
  def test_edit_user_success(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createAccount("billy", "billy", 2)
    self.assertTrue(self.App.editAccount("billy", "pauly", "billy", "2")) #should be user that doesn't exist

  def test_edit_pass_success(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createAccount("paul", "paul", 4)
    self.assertTrue(self.App.editAccount("paul", "paul", "Lol", "4")) #should be valid password

  def test_edit_clearance_success(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createAccount("brandon", "brandon", 3)
    self.assertTrue(self.App.editAccount("brandon", "isaiah", "isaiah", "2")) #should be valid clearance

  def test_edit_user_fail(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertFalse(self.App.editAccount("Admin", "TA1", "Admin", "1")) #should be user that does exist

  def test_edit_pass_fail(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertFalse(self.App.editAccount("Admin", "Admin", "", "1")) #should be invalid password

  def test_edit_clearance_fail(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertFalse(self.App.editAccount("Admin", "Admin", "Lol", "37")) #should be invalid clearance

  #tests definitely need some work. I'm having trouble with unit tests.


#Isaiah's tests
  def test_edit_course_successful(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createCourse("234", "Example", "rock")
    self.App.createAccount("Sorenson","password",3)
    self.assertTrue(self.App.editCourse("234", "235", "Example2", "Sorenson"))

  def test_edit_course_invalid_login(self):
    self.App.LoggedInUser is None
    self.assertFalse(self.App.editCourse("234", "235", "Example", "rock"))

  def test_edit_course_invalid_clearance(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createCourse("234", "Example", "rock")
    self.App.logout()
    self.App.LoggedInUser = User("TA", "TA", 4)
    self.assertFalse(self.App.editCourse("234", "235", "Example", "rock"))
    self.App.logout()

  def test_edit_course_invalid_professor(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createCourse("234", "Example", "rock")
    self.assertFalse(self.App.editCourse("234", "235", "Example2", "john"))
    self.App.logout()

  def test_edit_course_invalid_old_uniqueId(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createCourse("234", "Example", "rock")
    self.assertFalse(self.App.editCourse("236", "235", "Example", "Sorenson"))
    self.App.logout()

  def test_edit_course_new_uniqueId_exists(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createCourse("234", "Example", "rock")
    self.App.createCourse("235", "Example2", "rock")
    self.assertFalse(self.App.editCourse("234", "235", "Example3", "Sorenson"))
    self.App.logout()

  def test_edit_course_new_coursename_exists(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createCourse("234", "Example", "rock")
    self.App.createCourse("235", "Example2", "rock")
    self.assertFalse(self.App.editCourse("234", "236", "Example2", "Sorenson"))

  def test_create_lab_already_exists(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createAccount("mark", "mark", 3)
    self.App.createCourse("1000", "CS999", "mark")
    self.App.createAccount("Bill", "Bill", 4)
    self.App.createLab("1", "1000", "Bill")
    self.assertFalse(self.App.createLab("1", "1000", "Bill"))

  def test_display_ta_assignments_sucessful(self):
    self.App.LoggedInUser = User("TA","TA",4)
    x= self.App.displayTAAssignments() != "Could Not Display TA Assignments"
    self.assertTrue(x)
  def test_display_ta_assignments_invalid_user(self):
    self.App.LoggedInUser = User("Admin","Admin",1)
    x= self.App.displayTAAssignments() == "Could Not Display TA Assignments"
    self.assertTrue(x)
  def test_display_ta_assignments_no_user(self):
    x= self.App.displayTAAssignments() == "Could Not Display TA Assignments"
    self.assertTrue(x)
  def test_display_accounts_sucessful(self):
    self.App.LoggedInUser = User("Admin","Admin",1)
    x= self.App.displayAccounts() != "Could Not Display Accounts"
    self.assertTrue(x)
  def test_display_accounts_invalid_user(self):
    self.App.LoggedInUser = User("TA","TA",4)
    x = self.App.displayAccounts() == "Could Not Display Accounts"
    self.assertTrue(x)
  def test_display_accounts_no_user(self):
    x = self.App.displayAccounts() == "Could Not Display Accounts"
    self.assertTrue(x)
  def test_display_courses_sucessful(self):
    self.App.LoggedInUser = User("Admin","Admin",1)
    x= self.App.displayCourses() != "Could Not Display Courses"
    self.assertTrue(x)
  def test_display_courses_invalid_user(self):
    self.App.LoggedInUser = User("TA","TA",4)
    x = self.App.displayCourses() == "Could Not Display Courses"
    self.assertTrue(x)
  def test_display_courses_no_user(self):
    x = self.App.displayCourses() == "Could Not Display Courses"
    self.assertTrue(x)

  def test_display_labs_sucessful(self):
    self.App.LoggedInUser = User("Admin","Admin",1)
    x= self.App.displayLabs() != "Could Not Display Labs"
    self.assertTrue(x)
  def test_display_labs_invalid_user(self):
    self.App.LoggedInUser = User("TA","TA",4)
    x = self.App.displayLabs() == "Could Not Display Labs"
    self.assertTrue(x)
  def test_display_labs_no_user(self):
    x = self.App.displayLabs() == "Could Not Display Labs"
    self.assertTrue(x)

  def test_display_courses_for_professor_sucessful(self):
    self.App.LoggedInUser = User("Professor","Professor",3)
    x= self.App.displayCoursesForProfessor() != "Could Not Display Courses"
    self.assertTrue(x)
  def test_display_courses_for_professor_invalid_user(self):
    self.App.LoggedInUser = User("TA","TA",4)
    x = self.App.displayCoursesForProfessor() == "Could Not Display Courses"
    self.assertTrue(x)
  def test_display_courses_for_professor_no_user(self):
    x = self.App.displayCoursesForProfessor() == "Could Not Display Courses"
    self.assertTrue(x)

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

  def test_display_contacts_sucessful(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    x = self.App.displayContacts() != "Could Not Display Contacts"
    self.assertTrue(x)

  def test_display_contacts_no_user(self):
    self.App.LoggedInUser = None
    x = self.App.displayContacts() == "Could Not Display Contacts"
    self.assertTrue(x)
  # Isaiah's tests ends


  def test_AssignTAToLab_valid(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createAccount("Tristan", "Tristan", 3)
    self.App.createCourse("12345", "CS361", "Tristan")
    self.App.createAccount("Assistant", "Assistant", 4)
    self.App.logout()
    self.App.login("Tristan", "Tristan")
    self.App.createLab("001", "12345", "")
    self.assertTrue(self.App.assignTAToLab("001", "Assistant"))

  def test_AssignTAToLab_NotAProfessor(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createAccount("Tristan", "Tristan", 3)
    self.App.createCourse("12345", "CS361", "Tristan")
    self.App.createAccount("Assistant", "Assistant", 4)
    self.App.createLab("001", "12345", "")
    self.assertFalse(self.App.assignTAToLab("001", "Assistant"))

  def test_AssignTAToLab_WrongProfessor(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createAccount("Tristan", "Tristan", 3)
    self.App.createCourse("12345", "CS361", "Tristan")
    self.App.createAccount("Assistant", "Assistant", 4)
    self.App.createAccount("John", "John", 3)
    self.App.logout()
    self.App.login("Tristan", "Tristan")
    self.App.createLab("001", "12345", "")
    self.App.logout()
    self.App.login("John", "John")
    self.assertFalse(self.App.assignTAToLab("001", "Assistant"))

  def test_AssignTAToLab_TADoesntExist(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createAccount("Tristan", "Tristan", 3)
    self.App.createCourse("12345", "CS361", "Tristan")
    self.App.createAccount("John", "John", 3)
    self.App.logout()
    self.App.login("Tristan", "Tristan")
    self.App.createLab("001", "12345", "")
    self.assertFalse(self.App.assignTAToLab("001", "Assistant"))

  #contacts#

  def test_ContactInfo_invalid_info(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createAccount("bob", "bob", 3)
    self.App.createContact(8, "2624736485", "sheep@jeep.com")
    self.assertFalse(self.App.editAccount(7, 8, "2527364823", "boop.com"))

#suite = TestCase.TestSuite()
#suite.addTest(TestCase.makeSuite(Testcode))
#runner = TestCase.TextTestRunner()
#res=runner.run(suite)
#print(res)
#print("*"*20)
#for i in res.failures:
   # print(i[1])
