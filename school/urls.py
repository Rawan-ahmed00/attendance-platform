from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("classrooms/", views.classroom_list, name="classroom_list"),
    path("attendance/<int:pk>/", views.take_attendance, name="take_attendance"),
    path("grades/<int:pk>/", views.add_grades, name="add_grades"),
    path("parent/", views.parent_dashboard, name="parent_dashboard"),
    path("export/<int:pk>/", views.export_attendance, name="export_attendance"),
    path("dashboard/", views.manager_dashboard, name="manager_dashboard"),
    path("import/", views.import_students, name="import_students"),
    path("teachers/", views.manage_teachers, name="manage_teachers"),
    path("manifest.webmanifest", views.manifest, name="manifest"),
    path("sw.js", views.service_worker, name="service_worker"),
]