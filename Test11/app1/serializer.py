from rest_framework import serializers
from .models import *


class SerializersStudent(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class SerializersBook(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class SerializersBuy(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Buy
        fields = '__all__'

