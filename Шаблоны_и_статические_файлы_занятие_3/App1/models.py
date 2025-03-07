from django.db import models

class Film(models.Model):
    class Zhanr(models.TextChoices):
        DRAMA = 'DR', 'Драма'  
        COMEDY = 'CO', 'Комедия'  
        THRILLER = 'TH', 'Триллер'  
        HORROR = 'HO', 'Ужасы'  
        ACTION = 'AC', 'Боевик'  
        FANTASY = 'FN', 'Фэнтези'  
        SCI_FI = 'SF', 'Научная фантастика'
    
    name = models.CharField(max_length=255)
    img = models.ImageField(default=None)
    zhanr = models.CharField(max_length=2, choices=Zhanr.choices)
    year = models.IntegerField()
    country = models.CharField(max_length=255)
    view = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)