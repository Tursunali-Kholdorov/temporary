from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    order = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
