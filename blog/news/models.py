from django.db import models


class News(models.Model):
    title = models.CharField('Назва новини', max_length=75)
    announce = models.CharField('Анонс новини', max_length=300)
    image_url = models.CharField('Посилання на зображення', max_length=500)
    news_url = models.CharField('Посилання на новину', max_length=500)
    date = models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новину'
        verbose_name_plural = 'Новини'


class Restaurants(models.Model):
    restaurant_link = models.CharField('Посилання на заклад', max_length=500)
    restaurant_img = models.CharField('Посилання на фотографію закладу', max_length=500)
    restaurant_mark = models.CharField('Тип закладу', max_length=75)
    restaurant_name = models.CharField('Назва закладу', max_length=150)
    restaurant_location = models.CharField('Адреса закладу', max_length=100)

    def __str__(self):
        return self.restaurant_name

    class Meta:
        verbose_name = 'Заклад'
        verbose_name_plural = 'Заклади'


class Article(models.Model):
    article_img = models.CharField('Посилання на фотографію статті', max_length=500)
    article_title = models.CharField('Назва статті', max_length=100)
    article_announce = models.CharField('Анонс статті', max_length=500)
    article_content = models.TextField('Вміст статті')
    article_publication = models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Статтю'
        verbose_name_plural = 'Статті'


class Video(models.Model):
    video_link = models.CharField('Посилання на відео', max_length=500)
    video_name = models.CharField('Назва відео', max_length=75)

    def __str__(self):
        return self.video_name

    class Meta:
        verbose_name = 'Відео'
        verbose_name_plural = 'Відео'
