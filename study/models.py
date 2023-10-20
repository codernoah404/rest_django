from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(primary_key=True, max_length=10)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name
    
class Score(models.Model):
    Student = models.ForeignKey(Students, on_delete=models.CASCADE)
    english =  models.IntegerField(null=False)
    math = models.IntegerField(null=False)
    science = models.IntegerField(null=False )
    date = models.DateTimeField(auto_now_add=False)