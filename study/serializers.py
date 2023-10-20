from rest_framework.serializers import ModelSerializer
from .models import Students, Score

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Students
        fields = ["name", "address", "email"]
        
        
class ScoreSerializer(ModelSerializer):
    class Meta:
        model = Score
        fields = ["Student", "english", "math", 'science', "date"]