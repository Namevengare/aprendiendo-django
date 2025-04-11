from django import forms 

class createNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=250)
    description = forms.CharField(label="descripcion de la tarea",widget=forms.Textarea)

class createNewProject(forms.Form):
    name = forms.CharField(label="Nombre del project", max_length=200)

    