from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
