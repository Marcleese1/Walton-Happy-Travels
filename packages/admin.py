from django.contrib import admin

from.import models


#DISPLAYS THE PACKAGE INFO ON ADMIN PAGE
class Package(admin.ModelAdmin):
    model = models.Packages


admin.site.register(models.Packages)
