from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')
    file = models.FileField(upload_to='documents/', null=True)

    def __str__(self):
        return self.title