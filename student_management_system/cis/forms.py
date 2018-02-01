from django import forms
from cis.models import *

# class CourseForm(forms.Form):
# 	query = Course.objects.all()
# 	course_list = forms.ChoiceField(choices=[(q.course_name,q.course_name) for q in query])

class AttendanceForm(forms.ModelForm):
	class Meta:
		model = Attendance
		fields = '__all__'

class MarksForm(forms.ModelForm):
	class Meta:
		model = Marks
		fields = '__all__'
class ExamForm(forms.ModelForm):
	class Meta:
		model = Exam
		fields = '__all__'
