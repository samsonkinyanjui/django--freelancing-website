from typing import no_type_check
from django.db import models

from django.contrib.auth.models import User, update_last_login
from django.db.models.aggregates import Max
from django.db.models.fields import NullBooleanField
 
 
 # Create your models here.
class writer(models.Model):

        user = models.OneToOneField(User , on_delete=models.CASCADE)
        first_name =models.CharField(max_length=30 , default='none')
        second_name =models.CharField(max_length=30 , default='none')
        
        username =models.CharField(max_length=30 , default='none')
      
        last_login=models.DateField(auto_now=True)
        created=models.DateField(auto_now=True)
        total_balance=models.IntegerField(default=0)
        

        
        
        email=models.CharField(max_length=30 , default='none')
        phone =models.CharField(max_length=30 , default='none')
        mpesa_code=models.CharField(max_length=30,default='none')
        inviter_number  =       models.IntegerField(default=0)
        inviter_name    =       models.CharField(max_length=50, default="name")
        number = models.IntegerField(default=150)
        # long_url = models.URLField()
        # short_url = models.CharField(max_length=15, unique=True, blank=True)


        

        def __str__(self):
                return self.user.username
class Bids(models.Model):
        writer = models.ForeignKey(writer, null=True, on_delete=models.CASCADE)
        post=models.TextField(max_length=3000,default='none')
        cat=models.CharField(max_length=30,default='none')
        price=models.CharField(max_length=30,default='none')
        per=models.CharField(max_length=30,default='none')
        code=models.CharField(max_length=30,default="0x245")
        status=models.CharField(max_length=30,default='Active')
        

class pay(models.Model):
        writer = models.ForeignKey(writer, null=True, on_delete=models.CASCADE)
        
        username=models.CharField(max_length=30,default='none')
        code1=models.CharField(max_length=30,default="0x245")
        mpesa_code=models.CharField(max_length=30,default='none')
        created=models.DateField(auto_now=True)

        def __str__(self):
                return self.user.username
        
class comp(models.Model):
        writer = models.ForeignKey(writer, null=True, on_delete=models.CASCADE)
       
        upload1=models.TextField(max_length=30000,default='Attached(Bid)')
        username=models.CharField(max_length=30,default='none')
        mpesa_code=models.CharField(max_length=30,default='none')
        code=models.CharField(max_length=30,default='none')
        documents=models.FileField(null=True,blank=True,upload_to="files/")
        date_uploaded=models.DateField(auto_now=True)
class withdraw(models.Model):
        amount=models.IntegerField(default=0)

        phone=models.CharField(max_length=30,default='none')
        balance=models.IntegerField(default=0)
class transction (models.Model):
        type =models.CharField(max_length=30,)
        amount=models.IntegerField(default=0)
        phone=models.CharField(max_length=30,default='none')
        
        


        

       
