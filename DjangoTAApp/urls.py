"""DjangoTAApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

admin.autodiscover()
from django.urls import path
from DjangoTAApp.views import Home
from DjangoTAApp.views import Login
from DjangoTAApp.views import EditAccount
from DjangoTAApp.views import DeleteAccount
from DjangoTAApp.views import DisplayAccounts
from DjangoTAApp.views import DisplayCourses
from DjangoTAApp.views import DisplayLabs
from DjangoTAApp.views import EditContact
from DjangoTAApp.views import CreateAccount
from DjangoTAApp.views import CreateCourse
from DjangoTAApp.views import EditCourse
from DjangoTAApp.views import CreateLab
from DjangoTAApp.views import AssignProfToCourses
from DjangoTAApp.views import AssignTAtoLab
from DjangoTAApp.views import DisplayPublicAccounts
from DjangoTAApp.views import DisplayProfCourses
from DjangoTAApp.views import DisplayTALabs

urlpatterns = [
    path('', Login.as_view()),
    path('Home/', Home.as_view()),
    path('Home/EditAccount/', EditAccount.as_view()),
    path('Home/DeleteAccount/', DeleteAccount.as_view()),
    path('Home/DisplayAccounts/', DisplayAccounts.as_view()),
    path('Home/DisplayCourses/', DisplayCourses.as_view()),
    path('Home/DisplayLabs/', DisplayLabs.as_view()),
    path('Home/EditContact/', EditContact.as_view()),
    path('Home/CreateAccount/', CreateAccount.as_view()),
    path('Home/CreateCourse/', CreateCourse.as_view()),
    path('Home/EditCourse/', EditCourse.as_view()),
    path('Home/CreateLab/', CreateLab.as_view()),
    path('Home/AssignProfToCourses/', AssignProfToCourses.as_view()),
    path('Home/AssignTAtoLab/', AssignTAtoLab.as_view()),
    path('Home/DisplayPublicAccounts/', DisplayPublicAccounts.as_view()),
    path('Home/DisplayProfCourses/', DisplayProfCourses.as_view()),
    path('Home/DisplayTALabs/', DisplayTALabs.as_view())
]
