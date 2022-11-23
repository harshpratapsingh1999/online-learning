from statistics import mode
from django.db import models

# Create your models here.
class course(models.Model):
    course_id = models.BigAutoField(primary_key=True)
    cousre_name = models.TextField(max_length=50)
    course_type  = models.CharField(max_length=20)

    def __str__(self):
        return self.cousre_name

class course_details(models.Model):
    course_d_id = models.BigAutoField(primary_key=True)
    course_id = models.ForeignKey(course, on_delete=models.CASCADE)
    course_cost = models.TextField(max_length=50)
    course_desc  = models.TextField(max_length=100)
    instructor  = models.CharField(max_length=20)
    duration  = models.TimeField()
    created_date = models.DateField()

    def __str__(self):
        return self.course_desc

class coupon(models.Model):
    coupon_id = models.BigAutoField(primary_key=True)
    coupon_code = models.TextField(max_length=50)

    def __str__(self):
        return self.coupon_code

class coupon_generation(models.Model):
    coupon_g_id = models.BigAutoField(primary_key=True)
    coupon_id = models.ForeignKey(coupon, on_delete=models.CASCADE)
    coupon_code = models.TextField(max_length=50)
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    def __str__(self):
        return self.coupon_code


class certificate_details(models.Model):
    certificate_id = models.BigAutoField(primary_key=True)
    unique_no = models.TextField(max_length=14)
    qrcode = models.TextField(max_length=50)
    username  = models.TextField(max_length=100)
    instructor  = models.CharField(max_length=20)
    issue_date  = models.DateField()
    validity_for = models.IntegerField()

    def __str__(self):
        return self.unique_no


class videos(models.Model):
    video_id = models.BigAutoField(primary_key=True)
    course_id = models.ForeignKey(course, on_delete=models.CASCADE)
    coursename = models.TextField(max_length=50)
    video_link = models.TextField(max_length=500)

    def __str__(self):
        return self.coursename

