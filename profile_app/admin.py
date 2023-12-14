from django.contrib import admin

from profile_app import models


# Register your models here.
@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Rank)
class ProfileAdmin(admin.ModelAdmin):
    pass