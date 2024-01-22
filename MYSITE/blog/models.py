from django.db import models

from django.contrib import messages


from django.contrib.auth.models import User
# без загрузки картинок
# from ckeditor.fields import RichTextField

# с возможностью загружать картинки
from ckeditor_uploader.fields import RichTextUploadingField


# BEGIN PostCategory
class PostCategory(models.Model):
    class Meta():
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['create']

    title = models.CharField(
        verbose_name='Название',
        max_length=60
    )
    slug = models.SlugField(
        verbose_name='Slug',
        unique=True,
    )
    
    
    create = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )
    update = models.DateTimeField(
        'Дата посл. ред-ия',
        auto_now=True,
    )

    def __str__(self):
        return str(self.title)
# END PostCategory




# BEGIN Post
class Post(models.Model):
    class Meta():
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-create']
    
    category = models.ForeignKey(
        'PostCategory',
        verbose_name='Категория',
        on_delete=models.CASCADE,
        default=1,
    )
    
    user = models.ForeignKey(
        User,
        verbose_name='Создал',
        on_delete=models.CASCADE,
    )
    
    title = models.CharField(
        verbose_name='Название',
        max_length=60
    )
    text = RichTextUploadingField(
        'Текст',
        config_name='default'
    )
    
    create = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )
    update = models.DateTimeField(
        'Дата посл. ред-ия',
        auto_now=True,
    )
    
    def __str__(self):
        return str(self.title)
# END Post



# BEGIN PostReply
class PostReply(models.Model):
    class Meta():
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
        ordering = ['-create']
    
    post = models.ForeignKey(
        'Post',
        verbose_name='Пост',
        on_delete=models.CASCADE
    )
    
    user = models.ForeignKey(
        User,
        verbose_name='Создал',
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        'Текст',
        max_length=1000,
    )
    
    # Отклик Принят / Не принят
    confirm_mark = models.BooleanField(
        'Принято',
        default=False,
    )
    
    create = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )
    update = models.DateTimeField(
        'Дата посл. ред-ия',
        auto_now=True,
    )
    
    def __str__(self):
        return str(self.post.title)
# END PostReply