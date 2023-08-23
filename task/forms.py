from django import forms
from .models import Task

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border mt-1'


class NewTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'list', 'body', 'start_time', 'end_time')
        widgets = {
            'list': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'body': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'start_time': forms.DateInput(attrs={
                'class': INPUT_CLASSES
            }),
            'end_time': forms.DateInput(attrs={
                'class': INPUT_CLASSES
            }),
        }


class EditTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'list', 'body', 'start_time', 'end_time')
        widgets = {
            'list': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'body': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'start_time': forms.DateInput(attrs={
                'class': INPUT_CLASSES
            }),
            'end_time': forms.DateInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
