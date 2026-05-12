# blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category'] # ระบุฟิลด์ที่ต้องการให้ User กรอก