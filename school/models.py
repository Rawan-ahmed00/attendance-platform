from django.db import models
from django.contrib.auth.models import User


class Classroom(models.Model):
    name = models.CharField("اسم الفصل", max_length=100)
    teacher = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="classrooms", verbose_name="المدرس",
    )

    def __str__(self):
        return self.name


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField("رقم الموبايل", max_length=20)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Student(models.Model):
    name = models.CharField("اسم الطالب", max_length=150)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        Parent, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="children",
    )

    def __str__(self):
        return self.name


class Attendance(models.Model):
    STATUS = [("P", "حاضر"), ("A", "غائب"), ("L", "متأخر")]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField("التاريخ")
    status = models.CharField("الحالة", max_length=1, choices=STATUS)

    class Meta:
        unique_together = ("student", "date")  # مينفعش يتسجل مرتين في نفس اليوم

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField("المادة", max_length=100)
    score = models.DecimalField("الدرجة", max_digits=5, decimal_places=2)
    max_score = models.DecimalField("الدرجة النهائية", max_digits=5, decimal_places=2, default=100)
    date = models.DateField("التاريخ", auto_now_add=True)
    note = models.TextField("ملاحظة", blank=True)

    def percent(self):
        return round(float(self.score) * 100 / float(self.max_score))

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.score}/{self.max_score}"