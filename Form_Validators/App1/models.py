from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    cteared_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
