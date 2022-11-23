import razorpay
import json
from django.conf import settings
client = razorpay.Client(auth=(settings.PAYMENT_ID, settings.PAYMENT_KEY))
client.set_app_details({"title" : "LMS", "version" : "1.0.0"})



def pay(amount):
    DATA = {"amount": amount, "currency": "INR","receipt": "Payment Receipt"}
    data = client.order.create(data=DATA)
    razorpay_order_id = data['id']
    callback_url = 'viewCourse/'
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.PAYMENT_ID
    context['razorpay_amount'] = amount
    context['currency'] = data['currency']
    context['callback_url'] = callback_url
    return context

