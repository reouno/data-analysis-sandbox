"""Models of Account app"""
import uuid as uuid_lib

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    ref: https://tech.serhatteker.com/post/2020-01/email-as-username-django/
    """

    def create_user(
            self,
            email: str = None,
            username: str = None,
            password: str = None,
            **extra_fields
    ):
        """
        Create and save a User with the given email and password.
        """
        if not email and not username:
            raise ValueError(_('email or username must be set'))

        if email:
            # Use email as both username and email
            email = self.normalize_email(email)
            user = self.model(username=email, email=email, **extra_fields)
        else:
            # Use username if email is not set
            user = self.model(username=username, **extra_fields)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username: str, password: str, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('first_name', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username=username, email=username, password=password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Customized based on AbstractUser
    Use `email` as unique identifier instead of `username`
    """
    uuid = models.UUIDField(default=uuid_lib.uuid4,
                            primary_key=True, editable=False)

    # Email address can be used as username and it's max length is 320.
    username = models.CharField(_('visible user id'), unique=True, max_length=320)

    first_name = models.CharField(_('first name'), max_length=64, blank=True)
    last_name = models.CharField(_('last name'), max_length=64, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        """User model config"""
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        """clean"""
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
