from User import User
from Course import Course
from DjangoTAApp.models import User, Courses, Labs

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
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3:
            labs = list(Labs.objects.filter(LabID=iLabID))
            if len(labs) > 0:
                return False
            else:
                lab = Labs(LabID=iLabID, courseID=iCourseId, tausername=sTA)
                lab.save()
                return True
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
        out = []
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3:
            users = list(User.objects.all())
            for user in users:
                out.append("(" + user.username + ", " + user.password + ", " + str(user.clearance) + ")")
            return out
        return "Could Not Display Accounts"

    def displayCourses(self):
        out = []
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3:
            courses = list(Courses.objects.all())
            for course in courses:
                out.append("(" + str(course.courseID) + ", " + course.coursename + ", " + course.professor + ")")
            return out
        return "Could Not Display Courses"

    def displayLabs(self):
        out = []
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3:
            labs = list(Labs.objects.all())
            for lab in labs:
                out.append("(" + str(lab.LabID) + ", " + str(lab.courseID) + ", " + lab.tausername + ")")
            return out
        return "Could Not Display Labs"

    def editCourse(self, uniqId, newUniqId, coursename, professor):
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 2:
            courses = list(Courses.objects.filter(courseID=uniqId))
            if len(courses) == 1:
                Courses.objects.filter(courseID=uniqId).delete()
                course = Courses(courseID=newUniqId, coursename=coursename, professor=professor)
                course.save()
                return True
            else:
                return False
        else:
            return False
