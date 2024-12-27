from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

UserModel = get_user_model()

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=30)

    personal_photo = models.URLField()

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        blank=True,
        null=True,
        unique=True,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs ):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
