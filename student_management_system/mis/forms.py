from django import forms
from mis.models import Course,Account,Student

# class CourseForm(forms.Form):
# 	query = Course.objects.all()
# 	course_list = forms.ChoiceField(choices=[(q.course_name,q.course_name) for q in query])

class AccountForm(forms.ModelForm):
	class Meta:
		model = Account 
		fields = '__all__'

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'