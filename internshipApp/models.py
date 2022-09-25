from django.db import models
# Create your models here.

class Login(models.Model):
    # title = models.CharField(max_length=10)
    updated_at = models.DateTimeField(auto_now=True)
