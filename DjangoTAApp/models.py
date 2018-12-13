from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    clearance = models.IntegerField(default=0)

class Courses(models.Model):
    courseID = models.IntegerField(default=0)
    coursename = models.CharField(max_length=20)
    professor = models.CharField(max_length=20)

class Labs(models.Model):
    LabID = models.IntegerField(default=0)
    courseID = models.CharField(max_length=20)
    tausername = models.CharField(max_length=20)

class Contacts(models.Model):
    instructor = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

