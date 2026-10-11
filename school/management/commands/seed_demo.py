
import random
from datetime import timedelta
from decimal import Decimal

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone

from school.models import Classroom, Parent, Student, Attendance, Grade

PASSWORD = "Demo@2026"

CLASSES = {
    "2/أ": ["أحمد محمد", "سارة علي", "يوسف حسن", "مريم إبراهيم",
            "عمر خالد", "نور الدين", "ليلى محمود", "كريم سامي"],
    "3/ب": ["آدم طارق", "جنى أيمن", "ياسين هاني", "ملك وائل",
            "زياد رامي", "هدى عماد", "مصطفى ناصر", "رنا شريف"],
}
SUBJECTS = ["رياضيات", "علوم", "عربي", "إنجليزي"]


def demo_user(username, first_name, hashed):
    """ينشئ المستخدم أو يحدّثه، ويعيّن الباسورد دايمًا."""
    user, _ = User.objects.get_or_create(
        username=username, defaults={"first_name": first_name})
    user.first_name = first_name
    user.password = hashed
    user.save()
    return user


class Command(BaseCommand):
    help = "يملا المنصة ببيانات تجريبية للعرض على العميل"

    def handle(self, *args, **opts):
        random.seed(7)
        today = timezone.localdate()
        hashed = make_password(PASSWORD)   # التشفير مرة واحدة بس

        demo_user("demo_teacher", "أ. منى", hashed)

        n = 0
        for cname, names in CLASSES.items():
            classroom, _ = Classroom.objects.get_or_create(name=cname)
            for name in names:
                n += 1
                user = demo_user(f"demo_parent{n}",
                                 f"ولي أمر {name.split()[0]}", hashed)
                parent, _ = Parent.objects.get_or_create(
                    user=user, defaults={"phone": f"0100000{n:04d}"})
                student, new = Student.objects.get_or_create(
                    name=name, classroom=classroom, defaults={"parent": parent})
                if not new:
                    continue

                # الحضور: آخر 30 يوم، من غير الجمعة والسبت
                absent_p = random.choice([0.03, 0.05, 0.1, 0.2])
                records = []
                for i in range(30):
                    d = today - timedelta(days=i)
                    if d.weekday() in (4, 5):
                        continue
                    r = random.random()
                    status = "A" if r < absent_p else "L" if r < absent_p + 0.06 else "P"
                    records.append(Attendance(student=student, date=d, status=status))
                Attendance.objects.bulk_create(records, ignore_conflicts=True)

                # الدرجات
                ability = random.uniform(0.5, 0.98)
                for subj in SUBJECTS:
                    mx = random.choice([50, 100])
                    score = round(mx * min(1, max(0.2, random.gauss(ability, 0.08))), 1)
                    Grade.objects.create(student=student, subject=subj,
                                         score=Decimal(str(score)),
                                         max_score=Decimal(mx))

        self.stdout.write(self.style.SUCCESS(
            f"تم. المدرس: demo_teacher / أولياء الأمور: demo_parent1 .. demo_parent{n} / الباسورد: {PASSWORD}"))