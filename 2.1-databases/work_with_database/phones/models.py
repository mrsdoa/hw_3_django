from django.db import models

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250)

    # мб текст ниже и не нужен
    def __str__(self):
        return f'{self.name, self.price, self.image, self.release_date, self.lte_exists, self.slug}'