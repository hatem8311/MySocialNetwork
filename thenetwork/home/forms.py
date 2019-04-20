from django import forms
from home.models import Post


class HomeForm(forms.ModelForm):
##post is the name before the form :this stuff done by forms.Form
## in line 7,8 we are adding our attributes to make out form nicer - we use bootstrap class
     ##making the post field in the model ass a form to input in
     post = forms.CharField(widget = forms.TextInput(
     ## attrs isn`t optionally name
     attrs = {
            'class':'form-control',
            'placeholder':'Write your post here....'
     }
     ))


     class Meta:
         ##the model that the class (the form) will be linked to
         model = Post
         ##the fields tha will appear in the form page
         fields = ('post',)
