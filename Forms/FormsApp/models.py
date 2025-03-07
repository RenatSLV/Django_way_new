from django.db import models

class IceCream(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
