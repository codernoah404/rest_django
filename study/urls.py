from study import views
from django.urls import path

urlpatterns = [
    path('students/', views.StudentView),
    path('students/<str:name>', views.StudentDetailView),    
    path('score/', views.ScoreView),
    path('score/<int:pk>', views.ScoreDetailView),
]
