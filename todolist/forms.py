from django import forms


class TodoListForm(forms.Form):
    text = forms.CharField(label='', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a task...'}))
