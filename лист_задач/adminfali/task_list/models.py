from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=100)
    taskInfo = models.TextField(null=False, blank=True)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
    
    def __str__(self):
        return self.task
