from django.db import models

# Create your models here.

class MetaTable(models.Model):
    id = models.AutoField(primary_key=True)
    file_created = models.DateTimeField('date file created')
    file_number = models.IntegerField(default = 0)
    link=models.CharField(max_length=200)
    status= models.CharField(max_length=30)
    title=models.CharField(max_length=400)
    type=models.CharField(max_length=10)

class PassedLegislation(models.Model):
    file_number = models.ForeignKey(MetaTable, on_delete=models.CASCADE)
    action_details = models.CharField(max_length=200)
    action = models.CharField(max_length=100)
    action_by = models.CharField(max_length=100)
    date = models.DateTimeField('date passed')
    version = models.IntegerField(default = 0)


class all_links(models.Model):
    file_number = models.ForeignKey(MetaTable, on_delete=models.CASCADE)
    action_details = models.CharField(max_length=200)
    action = models.CharField(max_length=100)
    action_by = models.CharField(max_length=100)
    date = models.DateTimeField('date passed')
    version = models.IntegerField(default=0)

class votes(models.Model):
    file_number = models.ForeignKey(MetaTable, on_delete=models.CASCADE)
    person = models.CharField(max_length=20)
    vote = models.CharField(max_length=5)
    id = models.AutoField(primary_key=True)
