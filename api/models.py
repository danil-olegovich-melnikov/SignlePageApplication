from datetime import date

from django.db import models


# Create your models here.
class SomeModel(models.Model):
    date = models.DateField("Дата", default=date.today)
    name = models.CharField("Название", max_length=255)
    amount = models.IntegerField('Количество')
    distance = models.PositiveSmallIntegerField('Расстояние')
    objects = models.Manager()

    def __str__(self):
        return f'SomeModel[{self.pk}] - {self.name}'

    class Meta:
        db_table = 'some_model'
        ordering = ['-date']
