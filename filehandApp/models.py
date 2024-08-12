from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username
    
from django.db import models

class fileUpload(models.Model):
    file_uploaded = models.FileField(upload_to='uploads/')  # You may specify a directory here

    def __str__(self):
        return self.file_uploaded.name


