from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime    

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=20)
    usertype=models.CharField(max_length=20)
    viewPassword=models.CharField(max_length=200,null=True)
    status = models.CharField(max_length=20,null=True,default="Approved")

class Coder(models.Model):
    loginid = models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    photo=models.ImageField(upload_to="Image",null=True)
    fullname = models.CharField(max_length=20)
    username=models.EmailField()
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=200)
    dob = models.DateField()
    intro = models.CharField(max_length=200)
    role = models.CharField(max_length=20)

class Buyer(models.Model):
    loginid = models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    photo = models.ImageField(upload_to="Image",null=True)
    username = models.CharField(max_length=20)
    fullname = models.CharField(max_length=20)
    mobile = models.IntegerField(null=True)
    dob = models.DateField()
    address = models.CharField(max_length=200)
    role = models.CharField(max_length=20)

class Skills(models.Model):
    coderid = models.ForeignKey(Coder,on_delete=models.CASCADE,null=True)
    skills = models.CharField(max_length=20)

class BuyerData(models.Model):
    buyerid = models.ForeignKey(Buyer,on_delete=models.CASCADE,null=True)
    company = models.CharField(max_length=100)
    companydetails = models.CharField(max_length=200)
    buyerdetails = models.CharField(max_length=200)

class Projects(models.Model):
    buyerid = models.ForeignKey(Buyer,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100)
    jobtype = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    duration = models.IntegerField()
    salary = models.IntegerField()
    experience = models.IntegerField()
    careerlevel = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    status = models.CharField(max_length=20,null=True)
    today = models.DateField()
    attachment = models.ImageField(upload_to="Image",null=True)
    assignstatus = models.CharField(max_length=20,null=True)
    doneby = models.ForeignKey(Coder,on_delete=models.CASCADE,null=True)
    finalupload = models.FileField(upload_to="file",null=True)
    uploaddate = models.DateField(null=True)
    prototype = models.FileField(upload_to="file",null=True)
    projectstatus =  models.CharField(max_length=20,null=True)
    
class ApplyProject(models.Model):
    coderid = models.ForeignKey(Coder,on_delete=models.CASCADE,null=True)
    projectid = models.ForeignKey(Projects,on_delete=models.CASCADE,null=True)
    date = models.DateField()
    status = models.CharField(max_length=20,null=True,default="Pending")
    finalstatus = models.CharField(max_length=20,null=True)

class CoderReview(models.Model):
    coderid = models.ForeignKey(Coder,on_delete=models.CASCADE,null=True)
    buyerid = models.ForeignKey(Buyer,on_delete=models.CASCADE,null=True)
    review = models.IntegerField()
    feedback =  models.CharField(max_length=400,null=True)



    
class Chat(models.Model):
    coderid = models.ForeignKey(Coder, on_delete=models.CASCADE)
    buyerid = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    time = models.CharField(max_length=100)
    utype = models.CharField(max_length=100)

