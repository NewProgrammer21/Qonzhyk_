from django import forms
from django.contrib.auth.models import User
from .models import Profile, Lesson, Course, Message,Comment,laboratorywork,SRP


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data        
        if cd['password'] != cd['password2']:            
            raise forms.ValidationError('Passwords don\'t match.')        
        return cd['password2']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['information', 'photo', 'roles','adress']


class Lesson_form(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ['title','course','youtube','information','image', 'document']

class LessonZert_form(forms.ModelForm):

    class Meta:
        model = laboratorywork
        fields = ['lesson','title','information', 'document']

class LessonWork_form(forms.ModelForm):

    class Meta:
        model = SRP
        fields = ['lesson','title','information', 'document']


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('recipient','message')

class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'text']