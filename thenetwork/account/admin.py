from django.contrib import admin
from account.models import UserProfile

##UserProfileAdmin is not a mandatory name
##list_display is a function in (admin.ModelAdmin)
class UserProfileAdmin(admin.ModelAdmin):
##list_display is determine fields that will appear in the model
##user , website , city , etc....... is inherited from admin.ModelAdmin
    list_display = ('user','user_info' , 'website' , 'city' , 'phone')

##here we are asking for displaying each corresponding description for the
##obj name is not  mandatory
    def user_info(self , obj):
        return obj.description
## get_queryset is a function has been inherited from admin.ModelAdmin
##get_queryset is importing the data from the database
    def get_queryset(self , request):
##super is for saying that we do not want to overwritte (queryset) completely
## we want to use it but customize it a little bit
##self here is a refrence to the object that being passed through this class
        queryset = super(UserProfileAdmin , self).get_queryset(request)
##re order the sort of coloumns in userprofile by the phone number
## "-" is for reversing the original order
## 'user' is the second way for ordering if the users have the same phone number
        queryset = queryset.order_by('-phone' , 'user')
##the line above is calling the method (get_queryset)
        return queryset

## this line is for modifying the name os user_info
    user_info.short_description = 'Info'
##this line should be below the class UserProfileAdmin or it will cause an error
admin.site.register(UserProfile,UserProfileAdmin)

# Register your models here.
