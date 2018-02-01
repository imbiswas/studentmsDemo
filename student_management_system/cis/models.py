from __future__ import unicode_literals
from django.db import models
from mis.models import Student,Course
from cis.models import *

class Attendance(models.Model):
    name=models.ForeignKey(Student,on_delete=models.CASCADE)
    attendance=models.BooleanField()
    time=models.TimeField(auto_now_add=True)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s'%(self.name)



class Exam(models.Model):
    #name=models.ForeignKey(Student,on_delete=models.CASCADE)
    result_choices = (
		('Pass','Pass'),
		('Fail','Fail'),
		('Absent','Absent'),
		('Withheld','Withheld')
		)



    TestName=models.CharField(max_length=10)
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    MarksObtain=models.DecimalField(max_digits=4, decimal_places=1)
    FullMarks=models.DecimalField(max_digits=4, decimal_places=1)
    PassMarks=models.DecimalField(max_digits=4, decimal_places=1)
    Result=models.CharField(max_length=8,choices=result_choices)

    def __str__(self):
        return '%s'%(self.TestName)

class Marks(models.Model):
    name=models.ForeignKey(Student,on_delete=models.CASCADE)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)

    def __str__(self):
        return '%s'%(self.name)
