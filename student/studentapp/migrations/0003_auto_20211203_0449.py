# Generated by Django 3.2 on 2021-12-03 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_class',
        ),
        migrations.AddField(
            model_name='student',
            name='class_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='studentapp.class'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.TextField(max_length=200),
        ),
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees_per_month', models.IntegerField()),
                ('class_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='studentapp.class')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='subject',
            field=models.ManyToManyField(to='studentapp.Subject'),
        ),
    ]
