from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('student/',views.student, name='student'),
    path('teacher/',views.teacher, name='teacher'),
    path('manager/',views.manager, name='manager')
]