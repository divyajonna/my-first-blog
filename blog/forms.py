from django import forms

from .models import post

#PostForm is the name of our Form
class PostForm(forms.ModelForm):
#we need to tell django -that this model is ModelForm


    class Meta:
        #here we tell Django which model should be used to create this form (model = Post).
        model = Post
        fields = ('title','text') #fields to end up in this form
