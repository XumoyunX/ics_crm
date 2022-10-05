from django.shortcuts import render
from main.models import Course, Blog
from main.serializers import CourseSerializer, BlogSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


def index(r):
    return render(r, 'main/index.html')



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))

def course_list(request):
    if request.method == 'GET':
        snippets = Course.objects.all()
        serializer = CourseSerializer(snippets, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))

def blog_list(request):
    if request.method == 'GET':
        snippets = Blog.objects.all()
        serializer = BlogSerializer(snippets, many=True)
        return Response(serializer.data)