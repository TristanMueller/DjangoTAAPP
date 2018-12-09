from django.shortcuts import render
from django.views import View
from Commands import CommandHandler
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

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
        return render(request, "Main.html", {'out': ""})

    def post(self, request):
        out = com.command(request.POST["command"].split())
        return render(request, "Main.html", {'out': out})
