from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meals(models.Model):
    """
    Meals details for Customer
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=400)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to='media/', default=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meals, self).save(*args, **kwargs)

    class Meta:
        """
        Class Meta
        """
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

    def __str__(self):
        return str(self.name)
