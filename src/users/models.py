from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from src.base.validators import get_path_upload_avatar, validate_size_image_avatar


# class UserRole(models.TextChoices):
#     """Роли пользователей."""
#
#     LIDER = 'lr', _('Руководитель компании')
#     EMPLOYEE = 'ee', _('Сотрудник компании')


class User(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("Пользователь"), null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, unique=True)
    nickname = models.CharField(max_length=150, blank=True, default='nobody')
    country = CountryField()
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        default='default/default_avatar.png',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), validate_size_image_avatar]
    )
    tiktok = models.URLField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.username


class Follower(models.Model):
    """ Подписчики """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} подписан на {self.user}'
