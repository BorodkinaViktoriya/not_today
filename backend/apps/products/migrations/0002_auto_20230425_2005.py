# Generated by Django 3.2.18 on 2023-04-25 17:05

import django.db.models.deletion
from django.db import migrations, models

import apps.products.utils


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, help_text='Добавить описание к категории.', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, help_text='Добавить изображение к категории.', upload_to=apps.products.utils.get_upload_to, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Указывает, что этот объект является активный. Снять выделение вместо удаления.', verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='Добавить слаг не блее 256 символов. Слаг должен быть уникальным для каждой категории.', max_length=256, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(help_text='Добавить название категории не блее 256 символов.', max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=True, help_text='Указывает, что этот объект является активный. Снять выделение вместо удаления.', verbose_name='Активный')),
                ('title', models.CharField(help_text='Добавить название товара не более 256 символов.', max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Добавить слаг не более 256 символов. Слаг должен быть уникальным для каждого товара.', max_length=256, verbose_name='Слаг')),
                ('preview', models.TextField(help_text='Добавить короткое описание к товару.', verbose_name='Короткое описание')),
                ('description', models.TextField(help_text='Добавить подробное описание к товару.', verbose_name='Описание')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Цена')),
                ('image', models.ImageField(upload_to=apps.products.utils.get_upload_to, verbose_name='Изображение')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]