# Generated by Django 4.0.5 on 2023-12-14 16:18

import accounts.models
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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_token', models.CharField(blank=True, max_length=150, null=True, verbose_name='Token')),
                ('email_token_date', models.DateTimeField(blank=True, help_text='Время создания Token', null=True, verbose_name='Token Date')),
                ('email_confirm', models.BooleanField(default=False, verbose_name='Email подтвержден')),
                ('image', models.ImageField(default='accounts/avatar_uploads/default.jpg', upload_to=accounts.models.user_directory_path, verbose_name='Аватар')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили пользователей',
            },
        ),
    ]
