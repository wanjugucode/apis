from django.db import models
from django.db.models import fields

# Create your models here.
class Login(models.Model):
    email=models.EmailField(max_length=25)
    password=models.CharField(max_length=16)

class Registration(models.Model):
    first_name=models.CharField(max_length=13)
    last_name=models.CharField(max_length=13)
    phone_number=models.CharField(max_length=16)
    email=models.EmailField(max_length=25)
    password=models.CharField(max_length=16)

class DashBoardBillList(models.Model):
    id_number=models.CharField(max_length=16)
    bill_name=models.CharField(max_length=25)
    bill_icon_image=models.ImageField(null=True)

class UploadBillPhoto(models.Model):
    bill_photo=models.ImageField(null=True)

class BillDetails(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=26)
    account=models.CharField(max_length=25)
    amount=models.IntegerField()
    available_payment_method_details=models.CharField(max_length=30)
    
class PaymentConfirmationDetails(models.Model):
    name=models.CharField(max_length=17)


# Create your models here.
