# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Address(models.Model):
	house_no = models.CharField(max_length=10)
	ward_no = models.CharField(max_length=3)
	street = models.CharField(max_length=20)
	district = models.CharField(max_length=20)
	municipal_vdc = models.CharField(max_length=20)
	area = models.CharField(max_length=20)

	def __str__(self):
		return '%s'%(self.district)

class Course(models.Model):
	course_name = models.CharField(max_length=20)
	duration = models.CharField(max_length=20,help_text='specify duration in weeks')
	fee = models.DecimalField(max_digits=10, decimal_places=2)
	discount = models.DecimalField(max_digits=10, decimal_places=2)
	batch = models.CharField(max_length=50,help_text='eg:ds-001-2017, use py-python,dj-django,ds-datascience ')

	
	def __str__(self):
		return '%s'%(self.course_name)

# class Batch(models.Model):
# 	name = models.CharField(max_length=50,help_text='eg:ds-001-2017, use py-python,dj-django,ds-datascience ')

# 	def __str__(self):
# 		return '%s'%(self.name)

class Student(models.Model):
	title_choices = (
		('Mr.','Mr.'),
		('Mrs.','Mrs.'),
		('Miss','Miss'),
		('Ms','Ms')
		)
	gender_choices = (
		('Male','Male'),
		('Female','Female'),
		('NA','Prefer Not To Say')
		)
	title = models.CharField(max_length=5,choices=title_choices)
	first_name = models.CharField(max_length=20)
	middle_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	gender = models.CharField(max_length=20,choices=gender_choices)
	date_of_birth = models.DateField()
	qualification = models.CharField(max_length=50)
	telephone = models.CharField(max_length=14)
	mobile_number = models.CharField(max_length=14)
	email = models.EmailField()
	address = models.ForeignKey(Address,on_delete=models.CASCADE)
	# batch = models.ManyToManyField(Batch)
	course = models.ManyToManyField(Course)
	join_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return '%s%s'%(self.first_name,self.last_name)

class Account(models.Model):
	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	date_of_payment = models.DateField(auto_now_add=True)
	payment_amount = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return '%s'%(self.student)