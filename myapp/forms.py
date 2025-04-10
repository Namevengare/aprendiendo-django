from django import forms 

class createNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=250)
    description = forms.CharField(label="descripcion de la tarea",widget=forms.Textarea)