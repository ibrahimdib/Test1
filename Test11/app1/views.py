from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from rest_framework.permissions import *
from .serializer import *


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = SerializersStudent
    permission_classes = [AllowAny]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = SerializersBook
    # permission_classes = [IsAuthenticated]


class BuyViewSet(viewsets.ModelViewSet):
    queryset = Buy.objects.all()
    serializer_class = SerializersBuy
    permission_classes = [IsAdminUser]


def getStudentList(request):
    data = Student.objects.values()
    context = {
        'response': data,
    }
    return render(request, 'studentList.html', context)


def getStudentDetails(request):
    data = Student.objects.values()
    context = {
        'response': data,
    }
    return render(request, 'studentDetails.html', context)
