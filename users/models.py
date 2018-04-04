from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from django.db.migrations.migration import swappable_dependency

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=100, blank=True)
    
    class Meta(AbstractUser.Meta):
        pass
