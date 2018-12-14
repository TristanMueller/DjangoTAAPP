from django.shortcuts import render

from django.views import View

from Commands import CommandHandler

from django.shortcuts import redirect

from django.http import HttpResponseRedirect

from DjangoTAApp.models import User

from DjangoTAApp.models import Courses

from DjangoTAApp.models import  Contacts



# Create your views here.

com = CommandHandler()


class Login(View):

    def get(self, request):

        return render(request, "Login.html", {'out': ""})

    def post(self, request):

        username = request.POST["username"]

        password = request.POST["password"]

        out = com.command(["Login", username, password])

        if out != "Logged In":

            return render(request, "Login.html", {'out': out})

        else:

            return HttpResponseRedirect("Home/")


class Home(View):

    def get(self, request):
        links = ""
        if com.currentClearance() == 4:
            links = self.TA()
        elif com.currentClearance() == 3:
            links = self.Professor()
        elif com.currentClearance() == 2:
            links = self.Admin()
        elif com.currentClearance() == 1:
            links = self.Supervisor()

        return render(request, "Main.html", {'out': '', 'links': links})

    def post(self, request):

        links = ""
        if com.currentClearance() == 4:
            links = self.TA()

        post = request.POST["command"]
        out = com.command(post.split())

        return render(request, "Main.html", {'out': out, 'links': links})

    def TA(self):
        return "<a href=""/Home/EditContact/"">Edit your contact info</a><br>\
        <a href=""#"">View TA assignments</a><br> \
        <a href=""/Home/DisplayPublicAccounts"">Contact Book</a>"

    def Professor(self):
        return "<a href=""/Home/EditContact/"">Edit your contact info</a><br> \
        <a href=""#"">View TA assignments</a><br> \
        <a href=""/Home/DisplayPublicAccounts/"">Contact Book</a><br> \
        <a href=""#"">View Course Assignments</a><br> \
        <a href=""#"">Assign TAs</a>"

    def Admin(self):
        return "<a href=""/Home/CreateCourse"">Create Courses</a><br> \
        <a href=""/Home/EditCourse"">Edit Courses</a><br> \
        <a href=""/Home/CreateAccount"">Create Accounts</a><br> \
        <a href=""/Home/DisplayPublicAccounts/"">Contact Book</a><br> \
        <a href=""#"">Delete Accounts</a><br> \
        <a href=""/Home/EditAccount/"">Edit Accounts</a><br> \
        <a href=""#"">Access all data</a>"

    def Supervisor(self):
        return "<a href=""/Home/CreateCourse"">Create Courses</a><br> \
        <a href=""/Home/EditCourse"">Edit Courses</a><br> \
        <a href=""/Home/CreateAccount"">Create Accounts</a><br> \
        <a href=""/Home/DisplayPublicAccounts/"">Contact Book</a><br> \
        <a href=""#"">Delete Accounts</a><br> \
        <a href=""/Home/EditAccount/"">Edit Accounts</a><br> \
        <a href=""#"">Access all data</a><br> \
        <a href=""#"">Assign Professors To Courses</a><br> \
        <a href=""#"">Assign TAs to Labs</a>"

class EditAccount(View):

    def get(self, request):
        if com.currentClearance() < 3:
            users = list(User.objects.all())
        else:
            users = list(User.objects.filter(username=com.currentUser()))

        return render(request, "EditAccount.html", {'users': users, 'out': ""})

    def post(self, request):

        oldusername = request.POST["oldusername"]

        username = request.POST["username"]

        password = request.POST["password"]

        clearance = request.POST["clearance"]

        out = com.command(["EditAccount", oldusername, username, password, clearance])

        users = list(User.objects.all())

        return render(request, "EditAccount.html", {'users': users, 'out': out})


class EditContact(View):

    def get(self, request):
        if com.currentClearance() < 3:
            contacts = list(Contacts.objects.all())
        else:
            contacts = list(Contacts.objects.filter(instructor=com.currentUser()))

        return render(request, "EditContacts.html", {'contacts': contacts, 'out': ""})

    def post(self, request):

        username = request.POST["username"]

        email = request.POST["email"]

        phone = request.POST["phone"]

        out = com.command(["EditContact", username, username, phone, email])

        if com.currentClearance() < 3:
            contacts = list(Contacts.objects.all())
        else:
            contacts = list(Contacts.objects.filter(instructor=com.currentUser()))

        return render(request, "EditContacts.html", {'contacts': contacts, 'out': out})


class DisplayPublicAccounts(View):

    def get(self, request):
        out = com.command(["DisplayPublicAccounts"])
        return render(request, "DisplayPublicAccounts.html", {'out': out})

    def post(self, request):
        out = com.command(["DisplayPublicAccounts"])
        return render(request, "DisplayPublicAccounts.html", {'out': out})


class CreateAccount(View):

    def get(self, request):
        return render(request, "CreateAccount.html", {'out': ""})

    def post(self, request):

        username = request.POST["username"]

        password = request.POST["password"]

        clearance = request.POST["clearance"]

        out = com.command(["CreateAccount", username, password, clearance])

        return render(request, "CreateAccount.html", {'out': out})

class CreateCourse(View):

    def get(self, request):
        return render(request, "CreateCourse.html", {'out': ""})

    def post(self, request):

        courseid = request.POST["courseid"]

        coursename = request.POST["coursename"]

        courseprof = request.POST["courseprof"]

        out = com.command(["CreateCourse", courseid, coursename, courseprof])

        return render(request, "CreateCourse.html", {'out': out})


class EditCourse(View):

    def get(self, request):

        courses = list(Courses.objects.all())

        return render(request, "EditCourse.html", {'courses': courses, 'out': ""})

    def post(self, request):

        oldid = request.POST["oldid"]

        newid = request.POST["newid"]

        coursename = request.POST["coursename"]

        professor = request.POST["professor"]

        out = com.command(["EditCourse", oldid, newid, coursename, professor])

        courses = list(Courses.objects.all())

        return render(request, "EditCourse.html", {'courses': courses, 'out': out})
