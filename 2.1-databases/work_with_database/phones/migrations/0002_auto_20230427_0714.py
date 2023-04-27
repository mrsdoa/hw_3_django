# Generated by Django 3.2.18 on 2023-04-27 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
    ]
