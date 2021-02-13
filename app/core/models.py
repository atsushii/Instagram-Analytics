from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,\
    PermissionsMixin
from django.utils import timezone
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and save new user"""
        if not email:
            raise ValueError('user must have email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that uses email instead of usename"""
    email = models.EmailField(max_length=255, unique=True)
    instagram_account = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()
    USERNAME_FIELD = 'email'


class InstagramAccount(models.Model):
    """Instagram account that collects daily information"""
    counts_followed_by = models.IntegerField(default=0)
    profile_picture_url = models.URLField(max_length=200)
    counts_media = models.IntegerField(default=0)
    counts_follow = models.IntegerField(default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


class InstagramMedia(models.Model):
    """Store reactions for posted media"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_time = models.TimeField()
    link_to_media = models.URLField(max_length=200)
    comments_count = models.IntegerField(default=0)
    media_type = models.CharField(max_length=255)
    links_count = models.IntegerField(default=0)
    tags = models.ManyToManyField('InstagramMediaTag')
    locations = models.ManyToManyField('InstagramMediaLocation')


class InstagramComment(models.Model):
    """Store users comments for posted media"""
    from_username = models.CharField(max_length=255)
    comment = models.TextField()
    created_time = models.TimeField()
    media = models.ForeignKey(
        InstagramMedia,
        on_delete=models.CASCADE
    )


class InstagramMediaTag(models.Model):
    """Store posted media tags"""
    tag = models.CharField(max_length=255)


class InstagramMediaLocation(models.Model):
    """Store posted media location"""
    location = models.CharField(max_length=255)
