from django.db import models


class City(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Город',
        help_text='Название города'
    )

    def __str__(self):
        return self.name


class Brigada(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Бригада',
        help_text='Название Бригады'
    )
    head = models.CharField(
        max_length=100,
        verbose_name='Начальник',
        help_text='ФИО начальника'
    )
    amount_people = models.IntegerField()
    qualification = models.IntegerField()
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='city',
        verbose_name='Город',
        help_text='Определите город'
    )

    def __str__(self):
        return self.name

class Object(models.Model):
        name = models.CharField(
            max_length=50,
            verbose_name='Объект',
            help_text='Название объкта'
        )
        description = models.TextField(
            max_length=100,
            verbose_name='Описание работ',
            help_text='Описание работ на объекте'
        )
        brigada = models.ForeignKey(
            Brigada,
            on_delete=models.CASCADE,
            related_name='brigada',
            verbose_name='бригада',
            help_text='Определите бригаду'
        )

        def __str__(self):
            return self.name

