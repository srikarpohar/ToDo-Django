from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('task_title','task_description','is_important_task')
        labels = {
            "task_title": 'Task Title',
            "task_description": 'Task Description',
            "is_important_task": 'Favourite'
        }

        def __init__(self, *args, **kwargs):
            super(TodoForm,self).__init__(*args, **kwargs)
            self.fields['task_title'].empty_label = "Select"
            self.fields['is_important_task'].required = False