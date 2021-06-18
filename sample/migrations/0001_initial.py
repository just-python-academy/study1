# Generated by Django 3.2.4 on 2021-06-15 10:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=155, verbose_name='タイトル')),
                ('description', models.TextField(verbose_name='概要')),
                ('image', models.ImageField(blank=True, null=True, upload_to='book', verbose_name='イメージ')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name_plural': '本',
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='名前')),
                ('introduction', models.TextField(blank=True, null=True, verbose_name='自己紹介文')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='sample.book', verbose_name='本')),
            ],
            options={
                'verbose_name_plural': '著者',
                'db_table': 'author',
            },
        ),
    ]