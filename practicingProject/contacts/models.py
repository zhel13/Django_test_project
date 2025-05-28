from django.db import models
from django.utils.text import slugify


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
    )
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.id}")
        super().save(*args, **kwargs)