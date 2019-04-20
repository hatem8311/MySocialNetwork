from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    ##a field of data of creation
    created = models.DateTimeField(auto_now_add=True)
    ## a field of data of updating
    updated = models.DateTimeField(auto_now=True)

class Friends(models.Model):
    users = models.ManyToManyField(User)

##ManyToManyField has the ability to have alot of diffrent objects ,so will be able to store every relationship between every tow users in  as object
