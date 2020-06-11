from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Tasks will be seen as object in database 
class TaskList(models.Model):
    manage = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)

    #since we are noot editing from database no need to make migrations again
    def __str__(self):#This function is to return taskname not object
        return self.task + " - " +str(self.done)

     

"""
class TestTasks(models.Model):
    name_of_task = models.CharField(max_length=25)
    task_significance = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(100)])
    
    def __str__(self):
        return self.name_of_task + " #Task significance# : " + str(self.task_significance)
"""