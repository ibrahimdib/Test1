from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ['Name', 'Phone', 'Faculty', 'Email']


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['Title', 'Author', 'Edition', 'Price']


class BuyAdmin(admin.ModelAdmin):
    model = Buy
    list_display = ['Date_Buy', 'Quantity', 'Student_Bought', 'Books_Bought', 'getTotal']


admin.site.register(Student, StudentAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Buy, BuyAdmin)


#what is 3pl: how to select a third party logistics partner
#api drop shipping

