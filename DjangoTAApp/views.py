from django.shortcuts import render

from django.views import View

from Commands import CommandHandler

from django.shortcuts import redirect

from django.http import HttpResponseRedirect

from DjangoTAApp.models import User



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
        return render(request, "Main.html", {'out': '', 'links': links})



    def post(self, request):

        links = ""
        if com.currentClearance() == 4:
            links = self.TA()

        post = request.POST["command"]

        if post == "EditAccount":

            return HttpResponseRedirect("EditAccount/")

        out = com.command(post.split())

        return render(request, "Main.html", {'out': out, 'links': links})

    def TA(self):
        return "<a href=""#"">Edit your contact info</a><br> \
        <a href=""#"">View TA assignments</a><br> \
        <a href=""#"">Contact Book</a>"

    #def Professor(self):

    #def Admin(self):

    #def Supervisor(self):




class EditAccount(View):



    def get(self, request):

        users = list(User.objects.all())

        return render(request, "EditAccount.html", {'users': users, 'out': ""})



    def post(self, request):

        oldusername = request.POST["oldusername"]

        username = request.POST["username"]

        password = request.POST["password"]

        clearance = request.POST["clearance"]

        out = com.command(["EditAccount", oldusername, username, password, clearance])

        users = list(User.objects.all())

        return render(request, "EditAccount.html", {'users': users, 'out': out})