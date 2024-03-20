from django.db import models

class ToDo(models.Model):
    todotext = models.CharField(max_length=255)
    tododesc = models.FloatField()
     
    def __str__(self):
        return self.todotext 
