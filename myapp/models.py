from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=250)
    #cuando se crea una funcion dentro de una clase se llama metodo
    def __str__(self):
        return self.name

class Task(models.Model):
    tittle = models.CharField(max_length=250)
    description = models.TextField()
    priject = models.ForeignKey(Project, on_delete=models.CASCADE)
        #cuando se crea una funcion dentro de una clase se llama metodo

    def __str__(self):
        return self.tittle