from django.contrib import admin
from .models import Hotel,\
                    Image,\
                    OpeningHours

admin.site.register(Hotel)
admin.site.register(Image)
admin.site.register(OpeningHours)
