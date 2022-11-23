from django.db import models

# Create your models here.
class Login(models.Model):
    id= models.BigAutoField(primary_key=True)
    email = models.TextField(max_length=50)
    role = models.CharField(max_length=10)
    log_token = models.TextField(max_length=50)
    limit = models.IntegerField()

    def __str__(self):
        return self.id


class enrollment_details(models.Model):
    enrollment_id = models.BigAutoField(primary_key=True)
    username = models.TextField(max_length=50)
    course_category  = models.CharField(max_length=20)
    course_name = models.TextField(max_length=50)
    amount = models.IntegerField()
    course_type  = models.CharField(max_length=20)
    payment_mode  = models.CharField(max_length=20)
    payment_type  = models.CharField(max_length=20)
    course_status  = models.CharField(max_length=20)
    enrollment_date = models.DateField()

    def __str__(self):
        return self.username

class user_details(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.TextField(max_length=200)
    Email  = models.TextField(max_length=200)
    phone = models.IntegerField(max_length=15)
    age = models.IntegerField()
    address  = models.TextField(max_length=200)
    employment  = models.CharField(max_length=200)
    occupation  = models.TextField(max_length=2000)
    education  = models.CharField(max_length=200)
    Experience = models.DecimalField(max_digits=3,decimal_places=2)
    skillset = models.TextField(max_length=200)
    photo = models.TextField(max)
    created_date = models.DateField()
    def __str__(self):
        return self.username