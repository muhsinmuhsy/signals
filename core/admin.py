from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(MyModel)

admin.site.register(SourceModel)
admin.site.register(DestinationModel)