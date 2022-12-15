from django.db import models

class Meal(models.Model):
    meal_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    price = models.DecimalField(decimal_places=2, max_digits=6)


class Tag(models.Model):
    tag_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=15)
    
class Meal_tag(models.Model):
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    meal_id = models.ForeignKey(Meal, on_delete=models.CASCADE)
    