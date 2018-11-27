from django.shortcuts import render
from django.views import View
from Commands import CommandHandler
from DjangoTAApp.models import User,Courses,Labs

# Create your views here.
com = CommandHandler()

class Home(View):

    def get(self, request):
        return render(request, "Main.html", {'out': ""})

    def post(self, request):
        out = com.command(request.POST["command"].split())
        return render(request, "Main.html", {'out': out})
