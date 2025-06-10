from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-student', views.add_student, name='add-student'),
    path('student-view/<int:id>', views.student_view, name='student-view'),
    path('attendent-view', views.attendent_view, name='attendent-view'),
    path('payment', views.payment, name='payment'),
    path('student-show-list', views.student_show_list, name='student-show-list'),
    path('payment-show-list', views.payment_show_list, name='payment-show-list'),
    path('update-student/<int:id>', views.update_student, name='update-student'),
    path('delete-student/<int:id>', views.delete_student, name='delete-student'),
]
