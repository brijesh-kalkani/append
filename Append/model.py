from django.db import models

class employeeModel(models.Model):
    empName = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    salary = models.IntegerField()


