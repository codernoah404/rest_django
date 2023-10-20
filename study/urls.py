from study import views
from django.urls import path

urlpatterns = [
    path('students/', views.StudentView),
]
