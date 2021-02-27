from django.db import models

class School(models.Model):
    name = models.TextField(max_length=50, unique=True)
    location = models.TextField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False)
    mobile = models.TextField(max_length=15, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    activate = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False)
    gender = models.TextField(max_length=10, null=True, blank=True)
    address = models.TextField(max_length=250, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    dob = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.TextField(max_length=50, unique=True)
    credit = models.DecimalField(max_digits=5, decimal_places=1, null=False, blank=False)

    def __str__(self):
        return self.name

class School_Teacher(models.Model):
    school_name = models.ForeignKey(School, on_delete=models.CASCADE)
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Student_School_Teacher(models.Model):
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    school_teacher_name = models.ForeignKey(School_Teacher, on_delete=models.CASCADE)

class Student_Subject(models.Model):
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
