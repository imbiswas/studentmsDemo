# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mis.models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','mobile_number','email')
	list_filter = ('first_name',)
	search_fields = ['course__batch']

admin.site.register(Student,StudentAdmin)
admin.site.register(Address)
admin.site.register(Course)
admin.site.register(Account)
# admin.site.register(Batch)

from django.contrib.auth.models import Group,User

admin.site.unregister(Group)
admin.site.unregister(User)

# from django.contrib.admin.models import LogEntry
#
# LogEntry.objects.all().delete()
