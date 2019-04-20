from django.views.generic import TemplateView
from django.shortcuts import render , redirect
from home.forms import HomeForm
from home.models import Post
from django.contrib.auth.models import User
##the name is optipnally
##template_name is afunction inherited from TemplateView
class Homeview (TemplateView):
    template_name='home/home.html'


    def get(self , request):
##the class HomeForm can be passed as a form
##by the functions which we inheited from forms.Form(the superclass of HomeForm)
        form = HomeForm()
        ##to get data from database
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)

        args =  {'form':form , 'posts':posts , 'users':users}
        return render(request , self.template_name , args)



    def post(self,request):
##this is fill the form with the data that the user enters
        form = HomeForm(request.POST)
        if form.is_valid():
            ## 'post ' name is optilanlly
            post = form.save(commit = False)
            ##asking about the user who is posting
            ##to prevent an error of NULL raise
            post.user = request.user
            post.save()
##this line cleans the data that entered in the fill to not to be a malicious one that may harm our website
##'text ' doesn`t appear in the home page cuz the web redirect to the home page


##to make the form blank after submitting
            form = HomeForm()
            ##to request Get to demonstrate the data under the form
            return redirect('home:home')

        args =  {'form':form , 'text':text}
        return render(request , self.template_name , )
