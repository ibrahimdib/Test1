from django.db import models
from datetime import datetime


class Book(models.Model):
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    Title = models.CharField(max_length=40)
    Author = models.CharField(max_length=30)
    Edition = models.CharField(max_length=30)
    Price = models.PositiveIntegerField()

    def __str__(self):
        return self.Author

    def getPrice(self):
        return self.Price


class Student(models.Model):
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    Name = models.CharField(max_length=30)
    Phone = models.CharField(max_length=30)
    Faculty = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)

    def __str__(self):
        return self.Name


class Buy(models.Model):
    class Meta:
        verbose_name = 'Buy'
        verbose_name_plural = 'Buy'

    Date_Buy = models.DateField(default=datetime.now())
    Quantity = models.PositiveIntegerField()
    Student_Bought = models.ForeignKey(Student, on_delete=models.CASCADE)
    Books_Bought = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.DateBuy

    @property
    def getTotal(self):
        return self.Books_Bought.Price * self.Quantity
