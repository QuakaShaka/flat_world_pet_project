from cProfile import label
from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):    
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Задайте свой вопрос здесь.'}
        ), 
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

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]