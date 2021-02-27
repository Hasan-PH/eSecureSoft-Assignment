from django.contrib import admin

from .models import School, Teacher, Student, Subject, School_Teacher, Student_School_Teacher, Student_Subject

admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(School_Teacher)
admin.site.register(Student_School_Teacher)
admin.site.register(Student_Subject)

