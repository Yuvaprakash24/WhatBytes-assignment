from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from cloudinary.models import CloudinaryField
# Create your models here.
class User(AbstractUser):
    email = models.EmailField("email",unique=True)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    profile_picture = CloudinaryField(folder='profile_pics', blank=True, null=True)
    def __str__(self):
        return self.username