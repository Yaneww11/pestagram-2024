from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from pets.models import Pet
from photos.validators import FileSizeValidator

UserModel = get_user_model()

# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(
        upload_to='',
        validators=[
            FileSizeValidator(5)
        ],
    )

    description = models.TextField(
        max_length=300,
        validators=[
            MinLengthValidator(30)
        ],
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        through='PhotoPet',
    )

    date_of_published = models.DateTimeField(
        auto_now_add=True
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )

class PhotoPet(models.Model):
    pet = models.ForeignKey(to=Pet, on_delete=models.CASCADE)
    photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(auto_created=True, blank=True, null=True)