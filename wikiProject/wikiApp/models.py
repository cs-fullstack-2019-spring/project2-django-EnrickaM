from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class newuserModel(models.Model):
    first_name=models.CharField(max_length=200,default='')
    last_name=models.CharField(max_length=200,default='')
    # date_of_birth=models.DateField(default="")
    email=models.EmailField(max_length=200,default='')
    username=models.CharField(max_length=200,default='')
    password=models.CharField(max_length=200,default='')
    confim_password=models.CharField(max_length=200,default='')
    def __str__(self):
        return "This new user is: " + str(self.username)


class wikipostModel(models.Model):
    title=models.CharField(max_length=200,default='')
    text=models.TextField(max_length=200,default='')
    datecreated=models.DateField(null=True,default='')
    lastupdate=models.DateField(null=True,default='')
    author=models.ForeignKey(newuserModel, on_delete=models.CASCADE, blank=True, null=True)


#
class relativeItemsModel(models.Model):
    subject=models.CharField(max_length=200,default='')
    photo=models.FileField(null=True,blank=True)
    description=models.CharField(max_length=200,default='')
    links=models.ForeignKey(wikipostModel,on_delete=models.CASCADE, blank=True, null=True)

