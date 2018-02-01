# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from mis.models import *
from mis.forms import AccountForm,StudentForm
from django.http import HttpResponseRedirect,HttpResponse
from xhtml2pdf import pisa

# Create your views here.
# def get_batch_list(request):
# 	if request.method =='POST':
# 		sel_course = request.POST.get('course_list')
# 		s_query = Student.objects.filter(course__course_name=sel_course)
# 		course_taken = ''
# 		for q in s_query:
# 			student_name = q.first_name+' '+q.last_name
# 			for i in q.course.all():
# 				course_taken = ','+course_taken+ i.course_name 



# 		context_dict = {'student_name':student_name,'course_taken':course_taken, 'batch_name':sel_batch}
# 		return render(request,'student_list.html',context_dict)
# 	else:
# 		form = BatchForm()
# 	context_dict = {'form':form}
# 	return render(request,'batch_form.html',context_dict)

# def get_student_list_by_batch(request):
# 	print request.method
# 	pass

from django.contrib.auth.decorators import login_required
@login_required(login_url='/admin/')
def home(request):
	return render(request,'home.html')
# def register(request):
# 	if request.method=='POST':
# 		form = StudentForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect('/')
# 	else:
# 		form = StudentForm()
# 	context_dict = {'form':form}
# 	return render(request,'register.html',context_dict)
def student_list(request):
	query = Student.objects.all()
	student_list = []
	for q in query:
		temp_dict = {}
		temp_dict['name'] = q.first_name+''+q.last_name
		temp_dict['s_id']= q.id
		temp_dict['email'] = q.email
		c = 0
		c_name = ''
		c_fee=0
		for i in q.course.all():
			c = c+1
			c_name = c_name+i.course_name+' '
			c_fee = c_fee + i.fee
		temp_dict['number_of_course']=c
		temp_dict['course_taken'] = c_name
		temp_dict['c_fee'] = c_fee
		student_list.append(temp_dict)
	# print student_list

	context_dict = {'query':student_list}
	return render(request,'student_list.html',context_dict)

def account_detail(request,pid):
	s_query = Account.objects.filter(student__id=pid)
	student = Student.objects.get(id=pid)
	s_name = student.first_name+' '+student.last_name
	t_f = 0
	# c_name = ''
	for q in student.course.all():
		t_f = t_f+(q.fee-q.fee*q.discount)


	t_p = 0
	for q in s_query:
		t_p = t_p+q.payment_amount

	if t_p<t_f:
		due_amount = t_f-t_p
	else:
		due_amount = 'No Due'

	context_dict = {'s_query':s_query,'s_name':s_name,'total_fee':t_f,'due_amount':due_amount,'student':student}

	template = get_template('account_detail.html')
	html  = template.render(context_dict)
	result = StringIO.StringIO()
	pdf = pisa.pisaDocument(StringIO.StringIO(html), dest=result) 
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	else: 
		return HttpResponse('Errors') 
	# return render(request,'account_detail.html',context_dict)

from django.template import Context
from django.template.loader import get_template
import datetime
from django.template.loader import render_to_string
import os
import cStringIO as StringIO 
import datetime



def make_payment(request):
	if request.method=='POST':
		# data = {}
		# data['today'] = datetime.date.today()
		# data['farmer'] = 'Old MacDonald'
		# data['animals'] = [('Cow', 'Moo'), ('Goat', 'Baa'), ('Pig', 'Oink')]
		
		s_id = int(request.POST.get('student'))
		student = Student.objects.get(id=s_id)
		full_name = student.first_name+' '+student.last_name

		total_fee = 0
		c_name = ' '
		for q in student.course.all():
			total_fee = total_fee+(q.fee-q.fee*q.discount)
			c_name = c_name+q.course_name+' '

		total_paid = 0

		s_query = Account.objects.filter(student__id=s_id)

		for q in s_query:
			total_paid = total_paid+q.payment_amount
		total_paid = total_paid+int(request.POST.get('payment_amount'))

		if total_paid<total_fee:
			due_amount = total_fee-total_paid
		else:
			due_amount = 'No Due'

		data = {}
		data['full_name'] = full_name
		data['total_fee'] = total_fee
		data['total_paid'] = total_paid
		data['due_amount'] = due_amount
		data['course_name'] = c_name

		now = datetime.datetime.now()
		data['time'] = now.strftime("%Y-%m-%d")




		template = get_template('invoice.html')
		html  = template.render(data)

		# file = open('invoice.pdf', "w+b")
		# pisaStatus = pisa.CreatePDF(html, dest=file)

		result = StringIO.StringIO()
		pdf = pisa.pisaDocument(StringIO.StringIO(html), dest=result) 
		form = AccountForm(request.POST)
		print request.POST
		if form.is_valid():
			form.save()
			# return HttpResponseRedirect('/student/list/')
			return HttpResponse(result.getvalue(),content_type='application/pdf')
	else:
		form = AccountForm()
	context_dict = {'form':form}
	return render(request,'ac_payment.html',context_dict)


from django.contrib.auth import authenticate, login,logout
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')