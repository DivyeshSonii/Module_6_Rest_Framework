from django.db import models

# Create your models here.
class Book_Model(models.Model):
    Title = models.CharField(max_length=150)
    Author = models.CharField(max_length=150)
    Isbn = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.Title