from django.shortcuts import redirect, render
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.urls import reverse
from urllib.parse import quote_plus, urlencode

from myapp import models
import datetime
from django.db.models import Sum
from django.db.models.functions import TruncMonth

from . import models
from django.http import HttpResponse


def index(request):
    if request.session.get("role") =='Management':
        today=datetime.datetime.now().strftime ("%Y-%m-%d")
        obj = models.enrollment_details.objects.filter(enrollment_date=today)
        amount = obj.aggregate(Sum('amount'))
        enroll_count = models.enrollment_details.objects.count()
        users = models.user_details.objects.filter(created_date=today).count()
        total_sale = models.enrollment_details.objects.aggregate(Sum('amount'))
        monthcount=models.enrollment_details.objects.annotate(month=TruncMonth('enrollment_date')).values('month').annotate(c=Sum('amount')).values('month', 'c')
        
        return render(request,'index.html',context={
                "session": request.session.get("user"),
                "amount" : amount['amount__sum'],
                "usercount" : users,
                "enrollcount" : enroll_count,
                "totalsale" : total_sale['amount__sum']
            }
        )
    else:
        return render(
            request,
            "home.html",
            context={
                "session": request.session.get("user"),
            },
        )
def users(request):
    if request.session.get("role") =='Management':
        return render(request,'./pages/tables.html',context={
                "session": request.session.get("user"),
                
            },
        )
    else:
        return render(request,'home.html')    

def bill(request):
    if request.session.get("role") =='Management':
        return render(request,'./pages/billing.html',context={
                "session": request.session.get("user"),
                
            },
        )
    else:
        return render(request,'home.html')    
def account(request):
    if request.session.get("role") =='Management':
        return render(request,'./pages/profile.html',context={
                "session": request.session.get("user"),
                
            },
        )
    else:
        return render(request,'home.html')    
def course(request):
    if request.session.get("role") =='Management':
        data = models.course.objects.all()
        return render(request,'./pages/course.html',context={
                "session": request.session.get("user"),
                "data":data
            },
        )
    else:
        return render(request,'home.html')               

def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("home")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

def addcourseform(request):
    return render(request,'./pages/addcourse.html')

def addcourse(request):
    if request.method == 'POST':
        coursename = request.POST.get('COURSENAME')
        coursetype = request.POST.get('COURSETYPE')
        #course(cousre_name = coursename,course_type = coursetype).save()
        obj = models.course()
        obj.cousre_name = coursename
        obj.course_type = coursetype
        obj.save()
    return HttpResponse('Record added')  #-----------------------------------------------------------

def addcouponform(request):
    return render(request,'./pages/addcoupon.html')

def addcoupon(request):
    if request.method == 'POST':
        couponcode = request.POST.get('COUPONCODE')
        # models.coupon(coupon_code = couponcode).save()
        obj = models.coupon()
        obj.coupon_code = couponcode        
        obj.save()
    return HttpResponse('Record added')  #------------------------------------------------------------

def fetchingCourse(request):
    data=models.course.objects.all()
    return data
