from django.db import models


# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=10, blank=False, unique=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200, null=False)
    class_id = models.ManyToManyField(Class)
    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)

    def __str__(self):
        return   self.name


class Student(models.Model):
    student_name = models.CharField(primary_key=True, max_length=200)
    student_dob = models.DateField()
    address = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    school = models.TextField(max_length=200, null=False)
    class_id = models.ForeignKey(Class, on_delete=models.SET_NULL, blank=True, null=True)
    subject = models.ManyToManyField(Subject)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name


class Fees(models.Model):
    class_name = models.OneToOneField(Class, on_delete=models.CASCADE)
    fees_per_month = models.IntegerField()

    def __str__(self):
        return f'{self.class_name}'


class Exams(models.Model):
    subject = models.ManyToManyField(Subject)
    marks = models.IntegerField()
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student}'
