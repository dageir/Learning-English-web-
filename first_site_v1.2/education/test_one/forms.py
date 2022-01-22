from .models import Exam
from django.forms import ModelForm, TextInput, Textarea


class ExamForm(ModelForm):
    class Meta():
        model = Exam
        fields = ['question', 'answers', 'true_answer']

        widgets = {
            'question': TextInput(attrs={
                'class': 'form-control'
            }),
            'answers': Textarea(attrs={
                'class': 'form-control'
            }),
            'true_answer': TextInput(attrs={
                'class': 'form-control'
            })
        }