from django.db import models

# Create your models here.

class record(models.Model):
    username=models.CharField(max_length=20)
    number=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    platform=models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.username}'