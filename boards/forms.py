from cProfile import label
from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):    
    message = forms.CharField(
        widget=forms.Textarea(), 
        max_length=4000,
        help_text='Максимально символов: 4000.',
        label = 'Сообщение'
    )

    class Meta:
        model = Topic
        fields = ['name', 'message']
        labels = {
            'name':'Тема',
        }