from User import User, Clearance
from Course import Course
from DjangoTAApp.models import User, Courses, Labs, Contacts


class TASchedulingApp:
    def __init__(self):
        self.loggedInUser = None

    def login(self, username, password):
        if self.loggedInUser is None:
            self.loggedInUser = User.objects.filter(username=username, password=password).first()
            return self.loggedInUser is not None
        return False

    def logout(self):
        self.loggedInUser = None
        return True

    @staticmethod
    def verify_clearance(clearance):
        return 0 < clearance <= 4

    def createAccount(self, username, password, clearance):
        if not TASchedulingApp.verify_clearance(int(clearance)):
            return False
        if self.loggedInUser is not None and self.loggedInUser.clearance <= Clearance.ADMINISTRATOR:
            if len(list(User.objects.filter(username=username))) > 0:
                return False
            else:
                User(username=username, password=password, clearance=clearance).save()
                return True
        return False

    def editAccount(self, username, newUsername, password, clearance):
        if not TASchedulingApp.verify_clearance(int(clearance)):
            return False
        if self.loggedInUser is not None and self.loggedInUser.clearance <= Clearance.ADMINISTRATOR:
            if len(list(User.objects.filter(username=username))) > 0:
                User.objects.filter(username=username).delete()
                User(username=newUsername, password=password, clearance=clearance).save()
                return True
        return False

    def createCourse(self, uniqId, coursename, professor):
        if self.loggedInUser is not None and self.loggedInUser.clearance < 3:
            if len(list(Courses.objects.filter(courseID=uniqId))) > 0:
                return False
            else:
                Courses(courseID=uniqId, coursename=coursename, professor=professor).save()
                return True
        return False

    def deleteCourse(self, courseID):
        if self.loggedInUser is not None and self.loggedInUser.clearance <= Clearance.ADMINISTRATOR:
            if len(list(Courses.objects.filter(courseID=courseID))) > 0:
                Courses.objects.filter(courseID=courseID).delete()
                return True
        return False

    def createLab(self, labID, courseId, TA):
        if self.loggedInUser is not None and self.loggedInUser.clearance <= Clearance.INSTRUCTOR:
            if (len(list(Labs.objects.filter(LabID=labID))) == 0 and
                    len(list(Courses.objects.filter(courseID=courseId))) > 0 and
                    len(list(User.objects.filter(username=TA, clearance=Clearance.TA))) > 0):
                Labs(LabID=labID, courseID=courseId, tausername=TA).save()
                return True
        return False

    def deleteLab(self, LabID):
        if self.loggedInUser is not None and self.loggedInUser.clearance <= Clearance.ADMINISTRATOR:
            if len(list(Labs.objects.filter(LabID=LabID))) > 0:
                Labs.objects.filter(LabID=LabID).delete()
                return True
        return False

    def deleteAccount(self, username):
        if self.loggedInUser is not None and self.loggedInUser.clearance <= Clearance.SUPERVISOR:
            if len(list(User.objects.filter(username=username))) > 0:
                User.objects.filter(username=username).delete()
                return True
        return False

    @staticmethod
    def format_clearance(clearance):
        if clearance == 1:
            return "Supervisor"
        elif clearance == 2:
            return "Administrator"
        elif clearance == 3:
            return "Instructor"
        elif clearance == 4:
            return "TA"
        else:
            return "Unknown Clearance"

    def displayAccounts(self):
        if self.loggedInUser is not None and self.loggedInUser.clearance <= Clearance.ADMINISTRATOR:
            out = ""
            for user in list(User.objects.all()):
                out += "<p>(" + user.username + ", " + user.password + ", " + TASchedulingApp.format_clearance(user.clearance) + ")</p>"
            return out
        return "Could Not Display Accounts"

    def displayCourses(self):
        if self.loggedInUser is not None and self.loggedInUser.clearance <= Clearance.ADMINISTRATOR:
            out = ""
            for course in list(Courses.objects.all()):
                out += "<p>(" + str(course.courseID) + ", " + course.coursename + ", " + course.professor + ")</p>"
            return out
        return "Could Not Display Courses"

    def displayLabs(self):
        if self.loggedInUser is not None and self.loggedInUser.clearance <= Clearance.ADMINISTRATOR:
            out = ""
            for lab in list(Labs.objects.all()):
                out += "<p>(" + str(lab.LabID) + ", " + str(lab.courseID) + ", " + lab.tausername + ")</p>"
            return out
        return "Could Not Display Labs"

    def editCourse(self, uniqId, newUniqId, coursename, professor):
        if self.loggedInUser is not None and self.loggedInUser.clearance <= Clearance.ADMINISTRATOR:
            if (len(list(Courses.objects.filter(courseID=uniqId))) > 0 and
                    len(list(Courses.objects.filter(courseID=newUniqId))) == 0):
                Courses.objects.filter(courseID=uniqId).delete()
                Courses(courseID=newUniqId, coursename=coursename, professor=professor).save()
                return True
        return False

    def displayCoursesForProfessor(self):
        if self.loggedInUser is not None and self.loggedInUser.clearance == Clearance.INSTRUCTOR:
            out = ""
            for course in list(Courses.objects.filter(professor=self.loggedInUser.username)):
                out += "<p>Course: (" + str(course.courseID) + ", " + course.coursename + ", " + course.professor + ")</p>"
                for lab in list(Labs.objects.filter(courseID=course.courseID)):
                    out += "<p>Lab: (" + str(lab.LabID) + ", " + str(lab.courseID) + ", " + lab.tausername + ")</p>"
            return out
        return "Could Not Display Courses"

    def assignProfToCourse(self, courseid, profname):
        if self.loggedInUser is not None and self.loggedInUser.clearance < Clearance.ADMINISTRATOR:
            courses = list(Courses.objects.filter(courseID=courseid))
            if (len(courses) > 0 and
                    len(list(User.objects.filter(username=profname, clearance=Clearance.INSTRUCTOR))) > 0):
                Courses.objects.filter(courseID=courseid).delete()
                Courses(courseID=courseid, coursename=courses[0].coursename, professor=profname).save()
                return True
        return False

    def displayLabsForTA(self):
        if self.loggedInUser is not None and self.loggedInUser.clearance == Clearance.TA:
            out = ""
            for lab in list(Labs.objects.filter(tausername=self.loggedInUser.username)):
                out += "<p>(" + str(lab.LabID) + ", " + lab.courseID + ", " + lab.tausername + ")</p>"
            return out
        return "Could Not Display Labs"

    def assignTAToLab(self, labid, tausername):
        labs = list(Labs.objects.filter(LabID=labid))
        if (self.loggedInUser is not None and
                ((self.loggedInUser.clearance == Clearance.SUPERVISOR or
                    (self.loggedInUser.clearance == Clearance.INSTRUCTOR)))):
            if len(list(User.objects.filter(username=tausername))) == 1 and len(labs) == 1:
                Labs.objects.filter(LabID=labid).delete()
                Labs(labid, labs[0].courseID, tausername).save()
                return True
        return False

    def createContact(self, name, number, email):
        if self.loggedInUser is not None:
            if len(list(Contacts.objects.filter(instructor=name))) > 0:
                return False
            elif len(list(User.objects.filter(username=name))) == 1:
                Contacts(instructor=name, phone=number, email=email).save()
                return True
        return False

    def editContact(self, name, newName, newNumber, newEmail):
        if self.loggedInUser is not None:
            if len(list(Contacts.objects.filter(instructor=name))) == 1:
                Contacts.objects.filter(instructor=name).delete()
                Contacts(instructor=newName, phone=newNumber, email=newEmail).save()
                return True
            else:
                return False
        else:
            return False

    def displayContacts(self):
        if self.loggedInUser is not None:
            out = ""
            for contact in list(Contacts.objects.all()):
                out += "<p>Contacts: ID - " + str(contact.instructor) + ", Phone - " + contact.phone + ", Email - " + contact.email + "</p>"
            return out
        return "Could Not Display Contacts"

    def displayTAAssignments(self):
        if self.loggedInUser is not None and self.loggedInUser.clearance == 4:
            out = ""
            for TA in list(Labs.objects.all()):
                out += "<p>TA - " + str(TA.tausername) + ", courseID: - " + str(TA.courseID) + ", LabID: - " + str(TA.LabID) + "</p>"
            return out
        return "Could Not Display TA Assignments"

    def displayPublicAccounts(self):
        if self.loggedInUser is not None:
            out = ""
            for contact in list(Contacts.objects.all()):
                out += "<p>Contacts: ID - " + str(contact.instructor) + ", Phone - " + contact.phone + ", Email - " + contact.email + "</p>"
            return out
        return "Could Not Display Contacts"

