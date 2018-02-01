import pytest
from django.contrib.auth.models import User
from mis.models import Address,Course,Student,Account



#checking super user

@pytest.mark.django_db
def test_my_user():
   # me = User.objects.get(username='biswas')
   # assert me.is_superuser
   pass








@pytest.mark.django_db
def test_address():
    add=Address.objects.create(house_no = '1',ward_no = '1',street = 'aaa',district ='bbb',municipal_vdc = 'ccc',area = 1)
    add.save()
    assert add.house_no == "1"
    assert add.ward_no == "1"
    assert add.street=='aaa'
    assert add.district=='bbb'
    assert add.municipal_vdc=='ccc'
    assert add.area==1

@pytest.mark.django_db
def test_course():
    cou=Course.objects.create(course_name="cc1",duration="1",fee=100,discount=0.3,batch='apple')
    cou.save()
    assert cou.course_name=="cc1"
    assert cou.duration=="1"
    assert cou.fee==100
    assert cou.discount==0.3
    assert cou.batch=="apple"


@pytest.mark.django_db
def test_student():
	a = Address.objects.create(house_no = '1',ward_no = '1',street = 'aaa',district ='bbb',municipal_vdc = 'ccc',area = 1)
	cou=Course.objects.create(course_name="cc1",duration="1",fee=100,discount=0.3,batch='apple')
	std=Student.objects.create(title = "Mr.",first_name="kale",middle_name="bhale",last_name="ball",gender='NA',date_of_birth='2011-11-11',qualification = "NA",telephone = "NA",mobile_number = "NA",email = "apple@gmail.com",address = a,join_date = "2014-11-11")
	std.course.add(cou)
	std.save()
	assert std.first_name=="kale"



@pytest.mark.django_db
def test_account():
	a = Address.objects.create(house_no = '1',ward_no = '1',street = 'aaa',district ='bbb',municipal_vdc = 'ccc',area = 1)
	cou=Course.objects.create(course_name="cc1",duration="1",fee=100,discount=0.3,batch='apple')
	std=Student.objects.create(title = "Mr.",first_name="kale",middle_name="bhale",last_name="ball",gender='NA',date_of_birth='2011-11-11',qualification = "NA",telephone = "NA",mobile_number = "NA",email = "apple@gmail.com",address = a,join_date = "2014-11-11")
	std.course.add(cou)
	acc=Account.objects.create(student = std,date_of_payment = "2014-11-11",payment_amount = 100)
	acc.save()
	assert acc.payment_amount==100