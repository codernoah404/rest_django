from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Students, Score
from .serializers import StudentSerializer, ScoreSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.


@api_view(['GET', 'POST'])
def StudentView(request):
    if request.method == 'GET':
        qs = Students.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET',"POST"])
def ScoreView(request):
    qs = Score.objects.all()
    
    if request.method == "GET":
        serializer = ScoreSerializer(qs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
       serializer = ScoreSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    



@api_view(["GET","PUT","DELETE"])
def StudentDetailView(request, name):
    qs = get_object_or_404(Students, pk=name)
    
    if request.method == 'GET':
        serializer = StudentSerializer(qs)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
@api_view(["GET","PUT","DELETE"])
def ScoreDetailView(request, pk):
    qs = get_object_or_404(Score, pk=pk)
    print(qs)

    if request.method == 'GET':
        serializer = ScoreSerializer(qs)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ScoreSerializer(qs, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    