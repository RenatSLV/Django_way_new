from django.db import models

from django.db import models
from precise_bbcode.fields import BBCodeTextField

class BBCodeContent(models.Model):
    content = BBCodeTextField()

    def __str__(self):
        return self.content[:50]  # Показать первые 50 символов для удобства
