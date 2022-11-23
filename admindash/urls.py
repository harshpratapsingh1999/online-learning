from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="admindash"),
    path('users/',views.users,name="user"),
    path('bill/',views.bill,name="bill"),
    path('account/',views.account,name="account"),
    path('courses/',views.course,name="courses"),
    path('logout',views.logout,name="logout"),
    path('courses/addcourseform',views.addcourseform,name="addcourseform"),
    path('courses/addcourse',views.addcourse,name="addcourse"),
    path('courses/addcouponform',views.addcouponform,name="addcouponform"),
    path('courses/addcoupon',views.addcoupon,name="addcopon"),
]
 