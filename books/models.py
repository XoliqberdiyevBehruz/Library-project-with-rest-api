from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    isbn = models.CharField(max_length=17)
    author = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title

    