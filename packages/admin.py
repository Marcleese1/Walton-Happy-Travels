from django.contrib import admin

from.import models


class Package(admin.ModelAdmin):
    model = models.Packages


admin.site.register(models.Packages)
