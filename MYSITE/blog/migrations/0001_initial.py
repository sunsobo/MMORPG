# Generated by Django 4.0.5 on 2023-12-16 20:46

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Дата посл. ред-ия')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-create'],
            },
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Дата посл. ред-ия')),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
                'ordering': ['-create'],
            },
        ),
        migrations.CreateModel(
            name='PostReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Дата посл. ред-ия')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Пост')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создал')),
            ],
            options={
                'verbose_name': 'Отклик',
                'verbose_name_plural': 'Отклики',
                'ordering': ['-create'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.postcategory', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создал'),
        ),
    ]
