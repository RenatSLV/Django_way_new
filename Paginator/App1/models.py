from django.db import models

class Book(models.Model):
    class Zhanr(models.TextChoices):
        DRAMA = 'DR', 'Драма'  
        COMEDY = 'CO', 'Комедия'  
        THRILLER = 'TH', 'Триллер'  
        HORROR = 'HO', 'Ужасы'  
        ACTION = 'AC', 'Боевик'  
        FANTASY = 'FA', 'Фэнтези'  


    name_book = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_year = models.IntegerField()
    zhanr = models.CharField(max_length=2, choices=Zhanr.choices)
    created_at_post = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_book


