from django.db import models

# Create your models here.
class CourseModel(models.Model):
    Course_Name=models.CharField(max_length=100)
    Course_Fees=models.IntegerField()
   
class StudentModels(models.Model):
    Student_Name=models.CharField(max_length=100)
    Phone_Number=models.IntegerField()
    Gender=models.CharField(max_length=100)
    Address=models.CharField(max_length=200)
    Join_Date=models.DateField(auto_now=True)
    Course_Name=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)

    

class TeacherModel(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    User_Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=200)
    Email=models.CharField(max_length=100)
    Age=models.IntegerField()
    Course_Name=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to="image/",null=True) 
    