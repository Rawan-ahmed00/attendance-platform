from django.contrib import admin
from .models import Classroom, Parent, Student, Attendance, Grade

admin.site.register(Classroom)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Grade)