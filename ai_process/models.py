from django.db import models
from users.models import User


# Create your models here.
class ImageUpload(models.Model):
    image = models.ImageField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
