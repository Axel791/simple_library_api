from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    ADMINISTRATOR = "AD"
    MODERATOR = "MD"
    LIBRARY_ASSISTANT = "LA"
    ORDINARY_USER = "OU"

    USER_ROLE = [
        (ADMINISTRATOR, "Администратор"),
        (MODERATOR, "Модератор"),
        (LIBRARY_ASSISTANT, "Библиотекарь"),
        (ORDINARY_USER, "Пользователь")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    user_status = models.CharField(
        max_length=2,
        choices=USER_ROLE,
        default=ORDINARY_USER,
        verbose_name="Роль пользователя"
    )
    address = models.CharField(max_length=100, null=True, verbose_name="Адрес")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    last_action = models.DateTimeField(auto_now=True, verbose_name="Последние действия")

    @property
    def full_name(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "user_profile"
