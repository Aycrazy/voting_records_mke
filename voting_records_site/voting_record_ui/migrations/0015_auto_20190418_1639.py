# Generated by Django 2.2 on 2019-04-18 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_record_ui', '0014_auto_20190418_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='file_number',
            field=models.IntegerField(default=0),
        ),
    ]
