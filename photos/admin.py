from django.contrib import admin

from photos.models import Photo, PhotoPet


# Register your models here.

class PhotoPetInline(admin.TabularInline):
    model = PhotoPet
    extra = 1


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'date_of_published', 'get_tagged_pets']
    inlines = [PhotoPetInline]

    @staticmethod
    def get_tagged_pets(obj):
        return ', '.join(str(pet) for pet in obj.tagged_pets.all())