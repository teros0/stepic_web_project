from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title.strip():
            raise forms.ValidationError(u'Title is empty',
                                    code='validation_error')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text.strip():
            raise forms.ValidationError(u'Text is empty',
                                    code='validation_error')
        return text

    def save(self):
        self.cleaned_data['author_id'] = 1
        quest = Question(**self.cleaned_data)
        quest.save()
        return quest

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text.strip():
            raise forms.ValidationError(u'Text is empty',
                                    code='validation_error')
        return text

    def clean_question(self):
        question = self.cleaned_data['question']
        if question == -123:
            raise forms.ValidationError(u'Question number is incorrect', code='validation_error')
        return question

    def save(self):
        self.cleaned_data['question'] = get_object_or_404(Question, pk=self.cleaned_data['question'])
        self.cleaned_data['author_id'] = 1
        answ = Answer(**self.cleaned_data)
        answ.save()
        return answ

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError(u'Enter username')
        try:
            User.objects.get(username=username)
            print("Get")
            raise forms.ValidationError(u'User exists')
            print("Get")
        except:
            print("Except")
            pass
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError(u'Enter password')
        self.rawpass = password
        return make_password(password)

    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError(u'Enter username')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError(u'Enter password')
        return password

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(u'Wrong name or password')
        if not user.check_password(password):
            raise forms.ValidationError(u'Wrong name or password')
