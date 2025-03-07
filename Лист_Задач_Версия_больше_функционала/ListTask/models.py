from django.db import models

# Create your models here.
class Task(models.Model):
    Task = models.CharField(max_length=100)
    Task_Info = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.Task

