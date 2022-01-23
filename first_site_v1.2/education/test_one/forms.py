from .models import Exam, TestingWithChangeAnswer
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


class TestWChA(ModelForm):
    class Meta():
        model = TestingWithChangeAnswer
        fields = ['question', 'answer1', 'answer2', 'answer3', 'answer4', 'true_answer']

        widgets = {
            'question': Textarea(attrs={
                'class': 'form-control'
            }),
            'answer1': TextInput(attrs={
                'class': 'form-control'
            }),
            'answer2': TextInput(attrs={
                'class': 'form-control'
            }),
            'answer3': TextInput(attrs={
                'class': 'form-control'
            }),
            'answer4': TextInput(attrs={
                'class': 'form-control'
            }),
            'true_answer': TextInput(attrs={
                'class': 'form-control'
            })
        }

