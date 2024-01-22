from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


import uuid
import os


from PIL import Image

def crop_center(img, crop_width: int, crop_height: int) -> Image:
    """
    Функция для обрезки изображения по центру.
    """
    img_width, img_height = img.size
    return img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


# upload path
def user_directory_path(instance, filename):
    now = timezone.now()
    
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    
    return 'accounts/avatar_uploads/user_{0}/{1}/{2}/{3}'.format(
        instance.user.id,
        str(now.year),
        str(now.month) + '_' + str(now.day),
        filename
    )
    
    
    
# BEGIN Profile
class Profile(models.Model):
    '''Модель профиля'''
    class Meta():
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили пользователей'
    
    email_token = models.CharField(
        'Token',
        max_length=150,
        null=True,
        blank=True,
    )
    email_token_date = models.DateTimeField(
        'Token Date',
        help_text='Время создания Token',
        null=True,
        blank=True,
    )
    email_confirm = models.BooleanField(
        'Email подтвержден',
        default=False,
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    
    image = models.ImageField(
        'Аватар',
        default='accounts/avatar_uploads/default.jpg',
        upload_to=user_directory_path,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        default_path = 'accounts/avatar_uploads/default.jpg'
        if default_path not in self.image.path:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
            
            img = Image.open(self.image.path)
            img = crop_center(img, min(img.size), min(img.size))
            img.save(self.image.path)
        
    def user_email(self):
        return self.user.email
# END Profile