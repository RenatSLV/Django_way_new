from django.db import models

class Posts(models.Model):
    Title = models.CharField(max_length=255)
    bodyText = models.TextField()
    author = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Title