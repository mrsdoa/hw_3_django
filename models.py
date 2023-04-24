# coding=utf-8

from django.db import models


class Book(models.Model):
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateField(u'Дата публикации')

    def __str__(self):
        return self.name + " " + self.author

class Phone(models.Model):
    # id = заполняется по умолчанию
    name = models.CharField(u'Название', max_length=64)
    price = models.CharField(u'Цена', max_length=64)
    image = models.CharField(u'Изображение', max_length=64)
    release_date = models.DateField(u'Дата выпуска', max_length=64)
    lte_exists = models.CharField(u'Связь', max_length=64)
    slug = models.SlugField(u'URL', max_length=64)


