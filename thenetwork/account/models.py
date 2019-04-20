from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

##the name of this class is optionally
##models.Manager is the base to be able too make the manager
##we are making our coustom model manager
class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager , self).get_queryset().filter(city='london')
## NOTICE : evey time we make a change in the model we need to make migrations
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description  = models.CharField( max_length = 100, default = '')
    city  = models.CharField(max_length = 100,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    ## blank is used to make the field optional
    image = models.ImageField(upload_to = 'profile_image' , blank = True)
    ## this function to make the name of the user name appear either "UserProfilopbject"
    def __str__(self):
        return self.user.username

##this function says do an userprofile in each time an user is created
def create_profile(sender , **kwargs):
    if kwargs['created']:
        user_profile =UserProfile.objects.create(user = kwargs['instance'])


post_save.connect(create_profile , sender = User)
# Create your models here.
