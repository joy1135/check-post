from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Comment, Post

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text_com']
        widgets = {
            'text_com': forms.TextInput(attrs={
                'class': 'comment-form__input',
                'placeholder': 'Оставьте комментарий',
                'required': True
            })
        }
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'img']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'post-form__input',
                'placeholder': 'Введите текст поста...',
                'rows': 4
            }),
            'img': forms.ClearableFileInput(attrs={
                'class': 'post-form__file'
            }),
        }