from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid 
# Create your models here.


class User(AbstractUser):
    is_patient= models.BooleanField('Is admin', default=False)
    is_doctor = models.BooleanField('Is customer', default=False)
class Blog (models.Model):
    Category=(('Mental Health','Mental Health'),
    ('Heart Disease','Heart Disease'),
    ('Covid 19','Covid 19'),
    ('Imunization','Imunization '),)
    owner=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    title=models.CharField(max_length=200)
    featured_image=models.ImageField(null=True,blank=True,default="default.jpg")
    select_category=models.CharField(max_length=200,choices=Category)
    description= models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    draft=models.BooleanField(default=False)
    
    id = models.UUIDField(default=uuid.uuid4 , unique=True ,primary_key=True,editable=False)
    
    def __str__(self):
        return self.title