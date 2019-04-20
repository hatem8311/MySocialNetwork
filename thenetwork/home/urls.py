from django.conf.urls import url
from home.views import Homeview
urlpatterns = [
##as_view is define the class "Homeview" as aview
##as_view inherited from the superclass of TemplateView
##TemplateView is the superclass of Homeview
##as_view is used to make the urls resolver see the Homeview class as a function not as a class
##cuz the url resolver expect a function not a class 

   url(r'^$' , Homeview.as_view(), name ='home')


]
