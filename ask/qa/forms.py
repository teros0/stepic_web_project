from django import forms
from qa.models import Question, Answer
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