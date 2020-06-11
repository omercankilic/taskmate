from django.contrib import admin

from todolist_app.models import TaskList#import the model that you want to register
#from todolist_app.models import TestTasks
# Register your models here.

#Adding simple registration file
admin.site.register(TaskList)
#admin.site.register(TestTasks)