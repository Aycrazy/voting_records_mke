# Generated by Django 2.2 on 2019-04-18 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_record_ui', '0004_auto_20190418_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_links',
            name='Version',
            field=models.TextField(default='0'),
        ),
        migrations.AlterField(
            model_name='passedlegislation',
            name='Version',
            field=models.TextField(default='0'),
        ),
    ]
