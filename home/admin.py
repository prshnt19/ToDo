from django.contrib import admin
from .models import ToDo


class ToDoEntry(admin.ModelAdmin):
    list_display = ('id', 'task', 'date', 'time', 'priority', 'category', 'status')


admin.site.register(ToDo, ToDoEntry)
