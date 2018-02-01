from __future__ import unicode_literals

from django.shortcuts import render
from cis.models import *
from cis.forms import *
from django.http import HttpResponseRedirect,HttpResponse

#from mis.forms import AccountForm,StudentForm
#from xhtml2pdf import pisa
# Create your views here.


def student_attandance(request):
	query = Attendance.objects.all()
	student_list = []
	for q in query:
		temp_dict = {}
		temp_dict['name'] = q.name
		temp_dict['attendance']= q.attendance
		temp_dict['time'] = q.time
		temp_dict['date'] = q.date
		student_list.append(temp_dict)

	context_dict = {'query':student_list}
	return render(request,'attandance.html',context_dict)

def student_exam(request):
	query = Exam.objects.all()
	student_list = []
	for q in query:
		temp_dict = {}
		temp_dict['TestName']= q.TestName
		temp_dict['Course'] = q.Course
        temp_dict['MarksObtain'] = q.MarksObtain
        temp_dict['FullMarks'] = q.FullMarks
        temp_dict['PassMarks'] = q.PassMarks
        temp_dict['Result'] = q.Result

        student_list.append(temp_dict)

	context_dict = {'query':student_list}
	return render(request,'exam.html',context_dict)
def student_marks(request):
	query = Marks.objects.all()
	student_list = []
	for q in query:
		temp_dict = {}
		temp_dict['name'] = q.name
		temp_dict['Exam']= q.exam
		student_list.append(temp_dict)

	context_dict = {'query':student_list}
	return render(request,'marks.html',context_dict)

def attendance_add(request):
	if request.method == 'POST':
		forms = AttendanceForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = AttendanceForm()
	context_dict = {'forms':forms}
	return render (request,'form.html',context_dict)

def marks_add(request):
	if request.method == 'POST':
		forms = MarksForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = MarksForm()
	context_dict = {'forms':forms}
	return render (request,'form.html',context_dict)


def exam_form(request):
	if request.method == 'POST':
		forms = ExamForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = MarksForm()
	context_dict = {'forms':forms}
	return render (request,'form.html',context_dict)
