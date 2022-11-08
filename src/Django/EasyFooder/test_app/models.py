from django.db import models

# Create your models here.


class Teachers(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
