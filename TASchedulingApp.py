from User import User
from Course import Course
from DjangoTAApp.models import User, Courses, Labs, Contacts

class TASchedulingApp:
    LoggedInUser = None
    def __init__(self):
        self.LoggedInUser = None

    def login(self, sUsername, sPassword):
        if self.LoggedInUser is None:
            users = list(User.objects.filter(username=sUsername))
            for user in users:
                if user.password == sPassword:
                    self.LoggedInUser = User(sUsername, sPassword, user.clearance)
                    self.LoggedInUser.username = sUsername
                    self.LoggedInUser.password = sPassword
                    self.LoggedInUser.clearance = user.clearance
                    return True
            return False
        else:
            return False

    def logout(self):
        self.LoggedInUser = None
        return True

    def createAccount(self,sUsername,sPassword,iClearance):

        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3 and "," not in sUsername and "," not in sPassword and isinstance(iClearance, int):
            users = list(User.objects.filter(username=sUsername))
            if len(users) > 0:
                return False
            else:
                user = User(username=sUsername, password=sPassword, clearance=iClearance)
                user.save()
                return True

    def editAccount(self, sUsername, sNewUsername, sPassword, iClearance):
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3:
            users = list(User.objects.filter(username=sUsername))
            if len(users) == 1:
                User.objects.filter(username=sUsername).delete()
                u1 = User(username=sNewUsername, password=sPassword, clearance=iClearance)
                u1.save()
                return True
            else:
                return False
        else:
            return False

    def createCourse(self, uniqId, coursename, professor):
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 2:
            courses = list(Courses.objects.filter(courseID=uniqId))
            if len(courses) > 0:
                return False
            else:
                course = Courses(courseID=uniqId, coursename=coursename, professor=professor)
                course.save()
                return True
        else:
            return False

    def createLab(self, iLabID, iCourseId, sTA):
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 4:
            labs = list(Labs.objects.filter(LabID=iLabID))
            courses = list(Courses.objects.filter(courseID=iCourseId))
            if len(labs) == 0 and len(courses) > 0:
                lab = Labs(LabID=iLabID, courseID=iCourseId, tausername=sTA)
                lab.save()
                return True
            else:

                return False
        else:
            return False


    def deleteAccount(self, sUsername):
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3:
            if len(list(User.objects.filter(username=sUsername))) > 0:
                User.objects.filter(username=sUsername).delete()
                return True
            else:
                return False
        return "Could Not Delete Account"

    def displayAccounts(self):
        out = ""
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3:
            users = list(User.objects.all())
            for user in users:
                out += "<p>(" + user.username + ", " + user.password + ", " + str(user.clearance) + ")</p>"
            return out
        return "Could Not Display Accounts"

    def displayCourses(self):
        out = ""
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3:
            courses = list(Courses.objects.all())
            for course in courses:
                out += "<p>(" + str(course.courseID) + ", " + course.coursename + ", " + course.professor + ")</p>"
            return out
        return "Could Not Display Courses"

    def displayLabs(self):
        out = ""
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3:
            labs = list(Labs.objects.all())
            for lab in labs:
                out += "<p>(" + str(lab.LabID) + ", " + str(lab.courseID) + ", " + lab.tausername + ")</p>"
            return out
        return "Could Not Display Labs"

    def editCourse(self, uniqId, newUniqId, coursename, professor):
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3:
            coursesId = list(Courses.objects.filter(courseID=uniqId))
            coursesNid = list(Courses.objects.filter(courseID=newUniqId))
            coursesName = list(Courses.objects.filter(coursename=coursename))
            professors = list(User.objects.filter(username=professor))
            if len(coursesId) == 1 and len(coursesNid) == 0 and len(coursesName) == 0 and len(professors) == 1:
                Courses.objects.filter(courseID=uniqId).delete()
                course = Courses(courseID=newUniqId, coursename=coursename, professor=professor)
                course.save()
                return True
            else:
                return False
        else:
            return False

    def displayCoursesForProfessor(self):
        out = ""
        if self.LoggedInUser is not None and self.LoggedInUser.clearance == 3:
            courses = list(Courses.objects.filter(professor=self.LoggedInUser.username))
            for course in courses:
                out += "<p>Course: (" + str(course.courseID) + ", " + course.coursename + ", " + course.professor + ")</p>"
                for lab in list(Labs.objects.filter(courseID=course.courseID)):
                    out += "<p>Lab: (" + str(lab.LabID) + ", " + str(lab.courseID) + ", " + lab.tausername + ")</p>"
            return out
        return "Could Not Display Courses"

    def displayLabsForTA(self):
        out = ""
        if self.LoggedInUser is not None and self.LoggedInUser.clearance == 4:
            labs = list(Labs.objects.filter(tausername=self.LoggedInUser.username))
            for lab in labs:
                out += "<p>(" + str(lab.LabID) + ", " + lab.courseID + ", " + lab.tausername + ")</p>"
            return out
        return "Could Not Display Labs"

    def assignTAToLab(self, labid, tausername):
        if self.LoggedInUser is not None and self.LoggedInUser.clearance == 3:
            labs = list(Labs.objects.filter(LabID=labid))
            ta = list(User.objects.filter(username=tausername))
            if len(labs) == 1 and len(ta) == 1:
                Labs.objects.filter(LabID=labid).delete()
                lab = Labs(labid, labs[0].courseID, tausername)
                lab.save()
                return True
            else:
                return False
        else:
            return False

#brandon's stuff
    def createContact(self, sName, sNumber, sEmail):
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3:
            contacts = list(Contacts.objects.filter(instructor=sName))
            if len(contacts) > 0:
                return False
            else:
                contact = Contacts(instructor=sName, phone=sNumber, email=sEmail)
                contact.save()
                return True

    def editContact(self, sName, sNewName, sNewNumber, sNewEmail):
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3:
            contacts = list(Contacts.objects.filter(instructor=sName))
            if len(contacts) == 1:
                Contacts.objects.filter(instructor=sName).delete()
                c1 = Contacts(instructor=sNewName, phone=sNewNumber, email=sNewEmail)
                c1.save()
                return True
            else:
                return False
        else:
            return False

    def displayContacts(self):
        out = ""
        if self.LoggedInUser is not None:
            contacts = list(Contacts.objects.all())
            for contact in contacts:
                out += "<p>Contacts: ID - " + str(contact.instructor) + ", Phone - " + contact.phone + ", Email - " + contact.email + "</p>"
            return out
        return "Could Not Display Contacts"
    def displayTAAssignments(self):
        out = ""
        if self.LoggedInUser is not None and self.LoggedInUser.clearance == 4:
            TAs = list(Labs.objects.all())
            for TA in TAs:
                out += "<p>TA - " + str(TA.tausername) + ", courseID: - " + str(TA.courseID) + ", LabID: - " + str(TA.LabID) + "</p>"
            return out
        return "Could Not Display TA Assignments"
