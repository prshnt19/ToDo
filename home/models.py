from django.db import models


class ToDo(models.Model):
    task = models.CharField(max_length=100, null=False)
    date = models.DateField(null=False)
    time = models.TimeField(null=False,default='10:00')
    priority = models.IntegerField(null=False, default=3)
    category = models.CharField(max_length=50, null=False, default="None")
    status = models.CharField(max_length=10, null=False, default="active")
