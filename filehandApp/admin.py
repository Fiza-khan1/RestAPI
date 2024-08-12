from django.contrib import admin
from .models import CustomUser
from .models import fileUpload
admin.site.register(CustomUser)
admin.site.register(fileUpload)