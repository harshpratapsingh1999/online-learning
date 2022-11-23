from unicodedata import name
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('course/',views.course,name="course"),
    path('viewCourse/', views.viewCourse, name='viewCourse'),
    path('profile/', views.profile, name='profile'),
    path("login/", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
    path("create_order/", views.pay, name="create_order"),
    path('payment_status/', views.payment_status, name = 'payment_status'),
    path('save/', views.saveuserdata, name = 'payment_status'),
    path('editProfile/', views.editProfile, name='editProfile'),
    path('course_detail/', views.course_detail, name='course_detail'),

]
 