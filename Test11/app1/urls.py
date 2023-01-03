from django.urls import path, include
from . import views
from . views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)
router.register(r'book', BookViewSet)
router.register(r'buy', BuyViewSet)

urlpatterns = [
 path('student_names/', views.getStudentList, name='getStudentList'),
 path('student_details/', views.getStudentDetails, name='getStudentDetails'),
 path('myapi/', include(router.urls)),

]