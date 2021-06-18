import uuid

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):

    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False,unique=True)
    title = models.CharField('タイトル', max_length=155)
    description = models.TextField('概要')
    image = models.ImageField('イメージ', upload_to='book', null=True, blank=True)
    created = models.DateTimeField('作成日時', auto_now_add=True)
    updated = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
        verbose_name_plural = '本'


class Author(models.Model):

    name = models.CharField('名前', max_length=155)
    introduction = models.TextField('自己紹介文', null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='本', related_name='authors')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'
        verbose_name_plural = '著者'

