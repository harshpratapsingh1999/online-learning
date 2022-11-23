
from multiprocessing import context


from ast import operator
import datetime
from itertools import count
from types import NoneType
from django.shortcuts import render,redirect
import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from django.db.models import Sum
import http.client

from .forms import user_details_forms
from . import coursedriver
from .forms import user_details_forms
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from . import models
from admindash.models import course as crs
from admindash.models import course_details as cd
from django.http import HttpResponseBadRequest
from admindash.models import coupon_generation

from django.contrib.auth.decorators import login_required

# Create your views here.
import razorpay

global cook





def pay(request):
    global cook
    client = razorpay.Client(auth=(settings.PAYMENT_ID, settings.PAYMENT_KEY))
    client.set_app_details({"title" : "LMS", "version" : "1.0.0"})
    if request.method =="POST":
        coupon = 1000
        amount = 10000
        damount = amount/100
        total_amount = (amount+coupon)/100
        DATA = {"amount": amount, "currency": "INR","receipt": "Payment Receipt"}
        data = client.order.create(data=DATA)
        razorpay_order_id = data['id']
        callback_url = "http://" + "localhost:8000/" + 'payment_status/'
        context = {}
        context['order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.PAYMENT_ID
        context['amount'] = amount
        context['currency'] = data['currency']
        context['callback_url'] = callback_url
        context['coupon'] = coupon/100
        context['total']=total_amount
        context['damount']=damount
        order_status = data['status']
        context["session"]= request.session.get("user")
        cook = request.session.get("user")
        context['status'] = True
        context['key'] = settings.PAYMENT_ID
        if order_status=='created':
            return render(request, 'confirm_order.html', context)
    else:
        return redirect('/')
@csrf_exempt
def payment_status(request):
    
    if request.method == "POST":
        global cook
        client = razorpay.Client(auth=(settings.PAYMENT_ID, settings.PAYMENT_KEY))
        response = request.POST
       
        params_dict = {
            'razorpay_payment_id' : response['razorpay_payment_id'],
            'razorpay_order_id' : response['razorpay_order_id'],
            'razorpay_signature' : response['razorpay_signature']
        }
        # VERIFYING SIGNATURE
        try:
            status = client.utility.verify_payment_signature(params_dict)
            data = coursedriver.fetch_data()
            if status:
                return render(request, 'course.html', {'status': 'Payment Successful','session': cook,'course':json.dumps(data)})
            else:
                return redirect('/')
        except:
            print("error",HttpResponseBadRequest())
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        print("error",HttpResponseBadRequest())
        return redirect('/')
       # if other than POST request is made.
        #return render(request, 'course.html', {"session": request.session.get("user"),})


def index(request):
    if request.session.get("role") =='Management':
        today=datetime.datetime.now().strftime ("%Y-%m-%d")
        obj = models.enrollment_details.objects.filter(enrollment_date=today)
        mamount = obj.aggregate(Sum('amount'))
        print(type(mamount))
        if type(mamount) == NoneType:
            amount=0
        else:
            amount= mamount['amount__sum']
        enroll_count = models.enrollment_details.objects.count()
        users = models.user_details.objects.filter(created_date=today).count()
        total_sale = models.enrollment_details.objects.aggregate(Sum('amount'))
        cat_sale = models.enrollment_details.objects.values('course_category').annotate(totalsale=Sum('amount')).order_by()
        for i in cat_sale:
            if(i['course_category']=='Technology'):
                tech = i['totalsale']
            elif(i['course_category']=='Art'):
                art = i['totalsale']
            elif(i['course_category']=='Management'):
                mgmt = i['totalsale']
        cat_count = models.enrollment_details.objects.values('course_category').annotate(course_count=Count('course_name')).order_by()
        for i in cat_count:
            if(i['course_category']=='Technology'):
                techc = i['course_count']
            elif(i['course_category']=='Art'):
                artc = i['course_count']
            elif(i['course_category']=='Management'):
                mgmtc = i['course_count']
        monthcount=models.enrollment_details.objects.annotate(month=TruncMonth('enrollment_date')).values('month').annotate(c=Sum('amount')).values('month', 'c')
        data = []
        month=datetime.datetime.now().strftime ("%m")
        for i in monthcount:
           data.append([i['c'],int(datetime.datetime.strftime(i["month"],"%m")  )])

        length = len(data)
        jan=0,
        feb=0,
        mar=0,
        apr=0,
        may=0, 
        jun=0, 
        jul=0, 
        aug=0,
        sep=0,
        oct=0, 
        nov=0, 
        dec=0
        for i in range(length):
            if data[i][1] == 1:
                jan=data[i][0]
            elif data[i][1] == 2:
                feb=data[i][0]
            elif data[i][1] == 3:
                mar=data[i][0]
            elif data[i][1] == 4:
                apr=data[i][0]
            elif data[i][1] == 5:
                may=data[i][0]
            elif data[i][1] == 6:
                jun=data[i][0]
            elif data[i][1] == 7:
                jul=data[i][0]
            elif data[i][1] == 8:
                aug=data[i][0]
            elif data[i][1] == 9:
                sep=data[i][0]
            elif data[i][1] == 10:
                oct=data[i][0]
            elif data[i][1] == 11:
                nov=data[i][0]
            elif data[i][1] == 12:
                dec=data[i][0]
        return render(request,'index.html',context={
                "session": request.session.get("user"),
                "amount" : amount,
                "usercount" : users,
                "enrollcount" : enroll_count,
                "totalsale" : total_sale['amount__sum'],
                "jan" : jan,
                "feb": feb,
                "mar" : mar,
                "apr" : apr,
                "may" : may,
                "jun" : jun,
                "jul" : jul,
                "aug" : aug,
                "sep" : sep,
                "oct" : oct,
                "nov" : nov,
                "dec" : dec,
                "tech_sale" : tech,
                "art_sale": art,
                "mgmt_sale" : mgmt,
                "art_count" : artc,
                "tech_count" : techc,
                "mgmt_count" : mgmtc,
            }
        )
    else:
        checks = crs.objects.all()
        context= {}
        types= {}
        for i in checks:
            if (len(cd.objects.filter(course_id_id = i.course_id))) >0 :
                context[i.cousre_name] = cd.objects.filter(course_id_id = i.course_id)[0]
        for i in checks:
            types[i.course_id] = i.course_type
        return render(
            request,
            "home.html",
            context={
                "session": request.session.get("user"),
                "data": types,
                "coursedata":context,
            },
        )


def about(request):
    return render(request, 'about.html', context={
        "session": request.session.get("user"),
        
    })


def course(request):
    
    checks = crs.objects.all()
    context= {}
    types= {}
    for i in checks:
        if (len(cd.objects.filter(course_id_id = i.course_id))) >0 :
            context[i.cousre_name] = cd.objects.filter(course_id_id = i.course_id)[0]
    for i in checks:
        types[i.course_id] = i.course_type
     
    return render(request, 'courses.html', context={
        "session": request.session.get("user"),
        "data": types,
        "coursedata":context
    })


def contact(request):
    return render(request, 'contact.html', context={
        "session": request.session.get("user"),
        
    })

oauth = OAuth()
oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    request.session["usertype"] = request.session.get("user")[
        "userinfo"]["sub"]
    conn = http.client.HTTPSConnection(settings.AUTH0_DOMAIN)
    payload = {"client_id": settings.AUTH0_CLIENT_ID, "client_secret": settings.AUTH0_CLIENT_SECRET,
               "audience": settings.AUTH0_AUDIENCE, "grant_type": "client_credentials"}
    headers = {'content-type': "application/json"}
    conn.request("POST", "/oauth/token", json.dumps(payload), headers=headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))
    request.session["access_token"] = data["access_token"]
    conn = http.client.HTTPSConnection(settings.AUTH0_DOMAIN)
    data = request.session.get("usertype")
    headers = {'authorization': "Bearer "+str(request.session["access_token"])}
    url = f"https://{settings.AUTH0_DOMAIN}/api/v2/users/{data}/roles"
    conn.request("GET", url, headers=headers)
    result = json.loads(conn.getresponse().read().decode("utf-8"))
    if len(result) > 0:
        request.session["role"] = result[0]["name"]
    else:
        request.session["role"] = "Normal User"
    return redirect(request.build_absolute_uri(reverse("home")))


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )


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

def saveuserdata(request):
    data = {'userid': request.session.get("user")['userinfo']['email'],
            'videos': [
                {'link': 'https://www.youtube.com/embed/tgbNymZ7vqY', 'complete': True },
            ]
        }

    coursedriver.save_data(data)
    return "Data Saved"
     

def viewCourse(request):
    data = coursedriver.fetch_data()

    # print("this is the course data")
    # print(data)

    

    context = {}
    context["session"] = request.session.get("user")
    for obj in data:
        print(data[obj])
    course = [
            {
                'course_name': data[obj]['course_name'],
                'urls': data[obj]['urls']
            }
        for obj in data
        ]
    context['course'] = json.dumps(course)
    return render(request, 'course.html',context)
    
def profile(request):
    context = {}
    context["session"] = request.session.get("user")
    return render(request, 'profile.html', context)

def isfloat(num):
    
    try:
        if num.isnumeric():
            return False
        else:
          float(num)
          return True

    except ValueError:
        return False



def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def editProfile(request):

    if request.method == 'POST':
        context = {}
        
        context["session"] = request.session.get("user")
        formData = request.POST
        userForm = models.user_details()
        if userForm.photo == '':
            userForm.photo = context['session']['userinfo']['picture'].encode()
        
        notRquiredKeys = ['_state', 'user_id']
        res = {}
        for key in userForm.__dict__.keys():
            if key not in notRquiredKeys:
                res[key] = formData[key]
        for key, val in res.items():  
            if isint(val):
                res[key] = int(val)    
            if isfloat(val):
                   res[key] = float(val)
        for key, val in res.items():
                print(key, type(val))

                setattr(userForm, key, val)
        userForm.save()    
        return render(request, 'profile.html', context)

        
        

    


def course_detail(request):
    context = {}
    context["session"] = request.session.get("user")
    
    if request.method == "POST":
        checks = crs.objects.filter(cousre_name = request.POST.get('course_name'))[0]
        data = cd.objects.filter(course_id_id = checks.course_id)[0]

        
        context['cname'] = request.POST.get('course_name')
        context['ctype'] = request.POST.get('course_type')
        context['course_desc']= data.course_desc
        context['duration'] = data.duration
        context['course_cost'] =data.course_cost
        if request.POST.get('course_type') == 'free':
            return render(request, 'coursedetail.html',context)
        else:
            checks = crs.objects.filter(cousre_name = request.POST.get('course_name'))[0]
            data = cd.objects.filter(course_id_id = checks.course_id)[0]
            context['course_desc']= data.course_desc
            context['duration'] = data.duration
            context['course_cost'] = data.course_cost
            context['allCoupon'] = json.dumps(
                [
                    {
                        'amount': int(obj.amount),
                        'code': int(obj.coupon_code)
                    }
                    for obj in coupon_generation.objects.all()
                ]
            )
            context['cname'] = request.POST.get('course_name')
            context['ctype'] = request.POST.get('course_type')
            return render(request, 'coursedetail.html',context)
    else:
        return redirect('/')

    




