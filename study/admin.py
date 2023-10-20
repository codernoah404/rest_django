from django.contrib import admin
from .models import Students, Score

# Register your models here.

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "email"]
    list_display_links = ["name"]
    
@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ["Student", "english", "math", 'science', "date"]
    list_display_links = ["Student"]
    