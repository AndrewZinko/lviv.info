# Generated by Django 4.0.5 on 2022-06-05 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_img', models.CharField(max_length=500, verbose_name='Посилання на фотографію статті')),
                ('article_title', models.CharField(max_length=100, verbose_name='Назва статті')),
                ('article_announce', models.CharField(max_length=500, verbose_name='Анонс статті')),
                ('article_content', models.TextField(verbose_name='Вміст статті')),
                ('article_publication', models.DateTimeField(verbose_name='Дата публікації')),
            ],
            options={
                'verbose_name': 'Статтю',
                'verbose_name_plural': 'Статті',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Назва новини')),
                ('announce', models.CharField(max_length=300, verbose_name='Анонс новини')),
                ('image_url', models.CharField(max_length=500, verbose_name='Посилання на зображення')),
                ('news_url', models.CharField(max_length=500, verbose_name='Посилання на новину')),
                ('date', models.DateTimeField(verbose_name='Дата публікації')),
            ],
            options={
                'verbose_name': 'Новину',
                'verbose_name_plural': 'Новини',
            },
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_link', models.CharField(max_length=500, verbose_name='Посилання на заклад')),
                ('restaurant_img', models.CharField(max_length=500, verbose_name='Посилання на фотографію закладу')),
                ('restaurant_mark', models.CharField(max_length=75, verbose_name='Тип закладу')),
                ('restaurant_name', models.CharField(max_length=150, verbose_name='Назва закладу')),
                ('restaurant_location', models.CharField(max_length=100, verbose_name='Адреса закладу')),
            ],
            options={
                'verbose_name': 'Заклад',
                'verbose_name_plural': 'Заклади',
            },
        ),
    ]
