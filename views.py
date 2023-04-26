from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    # создаём объект класса
    # phone = Phone(name='', price='', release_date='', lte_exists='')
    # phone.save()
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)


# обработчик чтобы посмотреть что уже есть в БД
# def list_phone(request):
#   phone_objects = Phone.objects.order_by('name') #упорядочиваем сортировку по возрастанию
#     phone_objects = Phone.objects.all()
#     phones = [f'{c.id} {c.name}: {c.price}, {c.release_date}' for c in phone_objects]
#     return HttpResponse('<br>'.join(phone))

# для каждого телефона свой каталог
# def create_catalog(request):
#     phones = Phone.objects.all()
#   for phone in phones:
#     Catalog(name='P', phone=phone).save() или Catalog.objects.create(name='P', phone=phone)
#     return HttpResponse('Всё получилось!')

# обработчик чтобы посмотреть что уже есть в БД
#