from django.db import models

class User(models.Model):
    owner = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.owner


class User2QuerySet(models.QuerySet):
    def adults(self):
        return self.filter(age__gte=18)

    def with_email(self, email):
        return self.filter(email=email)


class MyObjects(models.Manager):
    def get_queryset(self):
        return User2QuerySet(self.model, using=self._db)

    def adults(self):
        return self.get_queryset().adults()

    def with_email(self, email):
        return self.get_queryset().with_email(email)


class User2(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    age = models.IntegerField()

    objects = MyObjects()

    def __str__(self):
        return self.name
