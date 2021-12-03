# Generated by Django 3.2 on 2021-12-03 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0006_exams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exams',
            name='subject',
        ),
        migrations.AddField(
            model_name='exams',
            name='subject',
            field=models.ManyToManyField(to='studentapp.Subject'),
        ),
    ]