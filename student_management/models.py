
from django.db import models

class Student_Details(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    branch=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=30)
    score=models.IntegerField()

    def Meta(self):
        db_table='student_details'


    

# Create your models here.
