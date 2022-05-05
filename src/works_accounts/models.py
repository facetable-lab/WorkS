from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


# Модель для создания пользователя (подписчика)
class SubscriberManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# Модель настроек пользователя (подписчика)
class Subscriber(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    city = models.ForeignKey('works_core.City', on_delete=models.SET_NULL, null=True, blank=True)
    specialization = models.ForeignKey('works_core.Specialization', on_delete=models.SET_NULL, null=True, blank=True)
    is_mailing = models.BooleanField(default=True)

    objects = SubscriberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
