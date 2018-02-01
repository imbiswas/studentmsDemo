"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mis import views as mv
from cis import views as cv

from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',mv.home,name='home'),
    # url(r'^new/register/$',views.register,name='register'),
    # url(r'^batch/list/$',views.get_batch_list,name='batch_list'),
    # url(r'^student/list/bybatch/$',views.get_student_list_by_batch,name='student_list')
    url(r'^student/list/$',mv.student_list,name='student_list'),
    url(r'^account/detail/(?P<pid>\d+)/$', mv.account_detail, name='account_detail'),
    url(r'^make/payment/$',mv.make_payment,name='make_payment'),
    url(r'^logout/$',mv.logout_page,name="logingout"),
    url(r'^attendance/$',cv.student_attandance,name='attandance_details'),
    url(r'^marks/$',cv.student_marks,name='marks_details'),
    url(r'^exam/$',cv.student_exam,name='student_exam'),
    url(r'^marksadd/$',cv.marks_add,name='marksadd'),
    url(r'^attadd/$',cv.attendance_add,name='attadd'),
    url(r'^examform/$',cv.exam_form,name='examdorm'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Change admin site title
admin.site.site_header = _("Infography Technologies Administration")
admin.site.site_title = _("MIS Site Admin")
 # s = Student.objects.filter(batch__name='dj-001-2017')
