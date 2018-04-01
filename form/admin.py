from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Patient)
admin.site.register(MedClerkPreSed)
admin.site.register(ProcReport)
admin.site.register(PostInject1)
admin.site.register(PostInject2)
