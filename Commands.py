from TASchedulingApp import TASchedulingApp
from DjangoTAApp.models import User, Courses, Contacts, Labs

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
            if app.createAccount(args[1], args[2], int(args[3])):
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
        elif args[0] == "DisplayAccounts":
            return app.displayAccounts()

        elif args[0] == "DisplayCourses":
            return app.displayCourses()

        elif args[0] == "DisplayLabs":
            return app.displayLabs()

        elif args[0] == "EditCourse":
          if app.editCourse(args[1], args[2], args[3]):
              return "Edited Course"
          else:
              return "Could Not Edit Course"

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

        elif args[0] == "Help":
            return commandlist()
        else:
            return "Error"

def commandlist():
    out = ["Commands"]
    out.append("Login <username> <password>")
    out.append("Logout")
    out.append("CreateAccount <username> <password> <clearance(1-4)>")
    out.append("EditAccount <username> <new username> <new password> <new clearance(1-4)>")
    out.append("CreateCourse <course ID> <course name> <professor name>")
    out.append("CreateLab <lab ID> <course ID> <ta name>")
    out.append("DeleteAccount <username>")
    out.append("DisplayAccounts")
    out.append("DisplayCourses")
    out.append("DisplayLabs")
    return out


