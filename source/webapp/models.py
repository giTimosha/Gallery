from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    pictures = models.ImageField(null=True, blank=True,
                                 upload_to='photo', verbose_name='Картинка')
    text = models.TextField(null=True, blank=True, max_length=2000, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    likes = models.IntegerField(default=0, verbose_name='Лайк')
    author_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                    null=True, blank=True, max_length=50, verbose_name='Автор фотки')

    def __str__(self):
        return self.text


class Comments(models.Model):
    text = models.TextField(null=True, blank=True, max_length=2000, verbose_name='Текст')
    photo = models.ForeignKey('webapp.Photo', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Фотография')
    author_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                    null=True, blank=True, max_length=50, verbose_name='Автор комента')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


class Like(models.Model):
    pass
