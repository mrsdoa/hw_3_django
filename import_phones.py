import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            next(phones)  # не читаем 1-ю строку csv
            for phone in phones:
            # TODO: Добавьте сохранение модели
                one_line = Phone.objects.create(
                    id = int(phone[0]),
                    name = phone[1],
                    image = phone[2],
                    price = int(phone[3]),
                    release_date = phone[4],
                    lte_exist = phone[5],
                    slug = slugify(phone[1]),
                )

