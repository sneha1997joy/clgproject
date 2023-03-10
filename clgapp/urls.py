from django.urls import path
from clgapp import views
from django.contrib import admin

urlpatterns=[
path('',views.home,name='home'),

path('signuppage',views.signuppage,name='signuppage'),
path('usercreate',views.usercreate,name='usercreate'),

path('loginpage',views.loginpage,name='loginpage'),
path('userlogin',views.userlogin,name='userlogin'),

path('admin_home',views.admin_home,name='admin_home'),
path('addcoursepage',views.addcoursepage,name='addcoursepage'),
path('addcourse',views.addcourse,name='addcourse'),

path('user_home',views.user_home,name='user_home'),
path('editpage/<int:id>',views.editpage,name='editpage'),
path('editteacher/<int:id>',views.editteacher,name='editteacher'),

path('showcourse',views.showcourse,name='showcourse'),

path('deletepage/<int:id>',views.deletepage,name='deletepage'),
path('deletecourse/<int:id>',views.deletecourse,name='deletecourse'),
path('addstudentpage',views.addstudentpage,name='addstudentpage'),
path('addstudent',views.addstudent,name='addstudent'),

path('showstudent',views.showstudent,name='showstudent'),
path('deletestudent/<int:id>',views.deletestudent,name='deletestudent'),
path('deletepages/<int:id>',views.deletepages,name='deletepages'),
path('showteacher',views.showteacher,name='showteacher'),
path('deletepaget/<int:id>',views.deletepaget,name='deletepaget'),
path('deleteteacher/<int:id>',views.deleteteacher,name='deleteteacher'),
path('adminlogout',views.adminlogout,name='adminlogout')
]