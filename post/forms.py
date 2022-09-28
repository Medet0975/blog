from django import forms
from post.models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("name", "description", "image")

        # def save(self, commit=True):

