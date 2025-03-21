from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Worker(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField()
    start_work = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    whouse_client = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Coment(models.Model):
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field='content_type', fk_field='object_id')

    def __str__(self):
        return self.content

