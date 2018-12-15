from TASchedulingApp import TASchedulingApp
from DjangoTAApp.models import User, Courses, Labs, Contacts

app = TASchedulingApp()


class CommandHandler():

    def __init__(self):
        pass

    @staticmethod
    def command(args):
        if args[0] == "Login":
            if app.login(args[1], args[2]):
                return "Logged In"
            else:
                return "Could not login"
        elif args[0] == "Logout":
            if app.logout():
                return "Logged Out"
            else:
                return "Could Not Logout"

        elif args[0] == "CreateAccount":
            if app.createAccount(args[1], args[2], args[3]):
                return "Created New Account"
            else:
                return "Could Not Create New Account"
        elif args[0] == "EditAccount":
            if app.editAccount(args[1], args[2], args[3], int(args[4])):
                return "Edited Account"
            else:
                return "Could Not Edit Account"
        elif args[0] == "CreateCourse":
            if app.createCourse(args[1], args[2], args[3]):
                return "Created New Course"
            else:
                return "Could Not Create New Course"
        elif args[0] == "CreateLab":
            if app.createLab(int(args[1]), int(args[2]), args[3]):
                return "Created New Lab"
            else:
                return "Could Not Create New Lab"
        elif args[0] == "DeleteAccount":
            if app.deleteAccount(args[1]):
                return "Deleted Account"
            else:
                return "Could Not Delete Account"

        elif args[0] == "DeleteCourse":
            if app.deleteCourse(args[1]):
                return "Deleted Course"
            else:
                return "Could Not Delete Course"

        elif args[0] == "DeleteLab":
            if app.deleteLab(args[1]):
                return "Deleted Lab"
            else:
                return "Could Not Delete Lab"

        elif args[0] == "DisplayAccounts":
            return app.displayAccounts()

        elif args[0] == "DisplayCourses":
            return app.displayCourses()

        elif args[0] == "DisplayLabs":
            return app.displayLabs()

        elif args[0] == "EditCourse":
            if app.editCourse(args[1], args[2], args[3], args[4]):
                return "Edited Course"
            else:
                return "Could Not Edit Course"

        elif args[0] == "AssignTAToLab":
            if app.assignTAToLab(args[1], args[2]):
                return "Assigned TA To Lab"
            else:
                return "Could Not Assign TA To Lab"

        elif args[0] == "AssignProfToCourses":
            if app.assignProfToCourse(args[1], args[2]):
                return "Assigned Professor to Course"
            else:
                return "Could Not Assign Professor to Course"

        elif args[0] == "CreateContact":
            if app.createContact(args[1], args[2], args[3]):
                return "Created New Contact"
            else:
                return "Could Not Create New Contact"

        elif args[0] == "EditContact":
          if app.editContact(args[1], args[2], args[3], args[4]):
              return "Edited Contact"
          else:
              return "Could Not Edit Contact"

        elif args[0] == "DisplayContacts":
            return app.displayContacts()

        elif args[0] == "DisplayMyCourses":
            return app.displayCoursesForProfessor()

        elif args[0] == "DisplayMyLabs":
            return app.displayLabsForTA()

        elif args[0] == "DisplayTAAssignments":
            return app.displayTAAssignments()

        elif args[0] == "DisplayPublicAccounts":
            return app.displayPublicAccounts()

        elif args[0] == "Help":
            return commandlist()
        else:
            return "Error"

    def currentClearance(self):
        return app.LoggedInUser.clearance

    def currentUser(self):
        return app.LoggedInUser.username


def commandlist():
    out = "<h1>Commands</h1>"
    out += "<p>Login (username) (password)</p>"
    out += "<p>Logout</p>"
    out += "<p>CreateAccount (username) (password) (clearance(1-4))</p>"
    out += "<p>EditAccount (username) (new username) (new password) (new clearance(1-4))</p>"
    out += "<p>CreateCourse (course ID) (course name) (professor name)</p>"
    out += "<p>CreateLab (lab ID) (course ID) (ta name)</p>"
    out += "<p>CreateContact (instructor ID #) (phone #) (e-mail)</p>"
    out += "<p>EditContact (old instructor ID #) (new instructor ID #) (new phone #) (new e-mail)</p>"
    out += "<p>DisplayContacts</p>"
    out += "<p>DeleteAccount (username)</p>"
    out += "<p>DisplayAccounts</p>"
    out += "<p>DisplayCourses</p>"
    out += "<p>DisplayLabs</p>"
    out += "<p>DisplayMyCourses</p>"
    out += "<p>DisplayMyLabs</p>"
    return out


