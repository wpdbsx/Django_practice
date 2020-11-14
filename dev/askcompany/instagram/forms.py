from django import forms
from .models import Post 
import re


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= [
            
            'message',
            'photo',
            'tag_set',
        'is_public',
        ]
        #exclude = [] 배제한다.
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message :
            message =re.sub(r'[a-zA-Z]+','',message)
            len(message) > 20
        return message 