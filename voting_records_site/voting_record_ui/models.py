from django.db import models

# Create your models here.

class MetaTable(models.Model):
    #id = models.AutoField(primary_key=True)
    file_created = models.DateTimeField('date file created')
    file_number = models.IntegerField(default = 0)
    link=models.CharField(max_length=200)
    status= models.CharField(max_length=30)
    title = models.TextField("description", null=True, blank=True)
    type=models.CharField(max_length=10)

class PassedLegislation(models.Model):
    #id = models.AutoField(primary_key=True)
    file_number = models.IntegerField(default=0)
    A_Details = models.TextField("description", null=True, blank=True)
    Action = models.TextField("action", null=True, blank=True)
    Action_By = models.CharField(max_length=100)
    Date = models.DateTimeField('date passed')
    Version = models.TextField(default='0')

class all_links(models.Model):
    #id = models.AutoField(primary_key=True)
    file_number = models.IntegerField(default=0)
    A_Details = models.TextField("description", null=True, blank=True)
    Action = models.TextField("action", null=True, blank=True)
    Action_By = models.CharField(max_length=100)
    Date = models.TextField('date passed',blank=True, null=True)
    Version = models.TextField(default='0')

class votes(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.CharField(max_length=20)
    vote = models.CharField(max_length=10)
    file_number = models.IntegerField(default=0)
    #id = models.AutoField(primary_key=True)
